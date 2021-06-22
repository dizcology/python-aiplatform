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

# [START aiplatform_v1beta1_create_data_labeling_job_active_learning_sample]
from google.cloud import aiplatform_v1beta1
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value


def create_data_labeling_job_active_learning_sample(
    project: str,
    display_name: str,
    dataset: str,
    instruction_uri: str,
    inputs_schema_uri: str,
    annotation_spec: str,
    location: str = "us-central1",
    api_endpoint: str = "us-central1-aiplatform.googleapis.com",
):
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform_v1beta1.JobServiceClient(client_options=client_options)
    inputs_dict = {"annotation_specs": [annotation_spec]}
    inputs = json_format.ParseDict(inputs_dict, Value())

    active_learning_config = {"max_data_item_count": 1}

    data_labeling_job = {
        "display_name": display_name,
        # Full resource name: projects/{project}/locations/{location}/datasets/{dataset_id}
        "datasets": [dataset],
        "labeler_count": 1,
        "instruction_uri": instruction_uri,
        "inputs_schema_uri": inputs_schema_uri,
        "inputs": inputs,
        "annotation_labels": {
            "aiplatform.googleapis.com/annotation_set_name": "data_labeling_job_active_learning"
        },
        "active_learning_config": active_learning_config,
    }
    parent = f"projects/{project}/locations/{location}"
    response = client.create_data_labeling_job(
        parent=parent, data_labeling_job=data_labeling_job
    )
    print("response:", response)


# [END aiplatform_v1beta1_create_data_labeling_job_active_learning_sample]
