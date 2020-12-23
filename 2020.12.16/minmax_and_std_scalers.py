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


class MinMaxScaler(normalizadorL1):
    """
    Normalize numeric observations into a <0, 1> range.
    """
    def __call__(self, datarow_values, metadata):
        return apply_norm(
            datarow_values, min_max_normalization, "min", "max"
        )


class StdScaler:
    """
    Normalize numeric values using z-score (mean=0, and standard deviation=1).
    """
    def __call__(self, datarow_values, metadata):
        return apply_norm(
            datarow_values, standard_scaler, "mean", "std"
        )


class ToNorm:
    """Normalize data accordingly."""
    def __init__(self, z_score: bool) -> None:
        super().__init__()
        self.scaler = StdScaler() if z_score else MinMaxScaler()

    def __call__(self, datarow_values: Iterable, metadata: Any) -> Iterable:
        return self.scaler(datarow_values)