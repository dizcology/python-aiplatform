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


from unittest.mock import patch

import create_and_import_dataset_sample


def test_create_and_import_dataset_sample(
    mock_create_dataset, mock_get_dataset, mock_import_data
):
    create_and_import_dataset_sample.create_and_import_dataset_sample(
        project="abc", gcs_csv_uri="123", display_name="test_dn"
    )

    mock_create_dataset.assert_called_once()
    mock_get_dataset.assert_called_once()
    mock_import_data.assert_called_once()
