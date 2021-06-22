def make_index_endpoint(name: str, display_name: str) -> google.cloud.aiplatform_v1beta1.types.index_endpoint.IndexEndpoint:
    index_endpoint = {
        'name': name,
        'display_name': display_name
    }

    return index_endpoint

def make_update_mask() -> google.protobuf.field_mask_pb2.FieldMask:
    update_mask = {
        'paths': [
            'display_name'
        ]
    }

    return update_mask

