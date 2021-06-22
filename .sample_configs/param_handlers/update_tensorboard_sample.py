def make_tensorboard(name: str, display_name: str) -> google.cloud.aiplatform_v1beta1.types.tensorboard.Tensorboard:
    tensorboard = {
        'name': name,
        'display_name': display_name
    }

    return tensorboard

def make_update_mask() -> google.protobuf.field_mask_pb2.FieldMask:
    update_mask = {
        'paths': [
            'display_name'
        ]
    }

    return update_mask

