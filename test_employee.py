import unittest
from employee import Employee
from unittest.mock import patch
import requests

class TestEmployee(unittest.TestCase):

    def setup(self):
        self.emp_1 = Employee("Corey", "Schafer", 50000)
        self.emp_2 = Employee("Sue", "Smith", 60000)

    def test_month_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"
            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_call_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, "Success")
