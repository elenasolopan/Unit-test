import unittest
from Personal_Dates import search_name, find_shelf, get_list, add_new_shelf, move_shelves
import mock


class TestUnittest(unittest.TestCase):
    def setUp(self):
        print("Method setup")

    def test_search_name_true(self):
        self.assertEqual(search_name('2207 876234'), 'Василий Гупкин')
        self.assertEqual(search_name('11-2'), 'Геннадий Покемонов')

    def test_search_name_true_error(self):
        self.assertEqual(search_name('1'), "Error")

    def test_search_name_wrong(self):
        self.assertNotEqual(search_name('2207 876234'), "Аристарх Павлов")

    def test_search_name_wrong_error(self):
        self.assertNotEqual(search_name('2207 876234'), "Error")

    def test_find_shelf(self):
        self.assertEqual(find_shelf('2207 876234'), '1')
        self.assertEqual(find_shelf('11-2'), '1')
        self.assertEqual(find_shelf('10006'), '2')

    def test_find_shelf_wrong(self):
        self.assertEqual(find_shelf('100'), 'Error')

    def test_get_list(self):
        correct_output = f'passport "2207 876234" "Василий Гупкин"\ninvoice "11-2" "Геннадий Покемонов"\ninsurance ' \
                     f'"10006" "Аристарх Павлов"\n'
        self.assertEqual(get_list(), correct_output)

    @mock.patch('builtins.input', side_effect=['4'])
    def test_add_new_shelf(self, input):
        shelf, status = add_new_shelf()
        self.assertEqual(status, True)

    @mock.patch('builtins.input', side_effect=['1'])
    def test_add_new_shelf_wrong(self, input):
        shelf, status = add_new_shelf()
        self.assertEqual(status, False)

    @mock.patch('builtins.input', side_effect=['10006', '1'])
    def test_move_shelves(self, input):
        directories, status = move_shelves()
        self.assertEqual(status, True)

    @mock.patch('builtins.input', side_effect=['3333', '1'])
    def test_move_shelves_wrong_number(self, input):
        directories, status = move_shelves()
        self.assertEqual(status, False)

    @mock.patch('builtins.input', side_effect=['10006', '5'])
    def test_move_shelves_wrong_shelf(self, input):
        directories, status = move_shelves()
        self.assertEqual(status, False)

    def tearDown(self):
        print(f"Method tearDown\n")


if __name__ == '__main__':
    unittest.main()
