import unittest
from add_folder_Ya import add_folder


class TestAddFolder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("method setUpClass")

    def setUp(self):
        print("method setUp")

    def test_add_folder(self):
        self.assert_(add_folder('Hello World'), 201)

    def tearDown(self):
        print("method tearDown")

    @classmethod
    def tearDownClass(cls):
        # Здесь, наверное, правильно было бы выполнить удаление папки
        print("method tearDownClass")

if __name__ == '__main__':
    unittest.main()