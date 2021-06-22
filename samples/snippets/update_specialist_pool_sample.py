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

# [START aiplatform_v1beta1_update_specialist_pool_sample]
from google.cloud import aiplatform_v1beta1


def update_specialist_pool_sample(
    specialist_pool_name: str,
    new_display_name: str,
    api_endpoint: str = "us-central1-aiplatform.googleapis.com",
    timeout: int = 300,
):
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform_v1beta1.SpecialistPoolServiceClient(
        client_options=client_options
    )
    specialist_pool = {
        "name": specialist_pool_name,
        "display_name": new_display_name,
    }
    update_mask = {"paths": ["display_name"]}
    response = client.update_specialist_pool(
        specialist_pool=specialist_pool, update_mask=update_mask
    )
    print("Long running operation:", response.operation.name)
    update_specialist_pool_response = response.result(timeout=timeout)
    print("update_specialist_pool_response:", update_specialist_pool_response)


# [END aiplatform_v1beta1_update_specialist_pool_sample]
