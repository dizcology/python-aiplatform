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

from typing import Callable, Dict

from google.api_core import grpc_helpers   # type: ignore
from google.api_core import operations_v1  # type: ignore
from google.auth import credentials        # type: ignore

import grpc  # type: ignore

from google.cloud.aiplatform_v1beta1.types import specialist_pool
from google.cloud.aiplatform_v1beta1.types import specialist_pool_service
from google.longrunning import operations_pb2 as operations  # type: ignore

from .base import SpecialistPoolServiceTransport


class SpecialistPoolServiceGrpcTransport(SpecialistPoolServiceTransport):
    """gRPC backend transport for SpecialistPoolService.

    A service for creating and managing Customer SpecialistPools.
    When customers start Data Labeling jobs, they can reuse/create
    Specialist Pools to bring their own Specialists to label the
    data. Customers can add/remove Managers for the Specialist Pool
    on Cloud console, then Managers will get email notifications to
    manage Specialists and tasks on CrowdCompute console.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """
    def __init__(self, *,
            host: str = 'aiplatform.googleapis.com',
            credentials: credentials.Credentials = None,
            channel: grpc.Channel = None) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
        """
        # Sanity check: Ensure that channel and credentials are not both
        # provided.
        if channel:
            credentials = False

        # Run the base constructor.
        super().__init__(host=host, credentials=credentials)
        self._stubs = {}  # type: Dict[str, Callable]

        # If a channel was explicitly provided, set it.
        if channel:
            self._grpc_channel = channel

    @classmethod
    def create_channel(cls,
                       host: str = 'aiplatform.googleapis.com',
                       credentials: credentials.Credentials = None,
                       **kwargs) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            address (Optionsl[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            scopes=cls.AUTH_SCOPES,
            **kwargs
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Sanity check: Only create a new channel if we do not already
        # have one.
        if not hasattr(self, '_grpc_channel'):
            self._grpc_channel = self.create_channel(
                self._host,
                credentials=self._credentials,
            )

        # Return the channel from cache.
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Sanity check: Only create a new client if we do not already have one.
        if 'operations_client' not in self.__dict__:
            self.__dict__['operations_client'] = operations_v1.OperationsClient(
                self.grpc_channel
            )

        # Return the client from cache.
        return self.__dict__['operations_client']

    @property
    def create_specialist_pool(self) -> Callable[
            [specialist_pool_service.CreateSpecialistPoolRequest],
            operations.Operation]:
        r"""Return a callable for the create specialist pool method over gRPC.

        Creates a SpecialistPool.

        Returns:
            Callable[[~.CreateSpecialistPoolRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_specialist_pool' not in self._stubs:
            self._stubs['create_specialist_pool'] = self.grpc_channel.unary_unary(
                '/google.cloud.aiplatform.v1beta1.SpecialistPoolService/CreateSpecialistPool',
                request_serializer=specialist_pool_service.CreateSpecialistPoolRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs['create_specialist_pool']

    @property
    def get_specialist_pool(self) -> Callable[
            [specialist_pool_service.GetSpecialistPoolRequest],
            specialist_pool.SpecialistPool]:
        r"""Return a callable for the get specialist pool method over gRPC.

        Gets a SpecialistPool.

        Returns:
            Callable[[~.GetSpecialistPoolRequest],
                    ~.SpecialistPool]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_specialist_pool' not in self._stubs:
            self._stubs['get_specialist_pool'] = self.grpc_channel.unary_unary(
                '/google.cloud.aiplatform.v1beta1.SpecialistPoolService/GetSpecialistPool',
                request_serializer=specialist_pool_service.GetSpecialistPoolRequest.serialize,
                response_deserializer=specialist_pool.SpecialistPool.deserialize,
            )
        return self._stubs['get_specialist_pool']

    @property
    def list_specialist_pools(self) -> Callable[
            [specialist_pool_service.ListSpecialistPoolsRequest],
            specialist_pool_service.ListSpecialistPoolsResponse]:
        r"""Return a callable for the list specialist pools method over gRPC.

        Lists SpecialistPools in a Location.

        Returns:
            Callable[[~.ListSpecialistPoolsRequest],
                    ~.ListSpecialistPoolsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_specialist_pools' not in self._stubs:
            self._stubs['list_specialist_pools'] = self.grpc_channel.unary_unary(
                '/google.cloud.aiplatform.v1beta1.SpecialistPoolService/ListSpecialistPools',
                request_serializer=specialist_pool_service.ListSpecialistPoolsRequest.serialize,
                response_deserializer=specialist_pool_service.ListSpecialistPoolsResponse.deserialize,
            )
        return self._stubs['list_specialist_pools']

    @property
    def delete_specialist_pool(self) -> Callable[
            [specialist_pool_service.DeleteSpecialistPoolRequest],
            operations.Operation]:
        r"""Return a callable for the delete specialist pool method over gRPC.

        Deletes a SpecialistPool as well as all Specialists
        in the pool.

        Returns:
            Callable[[~.DeleteSpecialistPoolRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'delete_specialist_pool' not in self._stubs:
            self._stubs['delete_specialist_pool'] = self.grpc_channel.unary_unary(
                '/google.cloud.aiplatform.v1beta1.SpecialistPoolService/DeleteSpecialistPool',
                request_serializer=specialist_pool_service.DeleteSpecialistPoolRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs['delete_specialist_pool']

    @property
    def update_specialist_pool(self) -> Callable[
            [specialist_pool_service.UpdateSpecialistPoolRequest],
            operations.Operation]:
        r"""Return a callable for the update specialist pool method over gRPC.

        Updates a SpecialistPool.

        Returns:
            Callable[[~.UpdateSpecialistPoolRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'update_specialist_pool' not in self._stubs:
            self._stubs['update_specialist_pool'] = self.grpc_channel.unary_unary(
                '/google.cloud.aiplatform.v1beta1.SpecialistPoolService/UpdateSpecialistPool',
                request_serializer=specialist_pool_service.UpdateSpecialistPoolRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs['update_specialist_pool']


__all__ = (
    'SpecialistPoolServiceGrpcTransport',
)
