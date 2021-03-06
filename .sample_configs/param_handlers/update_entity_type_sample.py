def make_entity_type(name: str, display_name: str) -> google.cloud.aiplatform_v1beta1.types.entity_type.EntityType:
    entity_type = {
        'name': name,
        'display_name': display_name
    }

    return entity_type

def make_update_mask() -> google.protobuf.field_mask_pb2.FieldMask:
    update_mask = {
        'paths': [
            'display_name'
        ]
    }

    return update_mask

