# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START aiplatform_v1beta1_search_model_deployment_monitoring_stats_anomalies_sample]
from google.cloud import aiplatform_v1beta1


def search_model_deployment_monitoring_stats_anomalies_sample(
    model_deployment_monitoring_job: str,
    deployed_model_id: str,
    api_endpoint: str = "us-central1-aiplatform.googleapis.com",
):
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform_v1beta1.JobServiceClient(client_options=client_options)
    response = client.search_model_deployment_monitoring_stats_anomalies(
        model_deployment_monitoring_job=model_deployment_monitoring_job,
        deployed_model_id=deployed_model_id,
    )
    for model_monitoring_stats_anomalies in response:
        print("model_monitoring_stats_anomalies:", model_monitoring_stats_anomalies)


# [END aiplatform_v1beta1_search_model_deployment_monitoring_stats_anomalies_sample]
