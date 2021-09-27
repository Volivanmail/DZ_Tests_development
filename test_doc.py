from add import*
import mock
import builtins

class Test_secretary_program:

    def setup(self):
        print("method setup")

    def teardown(self):
        print("method teardown")

    def test_get_doc_owner_name(self):
        with mock.patch.object(builtins, 'input', lambda _: '10006'):
            assert get_doc_owner_name() == 'Аристарх Павлов'


    def test_delete_doc(self):
        with mock.patch.object(builtins, 'input', lambda _: '10006'):
            assert delete_doc() == ('10006', True)

    def test_add_new_shelf(self):
        with mock.patch.object(builtins, 'input', lambda _: '4'):
             assert add_new_shelf() == ('4', True)

    def test_add_new_shelf(self):
        with mock.patch.object(builtins, 'input', lambda _: '2'):
            assert add_new_shelf() == ('2', False)