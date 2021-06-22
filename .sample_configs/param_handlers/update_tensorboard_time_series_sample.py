def make_tensorboard_time_series(name: str, display_name: str) -> google.cloud.aiplatform_v1beta1.types.tensorboard_time_series.TensorboardTimeSeries:
    tensorboard_time_series = {
        'name': name,
        'display_name': display_name
    }

    return tensorboard_time_series

def make_update_mask() -> google.protobuf.field_mask_pb2.FieldMask:
    update_mask = {
        'paths': [
            'display_name'
        ]
    }

    return update_mask

