# This file was auto-generated by Fern from our API Definition.

import typing

from .routing_strategy_channel import RoutingStrategyChannel
from .routing_strategy_provider import RoutingStrategyProvider

RoutingChannel = typing.Union[RoutingStrategyChannel, RoutingStrategyProvider, str]
