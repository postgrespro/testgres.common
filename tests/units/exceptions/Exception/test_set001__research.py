

class TestSet002__usage:
    def test_000__research(self):
        e = Exception("a\n1")
        assert str(e) == "a\n1"
        assert repr(e) == "Exception('a\\n1')"

        e = Exception("a\n1", 123)
        assert str(e) == "('a\\n1', 123)"
        assert repr(e) == "Exception('a\\n1', 123)"

    def test_001__str_and_repr__EEE_no_contrutor(self):
        class EEE(Exception):
            @property
            def message(self) -> str:
                return "EEE!\neee?"

        e = EEE("abc321\n123cba")
        assert isinstance(e, Exception)
        assert e.message == "EEE!\neee?"
        assert str(e) == "abc321\n123cba"
        # It a default implementation
        assert repr(e) == "EEE('abc321\\n123cba')"
        return

    def test_002__str_and_repr__EEE_with_default_constructor(self):
        class EEE(Exception):
            def __init__(self):
                super().__init__("zxc", "321")
                return

            @property
            def message(self) -> str:
                return "EEE!\neee?"

        e = EEE()
        assert isinstance(e, Exception)
        assert e.message == "EEE!\neee?"
        assert str(e) == "('zxc', '321')"
        # It a default implementation
        assert repr(e) == "EEE('zxc', '321')"
        return
