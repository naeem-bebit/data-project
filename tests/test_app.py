import unittest
from src.app import index


class unit_test(unittest.TestCase):
    def test_index(self):
        assert index() == "Hello, world!"


if __name__ == "__main__":
    pass
