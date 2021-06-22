def make_tensorboard_run(tensorboard_run: str) -> str:
    tensorboard_run = tensorboard_run

    return tensorboard_run

def make_time_series_data(tensorboard_time_series_id: str) -> typing.Sequence[google.cloud.aiplatform_v1beta1.types.tensorboard_data.TimeSeriesData]:
    time_series_data = [{'tensorboard_time_series_id': tensorboard_time_series_id}]

    return time_series_data

