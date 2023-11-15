## Test file for helper functions in Producer.py

import unittest
from Producer import requirementsCheck


class Test(unittest.TestCase):
    def testRequirementsCheck(self):
        givenRequest = {
            "type": "delete",
            "requestId": "8df3eb63-344a-4a90-b8c3-757defb338fe",
            "widgetId": "dbe06de0-47e9-49d0-9505-ef2d50d6bf5c",
            "owner": "Mary Matthews"
        }
        givenInvalidRequest = {
            "type": "delete",
            "requestId": "8df3eb63-344a-4a90-b8c3-757defb338fe",
            "owner": "Mary Matthews"
        }
        self.assertTrue(requirementsCheck(givenRequest))
        self.assertFalse(requirementsCheck(givenInvalidRequest))









if __name__ == '__main__': 
    unittest.main() 