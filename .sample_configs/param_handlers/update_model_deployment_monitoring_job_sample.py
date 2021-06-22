def make_model_deployment_monitoring_job(name: str, display_name: str) -> google.cloud.aiplatform_v1beta1.types.model_deployment_monitoring_job.ModelDeploymentMonitoringJob:
    model_deployment_monitoring_job = {
        'name': name,
        'display_name': display_name
    }

    return model_deployment_monitoring_job

def make_update_mask() -> google.protobuf.field_mask_pb2.FieldMask:
    update_mask = {
        'paths': [
            'display_name'
        ]
    }

    return update_mask

