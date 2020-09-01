import unittest
import json

from app import app
from config import basedir, TestingConfig

class FlaskApiTest(unittest.TestCase):
    
    ############################
    #### setup and teardown ####
    ############################
    
    # executed prior to each test
    def setUp(self):
        app.config.from_object(TestingConfig)
        self.app = app.test_client()
        self.number_list = [1, 2, 3]
        self.empty_number_list = []

    # executed after each test
    def tearDown(self):
        pass

    ########################
    #### helper methods ####
    ########################

    ###############
    #### tests ####
    ###############

    def test_index_route(self):
        """
        Test index route returns a successful response
        """
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # def test_sum_list_returns_error_message_if_empty(self):
    #     """
    #     Test sum_list route returns an error message if the provided list is empty
    #     """
    #     response = self.app.get('/total')
    #     self.assertIn(b'List provided is empty', response.data)
    #     print(response.data)

    def test_sum_list_returns_correct_format(self):
        """
        Test sum_list route returns correct format in key value pair
        total: sum
        """
        response = self.app.get('/total')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'total', response.data)
        data = json.loads(response.get_data(as_text=True))

    def test_sum_list_returns_correct_result(self):
        """
        Test sum_list route returns correct result once list has been totalled
        """
        response = self.app.get('/total')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(int(data['total']), 50000005000000)
 
 
if __name__ == "__main__":
    unittest.main()