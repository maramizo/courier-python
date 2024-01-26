# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class SubscriptionTopicStatus(str, enum.Enum):
    OPTED_OUT = "OPTED_OUT"
    OPTED_IN = "OPTED_IN"
    REQUIRED = "REQUIRED"

    def visit(
        self,
        opted_out: typing.Callable[[], T_Result],
        opted_in: typing.Callable[[], T_Result],
        required: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SubscriptionTopicStatus.OPTED_OUT:
            return opted_out()
        if self is SubscriptionTopicStatus.OPTED_IN:
            return opted_in()
        if self is SubscriptionTopicStatus.REQUIRED:
            return required()
