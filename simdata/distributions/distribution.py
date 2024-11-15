from abc import ABC, abstractmethod
import polars as pl

@ABC
class Distribution():

    @abstractmethod
    def simulate_n(self, n: int, covariates: pl.DataFrame):
        ...