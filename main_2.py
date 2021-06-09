import unittest
from Personal_Dates import add_new_document, del_number_doc
import mock


class TestUnittest(unittest.TestCase):
    def setUp(self):
        print("Method setup")

    @mock.patch('builtins.input', side_effect=['Паспорт', '0000', 'Василий Васильевич', '2'])
    def test_add_new_document(self, input):
        directories, documents, status = add_new_document()
        self.assertEqual(status, True)

    @mock.patch('builtins.input', side_effect=['Паспорт', '1111', 'Николай Николаевич', '8'])
    def test_add_new_document_wrong(self, input):
        directories, documents, status = add_new_document()
        self.assertEqual(status, False)

    @mock.patch('builtins.input', side_effect=['10006'])
    def test_del_number_doc(self, input):
        documents, directories, status = del_number_doc()
        self.assertEqual(status, True)

    @mock.patch('builtins.input', side_effect=['8888'])
    def test_del_number_doc_wrong(self, input):
        documents, directories, status = del_number_doc()
        self.assertEqual(status, False)

    def tearDown(self):
        print(f"Method tearDown\n")


if __name__ == '__main__':
    unittest.main()
