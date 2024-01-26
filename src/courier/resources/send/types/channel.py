# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .channel_metadata import ChannelMetadata
from .override import Override
from .routing_method import RoutingMethod
from .timeouts import Timeouts

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Channel(pydantic.BaseModel):
    brand_id: typing.Optional[str] = pydantic.Field(
        description=(
            "Id of the brand that should be used for rendering the message.\n"
            "If not specified, the brand configured as default brand will be used.\n"
        )
    )
    providers: typing.Optional[typing.List[str]] = pydantic.Field(
        description=(
            "A list of providers enabled for this channel. Courier will select\n"
            "one provider to send through unless routing_method is set to all.\n"
        )
    )
    routing_method: typing.Optional[RoutingMethod] = pydantic.Field(
        description=(
            "The method for selecting the providers to send the message with.\n"
            "Single will send to one of the available providers for this channel,\n"
            "all will send the message through all channels. Defaults to `single`.\n"
        )
    )
    if_: typing.Optional[str] = pydantic.Field(
        alias="if",
        description=(
            "A JavaScript conditional expression to determine if the message should\n"
            "be sent through the channel. Has access to the data and profile object.\n"
            "For example, `data.name === profile.name`\n"
        ),
    )
    timeouts: typing.Optional[Timeouts]
    override: typing.Optional[Override] = pydantic.Field(description="Channel specific overrides.")
    metadata: typing.Optional[ChannelMetadata]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
