from abc import abstractmethod
from typing import Protocol, Self
import polars as pl
import numpy as np

class Distribution(Protocol):

    @staticmethod
    def construct(**kwargs) -> Self: ...


    def pdf(self, observations) -> np.ndarray: ...

    def cdf(self, observations) -> np.ndarray: ...


    @abstractmethod
    def simulate_n(self, n: int, covariates: pl.DataFrame):
        ...