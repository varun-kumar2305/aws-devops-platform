import unittest
import json
from http.server import HTTPServer
from threading import Thread
from urllib.request import urlopen
from urllib.error import HTTPError

from app.main import AppHandler


class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("127.0.0.1", 0), AppHandler)
        cls.port = cls.server.server_address[1]

        cls.thread = Thread(
            target=cls.server.serve_forever,
            daemon=True
        )
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def test_home_endpoint(self):
        with urlopen(f"http://127.0.0.1:{self.port}/") as response:
            data = json.loads(response.read().decode())

            self.assertEqual(response.status, 200)
            self.assertEqual(
                data["message"],
                "AWS DevOps Platform is running!"
            )

    def test_health_endpoint(self):
        with urlopen(
            f"http://127.0.0.1:{self.port}/health"
        ) as response:
            data = json.loads(response.read().decode())

            self.assertEqual(response.status, 200)
            self.assertEqual(data["status"], "ok")

    def test_unknown_endpoint(self):
        with self.assertRaises(HTTPError) as error:
            urlopen(f"http://127.0.0.1:{self.port}/unknown")

        self.assertEqual(error.exception.code, 404)


if __name__ == "__main__":
    unittest.main()
