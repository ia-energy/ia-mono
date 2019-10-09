import unittest
import unittest
from unittest.mock import patch
from app.apis.test_api import TestMessage as TestMgsAPI
from app.model.test_message import TestMessage

import app.apis.test_api as api
from app.services.auth_0_manager import AuthError

class GetTest(unittest.TestCase):

    @patch('app.services.auth_0_manager.validAuth', return_value=False)
    def test_auth_required(self, validAuth):
        test_mgs_api = TestMgsAPI()
        with self.assertRaises(Exception) as context:
            test_mgs_api.get("test_uuid")
        self.assertTrue("({'code': 'invalid_header', 'description': 'Unable to find appropriate key'}, 401)" in str(context.exception))

    test_message = TestMessage()
    test_message.id = "private_db_id"
    test_message.uuid = "test_uuid"
    test_message.value = "Some value"

    @patch('app.services.test_message_db_srvc.get_a_message', return_value=test_message)
    @patch('app.services.auth_0_manager.validAuth', return_value=True)
    def test_removes_private_id(self, get_a_message, validAuth):
        #get_a_message.return_value = test_message
        #validAuth.return_value = False
        test_mgs_api = TestMgsAPI()
        self.assertFalse("private_db_id" in str(test_mgs_api.get("uuid")))

if __name__ == '__main__':
        unittest.main()
