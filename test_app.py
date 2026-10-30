import unittest
from app import welcome

class TestApp(unittest.TestCase):

    def test_welcome(self):
        self.assertEqual(welcome(), "Welcome to DevOps CI/CD Pipeline!")

if __name__ == "__main__":
    unittest.main()
