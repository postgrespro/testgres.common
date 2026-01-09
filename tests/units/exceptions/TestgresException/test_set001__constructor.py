from src.exceptions import TestgresException as testgres__TestgresException


class TestSet001_Constructor:
    def test_000_positional_args_001__arg1(self):
        e = testgres__TestgresException("abcdef")
        assert e.message == "abcdef"
        assert e.source is None
        return

    def test_000_positional_args_002__arg1_arg2(self):
        e = testgres__TestgresException("abc123", "mysource")
        assert e.message == "('abc123', 'mysource')"
        assert e.source is None
        return
