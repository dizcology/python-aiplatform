def make_request(trial_name: str) -> google.cloud.aiplatform_v1beta1.types.vizier_service.AddTrialMeasurementRequest:
    request = {
        'trial_name': trial_name
    }

    return request

