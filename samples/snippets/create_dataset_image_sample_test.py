# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from uuid import uuid4

import pytest

import create_dataset_image_sample
import delete_dataset_sample
import helpers

PROJECT_ID = os.getenv("BUILD_SPECIFIC_GCLOUD_PROJECT")


@pytest.fixture(scope="function", autouse=True)
def teardown(shared_state):
    yield

    assert "/" in shared_state["dataset_name"]

    dataset_id = shared_state["dataset_name"].split("/")[-1]

    # Delete the created dataset
    delete_dataset_sample.delete_dataset_sample(
        project=PROJECT_ID, dataset_id=dataset_id
    )


def test_ucaip_generated_create_dataset_image(capsys, shared_state):
    create_dataset_image_sample.create_dataset_image_sample(
        display_name=f"temp_create_dataset_image_test_{uuid4()}", project=PROJECT_ID
    )
    out, _ = capsys.readouterr()
    assert "create_dataset_response" in out

    shared_state["dataset_name"] = helpers.get_name(out)
