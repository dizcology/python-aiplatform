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

# [START aiplatform_v1beta1_create_training_pipeline_video_action_recognition_sample]
from google.cloud import aiplatform_v1beta1
from google.cloud.aiplatform.gapic.schema import trainingjob


def create_training_pipeline_video_action_recognition_sample(
    project: str,
    display_name: str,
    dataset_id: str,
    model_display_name: str,
    model_type: str,
    location: str = "us-central1",
    api_endpoint: str = "us-central1-aiplatform.googleapis.com",
):
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform_v1beta1.PipelineServiceClient(client_options=client_options)
    training_task_inputs = trainingjob.definition.AutoMlVideoActionRecognitionInputs(
        # modelType can be either 'CLOUD' or 'MOBILE_VERSATILE_1'
        model_type=model_type,
    ).to_value()

    training_pipeline = {
        "display_name": display_name,
        "training_task_definition": "gs://google-cloud-aiplatform/schema/trainingjob/definition/automl_video_action_recognition_1.0.0.yaml",
        "training_task_inputs": training_task_inputs,
        "input_data_config": {"dataset_id": dataset_id},
        "model_to_upload": {"display_name": model_display_name},
    }
    parent = f"projects/{project}/locations/{location}"
    response = client.create_training_pipeline(
        parent=parent, training_pipeline=training_pipeline
    )
    print("response:", response)


# [END aiplatform_v1beta1_create_training_pipeline_video_action_recognition_sample]
