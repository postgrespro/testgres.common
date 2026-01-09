from src.exceptions import InvalidOperationException


class TestSet001_Constructor:
    def test_000_positional_args_001__message(self):
        e = InvalidOperationException("abcdef")
        assert e.message == "abcdef"
        assert e.source is None
        return

    def test_000_positional_args_002__message_source(self):
        e = InvalidOperationException("abc123", "mysource")
        assert e.message == "abc123"
        assert e.source == "mysource"
        return

    def test_001_named_args_001__source_message(self):
        e = InvalidOperationException(source="s", message="m")
        assert e.message == "m"
        assert e.source == "s"
        return
