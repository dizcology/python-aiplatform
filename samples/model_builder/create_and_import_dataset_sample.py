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

# [START aiplatform_model_builder_create_and_import_dataset_sample]
from google.cloud import aiplatform


def create_and_import_dataset_sample(
    project: str, gcs_csv_uri: str, display_name: str, location: str = "us-central1"
):
    aiplatform.init(project=project, location=location)

    dataset = aiplatform.Dataset.create(
        display_name=display_name,
        metadata_schema_uri=aiplatform.schema.dataset.metadata.image,
        gcs_source=[gcs_csv_uri],
        import_schema_uri="what is this?",
    )

    print(dataset)


# [END aiplatform_model_builder_create_and_import_dataset_sample]
