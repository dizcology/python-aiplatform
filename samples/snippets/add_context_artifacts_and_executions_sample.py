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

# [START aiplatform_v1beta1_add_context_artifacts_and_executions_sample]
from google.cloud import aiplatform_v1beta1


def add_context_artifacts_and_executions_sample(
    context: str,
    artifact: str,
    project: str,
    metadata_store_id: str,
    execution_id: str,
    location: str = "us-central1",
    api_endpoint: str = "us-central1-aiplatform.googleapis.com",
):
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform_v1beta1.MetadataServiceClient(client_options=client_options)
    artifacts = [artifact]
    executions = [execution]
    execution = client.execution_path(
        project=project,
        location=location,
        metadata_store=metadata_store_id,
        execution=execution_id,
    )
    response = client.add_context_artifacts_and_executions(
        context=context, artifacts=artifacts, executions=executions
    )
    print("response:", response)


# [END aiplatform_v1beta1_add_context_artifacts_and_executions_sample]
