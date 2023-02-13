from enum import Enum

import igviz as ig
import networkx as nx
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

LatLng = tuple[float, float]


class StrEnum(str, Enum):
    def __str__(self) -> str:
        return str.__str__(self)


class EdgeWeight(StrEnum):
    TOTAL_REVENUE = "total_revenue"
    TOTAL_DISTANCE = "total_distance"
    LINEHAUL_COST = "linehaul_cost"
    EMPTY_DISTANCE = "empty_distance"
    NUM_ORDERS = "num_orders"


def create_edge_tooltip(edge_attr: EdgeWeight):
    def _(df: pd.DataFrame):
        edge_attr_val = df[edge_attr].map("{:,.2f}".format)

        return (
            df["pickup_area"]
            .str.cat(df["delivery_area"], sep=" ➡️ ")
            .str.cat(edge_attr_val, sep=f" | {edge_attr}: ")
        )

    return _


def build_graph_view(CN: nx.DiGraph):
    # Update each node with a name attribute
    for area in CN.nodes():
        CN.nodes[area]["name"] = area

    return ig.plot(
        CN,
        title="",
        layout="circular",
        node_label="name",
        edge_text=["label"],
    )


def _calc_arrow_pos(start_latlng: LatLng, end_latlng: LatLng, length=0.2, width=0.005):
    A = np.array([start_latlng[1], start_latlng[0]])
    B = np.array([end_latlng[1], end_latlng[0]])
    v = B - A
    w = v / np.linalg.norm(v)
    u = np.array([-w[1], w[0]]) * 10  # u orthogonal on w

    P = B - length * w
    S = P - width * u
    T = P + width * u

    lon = [S[0], T[0], B[0], S[0]]
    lat = [S[1], T[1], B[1], S[1]]

    return lon, lat


def build_map_view(CN: nx.DiGraph, latlng_df: pd.DataFrame):
    fig = go.Figure()
    longitudes = []
    latitudes = []
    arrow_traces = []

    for orig_area, dest_area, data in CN.edges(data=True):
        start_latlng: LatLng = tuple(latlng_df.loc[orig_area])
        end_latlng: LatLng = tuple(latlng_df.loc[dest_area])

        longitudes.extend([start_latlng[1], end_latlng[1]])
        latitudes.extend([start_latlng[0], end_latlng[0]])

        arrow_lon, arrow_lat = _calc_arrow_pos(start_latlng, end_latlng)

        # Create Arrow Traces
        arrow_traces.append(
            go.Scattermapbox(
                lon=arrow_lon,
                lat=arrow_lat,
                text=data["label"],
                mode="lines",
                fill="toself",
                fillcolor="blue",
                line_color="blue",
            )
        )

    # Add Line Traces
    fig.add_trace(
        go.Scattermapbox(
            mode="markers+lines",
            lon=longitudes,
            lat=latitudes,
            marker={"size": 10, "color": "black"},
            line={"width": 3},
            opacity=0.3,
        )
    )

    # Add Arrow Traces
    fig.add_traces(arrow_traces)

    # Add Marker Traces
    fig.add_trace(
        go.Scattermapbox(
            lon=latlng_df["AREA_LONGITUDE"],
            lat=latlng_df["AREA_LATITUDE"],
            mode="markers",
            hoverinfo="text",
            text=latlng_df.index,
            marker={"size": 14, "color": "rgb(255, 0, 0)"},
        )
    )

    fig.update_layout(
        showlegend=False,
        mapbox={
            "bearing": 0,
            "center": {"lat": 38, "lon": -94},
            "pitch": 0,
            "zoom": 3,
            "style": "open-street-map",
        },
    )

    return fig


if __name__ == "__main__":
    st.title("Carrier Network Visualzation")

    EDGE_WEIGHTS = [w.value for w in EdgeWeight]

    with st.sidebar:
        uploaded_file = st.file_uploader("Upload Carrier Network Data")
        selected_edge_weight: EdgeWeight = st.radio("Choose Edge Weight", EDGE_WEIGHTS)

    if not uploaded_file:
        st.text("Please upload carrier network data.")
    else:
        network_df = pd.read_csv(uploaded_file)
        area_latlng_df = pd.read_csv("data/area_latlong.csv", index_col="AREA_LABEL")

        CN = nx.from_pandas_edgelist(
            df=network_df.assign(label=create_edge_tooltip(selected_edge_weight)),
            source="pickup_area",
            target="delivery_area",
            edge_attr=EDGE_WEIGHTS + ["label"],
            create_using=nx.DiGraph,
        )

        st.subheader("Graph View")

        graph_fig = build_graph_view(CN)
        st.plotly_chart(graph_fig, use_container_width=True)

        st.subheader("Map View")

        map_fig = build_map_view(CN, area_latlng_df)
        st.plotly_chart(map_fig, use_container_width=True)
