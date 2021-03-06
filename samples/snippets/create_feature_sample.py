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

# [START aiplatform_v1beta1_create_feature_sample]
from google.cloud import aiplatform_v1beta1


def create_feature_sample(
    project: str,
    featurestore_id: str,
    entity_type_id: str,
    description: str,
    location: str = "us-central1",
    api_endpoint: str = "us-central1-aiplatform.googleapis.com",
    timeout: int = 300,
):
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform_v1beta1.FeaturestoreServiceClient(client_options=client_options)
    feature = {"description": description}
    parent = client.entity_type_path(
        project=project,
        location=location,
        featurestore=featurestore_id,
        entity_type=entity_type_id,
    )
    response = client.create_feature(parent=parent, feature=feature)
    print("Long running operation:", response.operation.name)
    create_feature_response = response.result(timeout=timeout)
    print("create_feature_response:", create_feature_response)


# [END aiplatform_v1beta1_create_feature_sample]
