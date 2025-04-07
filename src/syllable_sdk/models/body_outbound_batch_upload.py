"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import io
import pydantic
from syllable_sdk.types import BaseModel
from syllable_sdk.utils import FieldMetadata, MultipartFormMetadata
from typing import IO, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class FileTypedDict(TypedDict):
    file_name: str
    content: Union[bytes, IO[bytes], io.BufferedReader]
    content_type: NotRequired[str]


class File(BaseModel):
    file_name: Annotated[
        str, pydantic.Field(alias="fileName"), FieldMetadata(multipart=True)
    ]

    content: Annotated[
        Union[bytes, IO[bytes], io.BufferedReader],
        pydantic.Field(alias=""),
        FieldMetadata(multipart=MultipartFormMetadata(content=True)),
    ]

    content_type: Annotated[
        Optional[str],
        pydantic.Field(alias="Content-Type"),
        FieldMetadata(multipart=True),
    ] = None


class BodyOutboundBatchUploadTypedDict(TypedDict):
    file: NotRequired[FileTypedDict]


class BodyOutboundBatchUpload(BaseModel):
    file: Annotated[
        Optional[File], FieldMetadata(multipart=MultipartFormMetadata(file=True))
    ] = None
