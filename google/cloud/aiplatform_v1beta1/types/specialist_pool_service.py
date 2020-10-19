# -*- coding: utf-8 -*-

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
#

import proto  # type: ignore


from google.cloud.aiplatform_v1beta1.types import operation
from google.cloud.aiplatform_v1beta1.types import specialist_pool as gca_specialist_pool
from google.protobuf import field_mask_pb2 as field_mask  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.aiplatform.v1beta1',
    manifest={
        'CreateSpecialistPoolRequest',
        'CreateSpecialistPoolOperationMetadata',
        'GetSpecialistPoolRequest',
        'ListSpecialistPoolsRequest',
        'ListSpecialistPoolsResponse',
        'DeleteSpecialistPoolRequest',
        'UpdateSpecialistPoolRequest',
        'UpdateSpecialistPoolOperationMetadata',
    },
)


class CreateSpecialistPoolRequest(proto.Message):
    r"""Request message for
    ``SpecialistPoolService.CreateSpecialistPool``.

    Attributes:
        parent (str):
            Required. The parent Project name for the new
            SpecialistPool. The form is
            ``projects/{project}/locations/{location}``.
        specialist_pool (~.gca_specialist_pool.SpecialistPool):
            Required. The SpecialistPool to create.
    """

    parent = proto.Field(proto.STRING, number=1)

    specialist_pool = proto.Field(proto.MESSAGE, number=2,
        message=gca_specialist_pool.SpecialistPool,
    )


class CreateSpecialistPoolOperationMetadata(proto.Message):
    r"""Runtime operation information for
    ``SpecialistPoolService.CreateSpecialistPool``.

    Attributes:
        generic_metadata (~.operation.GenericOperationMetadata):
            The operation generic information.
    """

    generic_metadata = proto.Field(proto.MESSAGE, number=1,
        message=operation.GenericOperationMetadata,
    )


class GetSpecialistPoolRequest(proto.Message):
    r"""Request message for
    ``SpecialistPoolService.GetSpecialistPool``.

    Attributes:
        name (str):
            Required. The name of the SpecialistPool resource. The form
            is

            ``projects/{project}/locations/{location}/specialistPools/{specialist_pool}``.
    """

    name = proto.Field(proto.STRING, number=1)


class ListSpecialistPoolsRequest(proto.Message):
    r"""Request message for
    ``SpecialistPoolService.ListSpecialistPools``.

    Attributes:
        parent (str):
            Required. The name of the SpecialistPool's parent resource.
            Format: ``projects/{project}/locations/{location}``
        page_size (int):
            The standard list page size.
        page_token (str):
            The standard list page token. Typically obtained by
            ``ListSpecialistPoolsResponse.next_page_token``
            of the previous
            ``SpecialistPoolService.ListSpecialistPools``
            call. Return first page if empty.
        read_mask (~.field_mask.FieldMask):
            Mask specifying which fields to read.
            FieldMask represents a set of
    """

    parent = proto.Field(proto.STRING, number=1)

    page_size = proto.Field(proto.INT32, number=2)

    page_token = proto.Field(proto.STRING, number=3)

    read_mask = proto.Field(proto.MESSAGE, number=4,
        message=field_mask.FieldMask,
    )


class ListSpecialistPoolsResponse(proto.Message):
    r"""Response message for
    ``SpecialistPoolService.ListSpecialistPools``.

    Attributes:
        specialist_pools (Sequence[~.gca_specialist_pool.SpecialistPool]):
            A list of SpecialistPools that matches the
            specified filter in the request.
        next_page_token (str):
            The standard List next-page token.
    """

    @property
    def raw_page(self):
        return self

    specialist_pools = proto.RepeatedField(proto.MESSAGE, number=1,
        message=gca_specialist_pool.SpecialistPool,
    )

    next_page_token = proto.Field(proto.STRING, number=2)


class DeleteSpecialistPoolRequest(proto.Message):
    r"""Request message for
    ``SpecialistPoolService.DeleteSpecialistPool``.

    Attributes:
        name (str):
            Required. The resource name of the SpecialistPool to delete.
            Format:
            ``projects/{project}/locations/{location}/specialistPools/{specialist_pool}``
        force (bool):
            If set to true, any specialist managers in
            this SpecialistPool will also be deleted.
            (Otherwise, the request will only work if the
            SpecialistPool has no specialist managers.)
    """

    name = proto.Field(proto.STRING, number=1)

    force = proto.Field(proto.BOOL, number=2)


class UpdateSpecialistPoolRequest(proto.Message):
    r"""Request message for
    ``SpecialistPoolService.UpdateSpecialistPool``.

    Attributes:
        specialist_pool (~.gca_specialist_pool.SpecialistPool):
            Required. The SpecialistPool which replaces
            the resource on the server.
        update_mask (~.field_mask.FieldMask):
            Required. The update mask applies to the
            resource.
    """

    specialist_pool = proto.Field(proto.MESSAGE, number=1,
        message=gca_specialist_pool.SpecialistPool,
    )

    update_mask = proto.Field(proto.MESSAGE, number=2,
        message=field_mask.FieldMask,
    )


class UpdateSpecialistPoolOperationMetadata(proto.Message):
    r"""Runtime operation metadata for
    ``SpecialistPoolService.UpdateSpecialistPool``.

    Attributes:
        specialist_pool (str):
            Output only. The name of the SpecialistPool to which the
            specialists are being added. Format:

            ``projects/{project_id}/locations/{location_id}/specialistPools/{specialist_pool}``
        generic_metadata (~.operation.GenericOperationMetadata):
            The operation generic information.
    """

    specialist_pool = proto.Field(proto.STRING, number=1)

    generic_metadata = proto.Field(proto.MESSAGE, number=2,
        message=operation.GenericOperationMetadata,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
