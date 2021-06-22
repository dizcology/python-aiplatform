def make_parent(parent: str) -> str:
    parent = parent

    return parent

def make_requests(parent: str,
description: str) -> typing.Sequence[google.cloud.aiplatform_v1beta1.types.featurestore_service.CreateFeatureRequest]:
    requests = {
        'parent': parent,
        'feature': {
            'description': description
        }
    }

    return requests

