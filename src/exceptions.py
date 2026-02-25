# coding: utf-8
import typing


class TestgresException(Exception):
    @property
    def message(self) -> str:
        assert isinstance(self, TestgresException)
        r = super().__str__()
        assert r is not None
        assert type(r) is str
        return r

    @property
    def source(self) -> typing.Optional[str]:
        assert isinstance(self, TestgresException)
        return None

    def __str__(self) -> str:
        r = self.message
        assert type(r) is str
        return r


class InvalidOperationException(TestgresException):
    _message: str
    _source: typing.Optional[str]

    def __init__(self, message: str, source: typing.Optional[str] = None):
        assert type(message) is str
        assert source is None or type(source) is str
        super().__init__()
        self._message = message
        self._source = source
        return

    @property
    def message(self) -> str:
        assert type(self._message) is str
        return self._message

    @property
    def source(self) -> str:
        assert self._source is None or type(self._source) is str
        return self._source

    def __repr__(self) -> str:
        # It must be overrided!
        assert type(self) == InvalidOperationException  # noqa: E721
        r = "{}({}, {})".format(
            __class__.__name__,
            repr(self._message),
            repr(self._source),
        )
        assert type(r) is str
        return r
