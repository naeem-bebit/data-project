import unittest
from src.app import index
from src.app import app


class unit_test(unittest.TestCase):
    def test_index(self):
        response = app.test_client().get("/")
        assert response.status_code == 200
        assert response.data == b"Hello, World!"


if __name__ == "__main__":
    pass
