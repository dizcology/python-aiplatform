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

# [START aiplatform_v1beta1_batch_migrate_resources_sample]
from google.cloud import aiplatform_v1beta1


def batch_migrate_resources_sample(
    parent: str,
    migrate_resource_requests: typing.Sequence[
        google.cloud.aiplatform_v1beta1.types.migration_service.MigrateResourceRequest
    ],
    api_endpoint: str = "us-central1-aiplatform.googleapis.com",
    timeout: int = 300,
):
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform_v1beta1.MigrationServiceClient(client_options=client_options)
    response = client.batch_migrate_resources(
        parent=parent, migrate_resource_requests=migrate_resource_requests
    )
    print("Long running operation:", response.operation.name)
    batch_migrate_resources_response = response.result(timeout=timeout)
    print("batch_migrate_resources_response:", batch_migrate_resources_response)


# [END aiplatform_v1beta1_batch_migrate_resources_sample]
