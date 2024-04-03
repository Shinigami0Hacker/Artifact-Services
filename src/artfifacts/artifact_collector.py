from src.utils.graphic import generate_table
from functools import wraps
import numpy as np
import asyncio
import aiohttp
import socket
import torch
from enum import Enum

class ProtocolType(Enum):
    """
    ProtocolType enum support 5 file of protocol: SINGLE_SOCKET, MULTI_SOCKET, HTTP_v1, HTTP_v2\
    and GOOGLE_DRIVE. Those will use as the standard in and output for validating type.
    """
    SINGLE_SOCKET = 0
    MULTI_SOCKET = 1
    HTTP_v1 = 2
    HTTP_v2 = 3
    GOOGLE_DRIVE = 4

class Scheduler():
    """
    Set how long the function cover by wrapper
    """
    EVERY_FUNCTION_CALL = 0
    EVERY_COLLECTOR_CALL = 1
    COLLECTER_BUILD = 2

class MetadataBuilder():
    def __init__(self, runtime_id) -> None:
        self.runtime_id = runtime_id
        self.__fileds = {}

    def add_field(self, field_name, value):
        assert (not self.__fileds.get(field_name, None)), ... 
        self.__fileds[field_name] = value

    def add_fields(self, form_fields: dict | zip):
        assert (isinstance(form_fields, zip) | isinstance(form_fields, dict)), ...
        form_fields = form_fields if isinstance(form_fields, zip) else form_fields.item()
        for field_name, value in form_fields :
            self.add_field(field_name, value)

    def build(self):
        return self
    
    def __build_validation(self):
        for field_name, value in self.____fileds:
            pass


class ProtocolConnection:
    @staticmethod
    def etalbish_single_socket_connection():
        pass

    @staticmethod
    def etalbish_multiple_socket_connection():
        pass
    
    @staticmethod
    def etalbish_http_v1_connection():
        pass

    @staticmethod
    def etalbish_http_v2_connection():
        pass

    @staticmethod
    def default_connection():
        pass

class ArtifactPayload:
    def __init__(self, payload: any, name: str, id: str, *, scheduler) -> None:
        self.id = id
        self.name = name
        self.__payload = payload
        self.temporary = []
        self.__serializer = None 

    @property.getter
    def get_payload(self):
        return self.__payload

    @property.getter
    def get_serialize_payload(self):
        serialize_data = self.__serializer.serialize(self.__payload)
        return serialize_data

    def __supported_payload_data_type(self):
        match self.__payload:
            case torch.Tensor:
                self.__serializer = None
                return True
            case _:
                return False

    def __str__(self) -> str:
        return f"ID:{self.id}\tName:{self.name}\tPayload_type{type(self.__payload)}"

class ArtifactColector:
    def __init__(self, host: str, port: str, *, protocol_type: ProtocolType) -> None:
        """
        The artifact collecter using the decoration method to cover the input and push it into the backend.\
        Support many protocol including multi-socket, metadata builder and lazy processing to construct the \
        data for performance.
        @params:
        + host:
        + port:
        + protocol_type (position required): 
        @returns:
        + Nonee
        """
        self.__host = host
        self.__port = port
        self.__payloads: list[ArtifactPayload] = {}
        self.__metadata: MetadataBuilder = []
        self.__cached = []
        self.__had_build = False
        self.conn = self.__etablish_connection(protocol_type=protocol_type)

    @property.getter
    def get_host(self):
        return self.__host
    
    @property.getter
    def get_port(self):
        return self.__port

    def artifact_summary(self):
        generate_table(self.__payloads)

    def add_artifact(self, id, name, *, scheduler: Scheduler):
        """
        The decorator using for capture the output of the function and append it into the collector.
        @params:
        - 
        @return:
        - None
        """
        payload = ArtifactPayload()
        @wraps
        def decorator():
            def wrapper(output):
                assert(isinstance(output))

    def push_by_id():
        pass

    def build_all(self):
        """
        Serialize all the data that in the 
        """
        self.__metadata.build()
        self.__had_build = True

    def push_all(self, push_all, reset):
        assert (self.__had_build), ...
        pass
        """

        """
        if reset:
            self.__clean_payload()
        pass

    def __check_id(self, id):
        assert isinstance(id, str), ...
        return id in [payload.id for payload in self.__payloads]

    def __etablish_connection(self, *, protocol_type):
        match (protocol_type):
            case ProtocolType.SINGLE_SOCKET:
                ProtocolConnection.etalbish_socket_connection(self.__host, self.__port)
            case ProtocolType.MULTI_SOCKET:
                ProtocolConnection.etalbish_single_socket_connection()
            case ProtocolType.HTTP_v1:
                ProtocolConnection.etalbish_http_v1_connection(self.__host, self.__port)
            case ProtocolType.HTTP_v2:
                ProtocolConnection.etalbish_http_v1_connection(self.__host, self.__port)
            case _:
                ProtocolConnection.default_connection(self.__host, self.__host)

    def __build_validation(self):
        pass

    def __clean_payload(self):
        pass