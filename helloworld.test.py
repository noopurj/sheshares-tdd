import unittest

from helloworld import hello_world


class TestHelloWorld(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(hello_world("world"), "Hello world!")

    def test_hello_world_name(self):
        self.assertEqual(hello_world("Lucy"), "Hello Lucy!")


if __name__ == '__main__':
    unittest.main()