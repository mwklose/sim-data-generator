import polars as pl

class Equation():

    def __init__(self, input_str: str) -> None:
        pass


    # TODO: hint - match operators first, then alter non-operators into tokens (variables or values)
    def evaluate_df(self, df: pl.DataFrame) -> pl.Series: ...

    def evaluate(self, **kwargs) -> float: ...