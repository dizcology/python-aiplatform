def make_request(name: str) -> google.cloud.aiplatform_v1beta1.types.vizier_service.StopTrialRequest:
    request = {'name': name}

    return request

