def make_context(name: str, display_name: str) -> google.cloud.aiplatform_v1beta1.types.context.Context:
    context = {
        'name': name,
        'display_name': display_name
    }

    return context

def make_update_mask() -> google.protobuf.field_mask_pb2.FieldMask:
    update_mask = {
        'paths': [
            'display_name'
        ]
    }

    return update_mask

