from decimal import Decimal
from typing import Literal

from fluent_compiler.types import FluentType
from typing_extensions import TypeAlias

PossibleValue: TypeAlias = str | int | float | Decimal | bool | FluentType

class TranslatorRunner:
    def get(self, path: str, **kwargs: PossibleValue) -> str: ...
    hello: Hello
    button: Button
    no: No

class Hello:
    @staticmethod
    def user(*, username: PossibleValue) -> Literal["""Hello { $username }. Click on the button"""]: ...

class Button:
    @staticmethod
    def button() -> Literal["""Button"""]: ...
    @staticmethod
    def pressed() -> Literal["""You pressed the button"""]: ...

class No:
    @staticmethod
    def copy() -> Literal["""This type of update is not supported by the send_copy method"""]: ...
