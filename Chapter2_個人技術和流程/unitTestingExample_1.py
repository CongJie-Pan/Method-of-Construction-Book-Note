import unittest
from user import User  # Import the User class from user module

class UserTests(unittest.TestCase):
    def test_constructor(self):
        """
        Test for User constructor with email parameter
        
        This test verifies that:
        1. A User object can be created with an email address
        2. The created object is valid and not None
        3. The email property is correctly set
        """
        # Setup - prepare test data (a sample email address)
        user_email = "someone@example.com"
        
        # Exercise - use the functionality of the class being tested (create a User instance with the email)
        target = User(user_email)
        
        # Verify - compare actual results with expected results
        self.assertIsNotNone(target, "User object should not be None")
        self.assertEqual(target.email, user_email, "Email should be correctly assigned")
        
        # Expected result: A valid User object is created with the correct email address


if __name__ == "__main__":
    unittest.main()
