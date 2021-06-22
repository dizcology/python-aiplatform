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

# [START aiplatform_v1beta1_list_tensorboard_time_series_sample]
from google.cloud import aiplatform_v1beta1


def list_tensorboard_time_series_sample(
    project: str,
    tensorboard_id: str,
    experiment_id: str,
    run_id: str,
    location: str = "us-central1",
    api_endpoint: str = "us-central1-aiplatform.googleapis.com",
):
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform_v1beta1.TensorboardServiceClient(client_options=client_options)
    parent = client.tensorboard_run_path(
        project=project,
        location=location,
        tensorboard=tensorboard_id,
        experiment=experiment_id,
        run=run_id,
    )
    response = client.list_tensorboard_time_series(parent=parent)
    for tensorboard_time_series in response:
        print("tensorboard_time_series:", tensorboard_time_series)


# [END aiplatform_v1beta1_list_tensorboard_time_series_sample]
