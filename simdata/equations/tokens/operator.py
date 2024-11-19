from typing import Protocol
import polars as pl


# TODO: basic arithmetic operators
# TODO: logical operators

class Operator(Protocol): 

    def get_precedence(self) -> int: ...

    def evaluate(self, a, b) -> float: ...

    def evaluate_df(self, a_series: pl.Series, b_series: pl.Series) -> pl.Series: ...