from pyodbc import Row
from sqlparams import SQLParams
from aiosql.types import SQLOperationType
from typing import Optional


class SQLServerAdapter:
    """ Database Driver Adapter based on the pydobc db driver """

    def __init__(self) -> None:
        self.qformatter = SQLParams("named", "qmark")

    @staticmethod
    def process_sql(query_name: str, op_type: SQLOperationType, sql: str) -> str:
        return sql

    @staticmethod
    def get_column_names(cursor) -> list[str]:
        return [col[0] for col in cursor.description]

    def select(self, conn, _query_name, sql, parameters, record_class=None):
        cur = conn.cursor()

        if parameters:
            fmt_sql, params = self.qformatter.format(sql, parameters)
        else:
            fmt_sql, params = sql, ()

        cur.execute(fmt_sql, params)

        results = cur.fetchall()

        if record_class is not None:
            column_names = self.get_column_names(cur)
            results = [record_class(**dict(zip(column_names, row))) for row in results]

        return results

    def select_one(self, conn, _query_name, sql, parameters, record_class=None) -> Optional[Row]:
        cur = conn.cursor()
        fmt_sql, params = self.qformatter.format(sql, parameters)
        cur.execute(fmt_sql, params)

        result = cur.fetchone()

        if result is not None and record_class is not None:
            column_names = self.get_column_names(cur)
            result = record_class(**dict(zip(column_names, result)))

        return result

    def insert_update_delete(self, conn, _query_name, sql, parameters):
        cur = conn.cursor()
        fmt_sql, params = self.qformatter.format(sql, parameters)
        cur.execute(fmt_sql, params)

    def insert_update_delete_many(self, conn, _query_name, sql, parameters):
        cur = conn.cursor()
        cur.fast_executemany = True
        fmt_sql, params = self.qformatter.formatmany(sql, parameters)

        cur.executemany(fmt_sql, params)
