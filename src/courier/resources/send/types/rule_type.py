# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class RuleType(str, enum.Enum):
    SNOOZE = "snooze"
    CHANNEL_PREFERENCES = "channel_preferences"
    STATUS = "status"

    def visit(
        self,
        snooze: typing.Callable[[], T_Result],
        channel_preferences: typing.Callable[[], T_Result],
        status: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RuleType.SNOOZE:
            return snooze()
        if self is RuleType.CHANNEL_PREFERENCES:
            return channel_preferences()
        if self is RuleType.STATUS:
            return status()
