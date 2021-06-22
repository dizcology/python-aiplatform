def make_tensorboard_run(name: str, display_name: str) -> google.cloud.aiplatform_v1beta1.types.tensorboard_run.TensorboardRun:
    tensorboard_run = {
        'name': name,
        'display_name': display_name
    }

    return tensorboard_run

def make_update_mask() -> google.protobuf.field_mask_pb2.FieldMask:
    update_mask = {
        'paths': [
            'display_name'
        ]
    }

    return update_mask

