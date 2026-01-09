from src.exceptions import InvalidOperationException


class TestSet001_Constructor:
    def test_001_positional_args_001__message(self):
        e = InvalidOperationException("abcdef\n12345")
        assert e.message == "abcdef\n12345"
        assert e.source is None
        assert str(e) == "abcdef\n12345"
        assert repr(e) == "InvalidOperationException('abcdef\\n12345', None)"
        return

    def test_001_positional_args_002__message_source(self):
        e = InvalidOperationException("abcdef\n54321", "mysource\n1")
        assert e.message == "abcdef\n54321"
        assert e.source == "mysource\n1"
        assert str(e) == "abcdef\n54321"
        assert repr(e) == "InvalidOperationException('abcdef\\n54321', 'mysource\\n1')"
        return

    def test_002_named_args_001__source_message(self):
        e = InvalidOperationException(source="s", message="m")
        assert e.message == "m"
        assert e.source == "s"
        assert str(e) == "m"
        assert repr(e) == "InvalidOperationException('m', 's')"
        return
