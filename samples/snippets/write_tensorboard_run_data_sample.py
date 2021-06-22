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

# [START aiplatform_v1beta1_write_tensorboard_run_data_sample]
from google.cloud import aiplatform_v1beta1


def write_tensorboard_run_data_sample(
    tensorboard_run: str,
    tensorboard_time_series_id: str,
    api_endpoint: str = "us-central1-aiplatform.googleapis.com",
):
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform_v1beta1.TensorboardServiceClient(client_options=client_options)
    time_series_data = [{"tensorboard_time_series_id": tensorboard_time_series_id}]
    response = client.write_tensorboard_run_data(
        tensorboard_run=tensorboard_run, time_series_data=time_series_data
    )
    print("response:", response)


# [END aiplatform_v1beta1_write_tensorboard_run_data_sample]
