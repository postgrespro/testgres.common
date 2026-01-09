# coding: utf-8
import typing


class TestgresException(Exception):
    @property
    def message(self) -> str:
        assert isinstance(self, TestgresException)
        return str(self)

    @property
    def source(self) -> typing.Optional[str]:
        assert isinstance(self, TestgresException)
        return None


class InvalidOperationException(TestgresException):
    _message: str
    _source: typing.Optional[str]

    def __init__(self, message: str, source: typing.Optional[str] = None):
        assert type(message) == str  # noqa: E721
        assert source is None or type(source) == str  # noqa: E721
        super().__init__()
        self._message = message
        self._source = source
        return

    @property
    def message(self) -> str:
        assert type(self._message) == str  # noqa: E721
        return self._message

    @property
    def source(self) -> str:
        assert self._source is None or type(self._source) == str  # noqa: E721
        return self._source
