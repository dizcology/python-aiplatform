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

# [START aiplatform_v1beta1_search_migratable_resources_sample]
from google.cloud import aiplatform_v1beta1


def search_migratable_resources_sample(
    parent: str, api_endpoint: str = "us-central1-aiplatform.googleapis.com"
):
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform_v1beta1.MigrationServiceClient(client_options=client_options)
    response = client.search_migratable_resources(parent=parent)
    for migratable_resource in response:
        print("migratable_resource:", migratable_resource)


# [END aiplatform_v1beta1_search_migratable_resources_sample]
