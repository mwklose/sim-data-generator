# Postfix Evaluators - should be straightforward?
from typing import List
from equations.tokens import Operator, Scalar, Variable 
import polars as pl


def postfix_eval(postfix_stack: List[Operator | Scalar | Variable]) -> float: ...

def postfix_eval_df(postfix_stack: List[Operator | Scalar | Variable], df: pl.DataFrame) -> pl.Series: ...