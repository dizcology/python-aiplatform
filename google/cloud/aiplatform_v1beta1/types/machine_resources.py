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


from google.cloud.aiplatform_v1beta1.types import (
    accelerator_type as gca_accelerator_type,
)


__protobuf__ = proto.module(
    package="google.cloud.aiplatform.v1beta1",
    manifest={
        "MachineSpec",
        "DedicatedResources",
        "AutomaticResources",
        "BatchDedicatedResources",
        "ResourcesConsumed",
    },
)


class MachineSpec(proto.Message):
    r"""Specification of a single machine.

    Attributes:
        machine_type (str):
            Immutable. The type of the machine. Following machine types
            are supported:

            -  ``n1-standard-2``

            -  ``n1-standard-4``

            -  ``n1-standard-8``

            -  ``n1-standard-16``

            -  ``n1-standard-32``

            -  ``n1-highmem-2``

            -  ``n1-highmem-4``

            -  ``n1-highmem-8``

            -  ``n1-highmem-16``

            -  ``n1-highmem-32``

            -  ``n1-highcpu-2``

            -  ``n1-highcpu-4``

            -  ``n1-highcpu-8``

            -  ``n1-highcpu-16``

            -  ``n1-highcpu-32``

            When used for [DeployedMode][] this field is optional and
            the default value is ``n1-standard-2``. If used for
            ``BatchPredictionJob``
            or as part of
            ``WorkerPoolSpec``
            this field is required.
        accelerator_type (~.gca_accelerator_type.AcceleratorType):
            Immutable. The type of accelerator(s) that may be attached
            to the machine as per
            ``accelerator_count``.
        accelerator_count (int):
            The number of accelerators to attach to the
            machine.
    """

    machine_type = proto.Field(proto.STRING, number=1)

    accelerator_type = proto.Field(
        proto.ENUM, number=2, enum=gca_accelerator_type.AcceleratorType,
    )

    accelerator_count = proto.Field(proto.INT32, number=3)


class DedicatedResources(proto.Message):
    r"""A description of resources that are dedicated to a
    DeployedModel, and that need a higher degree of manual
    configuration.

    Attributes:
        machine_spec (~.machine_resources.MachineSpec):
            Required. Immutable. The specification of a
            single machine used by the prediction.
        min_replica_count (int):
            Required. Immutable. The minimum number of machine replicas
            this DeployedModel will be always deployed on. If traffic
            against it increases, it may dynamically be deployed onto
            more replicas, and as traffic decreases, some of these extra
            replicas may be freed. Note: if
            ``machine_spec.accelerator_count``
            is above 0, currently the model will be always deployed
            precisely on
            ``min_replica_count``.
        max_replica_count (int):
            Immutable. The maximum number of replicas this DeployedModel
            may be deployed on when the traffic against it increases. If
            requested value is too large, the deployment will error, but
            if deployment succeeds then the ability to scale the model
            to that many replicas is guaranteed (barring service
            outages). If traffic against the DeployedModel increases
            beyond what its replicas at maximum may handle, a portion of
            the traffic will be dropped. If this value is not provided,
            will use
            ``min_replica_count``
            as the default value.
    """

    machine_spec = proto.Field(proto.MESSAGE, number=1, message=MachineSpec,)

    min_replica_count = proto.Field(proto.INT32, number=2)

    max_replica_count = proto.Field(proto.INT32, number=3)


class AutomaticResources(proto.Message):
    r"""A description of resources that to large degree are decided
    by AI Platform, and require only a modest additional
    configuration. Each Model supporting these resources documents
    its specific guidelines.

    Attributes:
        min_replica_count (int):
            Immutable. The minimum number of replicas this DeployedModel
            will be always deployed on. If traffic against it increases,
            it may dynamically be deployed onto more replicas up to
            ``max_replica_count``,
            and as traffic decreases, some of these extra replicas may
            be freed. If requested value is too large, the deployment
            will error.
        max_replica_count (int):
            Immutable. The maximum number of replicas
            this DeployedModel may be deployed on when the
            traffic against it increases. If requested value
            is too large, the deployment will error, but if
            deployment succeeds then the ability to scale
            the model to that many replicas is guaranteed
            (barring service outages). If traffic against
            the DeployedModel increases beyond what its
            replicas at maximum may handle, a portion of the
            traffic will be dropped. If this value is not
            provided, a no upper bound for scaling under
            heavy traffic will be assume, though AI Platform
            may be unable to scale beyond certain replica
            number.
    """

    min_replica_count = proto.Field(proto.INT32, number=1)

    max_replica_count = proto.Field(proto.INT32, number=2)


class BatchDedicatedResources(proto.Message):
    r"""A description of resources that are used for performing batch
    operations, are dedicated to a Model, and need manual
    configuration.

    Attributes:
        machine_spec (~.machine_resources.MachineSpec):
            Required. Immutable. The specification of a
            single machine.
        starting_replica_count (int):
            Immutable. The number of machine replicas used at the start
            of the batch operation. If not set, AI Platform decides
            starting number, not greater than
            ``max_replica_count``
        max_replica_count (int):
            Immutable. The maximum number of machine
            replicas the batch operation may be scaled to.
            The default value is 10.
    """

    machine_spec = proto.Field(proto.MESSAGE, number=1, message=MachineSpec,)

    starting_replica_count = proto.Field(proto.INT32, number=2)

    max_replica_count = proto.Field(proto.INT32, number=3)


class ResourcesConsumed(proto.Message):
    r"""Statistics information about resource consumption.

    Attributes:
        replica_hours (float):
            Output only. The number of replica hours
            used. Note that many replicas may run in
            parallel, and additionally any given work may be
            queued for some time. Therefore this value is
            not strictly related to wall time.
    """

    replica_hours = proto.Field(proto.DOUBLE, number=1)


__all__ = tuple(sorted(__protobuf__.manifest))
