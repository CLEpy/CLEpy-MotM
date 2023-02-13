"""
# My first app
Here's our first attempt at using data to create a table:
"""

import numpy as np
import pandas as pd

import streamlit as st

# Basic Display of Data

st.markdown("## Displaying Data")

st.write("Here's our first attempt at using data to create a table")

df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})

# st.write(200_00_0)

st.dataframe(df)

## Display Styled Dataframe

df2 = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df2.style.highlight_max(axis=0))

## Display Line Chart

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)

## Display Map Data

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
)

st.map(map_data)

## Slider Widget

st.markdown("## Simple Widgets")

x: int = st.slider("x")  # 👈 this is a widget

st.write(x, "squared is", x * x)

## Checkbox Widget

if st.checkbox("Show dataframe"):
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    st.table(chart_data)

## Select box Widget

df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})

option = st.selectbox("Which number do you like best?", df["first column"])

st.write("You selected: ", option)

## Layout

## Add a selectbox to the sidebar:

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?", ("Email", "Home phone", "Mobile phone")
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))

## Columns

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button("Press me!")

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        "Sorting hat", ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin")
    )
    st.write(f"You are in {chosen} house!")
