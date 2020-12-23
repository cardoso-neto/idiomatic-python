
from typing import Any, Callable, Iterable


def apply_norm(
    datarow_values: Any,
    normalization: Callable,
    first_value: str,
    second_value: str,
):
    for event in datarow_values:
        for observation in event.values:
            if observation.attribute.is_categorical:
                continue

            if observation.is_missing_value and observation.observation_value is None:
                raise ValueError("Error: Missing value found and imputation flag is null")

            observation.observation_value = normalization(
                define_value(observation), 
                getattr(observation.attribute, first_value),
                getattr(observation.attribute, second_value),
            )
    return datarow_values


class ToNorm:
    """Normalize data accordingly."""
    def __init__(self, z_score: bool) -> None:
        super().__init__()
        self.scaler = self.std_scale if z_score else self.min_max_scale
        
    def __call__(self, datarow_values: Iterable, metadata: str) -> Iterable:
        return self.scaler(datarow_values)

    def min_max_scale(self, datarow_values):
        """
        Normalize numeric observations into a <0, 1> range.
        """
        return apply_norm(
            datarow_values, standard_scaler, "mean", "std"
        )

    def std_scale(self, datarow_values):
        """
        Normalize numeric values using z-score (mean=0, and standard deviation=1).
        """
        return apply_norm(
            datarow_values, standard_scaler, "mean", "std"
        )


normalizer = ToNorm(z_score=True)
normed_datarow_values = normalizer(datarow_values, metadata={})