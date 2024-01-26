# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .tenant import Tenant

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TenantListResponse(pydantic.BaseModel):
    cursor: typing.Optional[str] = pydantic.Field(
        description="A pointer to the next page of results. Defined only whenhas_more is set to true."
    )
    has_more: bool = pydantic.Field(description="Set to true when there are more pages that can be retrieved.")
    items: typing.List[Tenant] = pydantic.Field(description="An array of Tenants")
    next_url: typing.Optional[str] = pydantic.Field(
        description=(
            "A url that may be used to generate fetch the next set of results.\n"
            "Defined only whenhas_more is set to true\n"
        )
    )
    url: str = pydantic.Field(description="A url that may be used to generate these results.")
    type: typing_extensions.Literal["list"] = pydantic.Field(
        description='Always set to "list". Represents the type of this object.'
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
