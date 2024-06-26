# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from .brand_settings import BrandSettings
from .brand_snippets import BrandSnippets


class Brand(pydantic_v1.BaseModel):
    created: int = pydantic_v1.Field()
    """
    The date/time of when the brand was created. Represented in milliseconds since Unix epoch.
    """

    id: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Brand Identifier
    """

    name: str = pydantic_v1.Field()
    """
    Brand name
    """

    published: int = pydantic_v1.Field()
    """
    The date/time of when the brand was published. Represented in milliseconds since Unix epoch.
    """

    settings: BrandSettings
    updated: int = pydantic_v1.Field()
    """
    The date/time of when the brand was updated. Represented in milliseconds since Unix epoch.
    """

    snippets: typing.Optional[BrandSnippets] = None
    version: str = pydantic_v1.Field()
    """
    The version identifier for the brand
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
