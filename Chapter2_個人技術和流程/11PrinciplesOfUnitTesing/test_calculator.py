"""
Unit Tests for Calculator Module

This file contains unit tests for the Calculator class, demonstrating the 11 
principles of good unit testing as described in the document.

Principles demonstrated:
1. Detailed specifications expressed as test cases
2. Clear documentation of what the unit does and doesn't do
3. Testing the most basic functionality with parameters
4. Tests written by the author of the code
5. Machine state unchanged after tests (test isolation)
6. Fast tests (seconds, not minutes)
7. Repeatable, consistent results
8. Independent tests not relying on other tests
9. Complete code path coverage
10. Integration with automated testing framework
11. Tests stored and maintained with the product code
"""

import unittest
import tempfile
import os
from calculator import Calculator


class CalculatorTest(unittest.TestCase):
    """
    Test suite for the Calculator class.
    
    Each test method is designed to be independent, fast, and repeatable.
    The tests verify normal operation and error handling for all methods.
    """
    
    def setUp(self):
        """
        Set up a fresh calculator instance before each test.
        
        This follows principle #5 (unchanged machine state) and #8 (independence)
        by ensuring each test starts with a clean calculator.
        """
        self.calc = Calculator()
        
        # Principle #5: If we create any temporary files for testing,
        # ensure they're removed afterwards
        self.temp_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """
        Clean up after each test to ensure machine state is unchanged.
        
        This follows principle #5 by removing any temporary resources
        created during testing.
        """
        # Remove any temporary files created during tests
        if os.path.exists(self.temp_dir):
            for file in os.listdir(self.temp_dir):
                os.remove(os.path.join(self.temp_dir, file))
            os.rmdir(self.temp_dir)
    
    # Principle #3 and #9: Test basic functionality and cover all code paths
    
    def test_initial_state(self):
        """Test the initial state of the calculator."""
        # Verify initial memory is zero
        self.assertEqual(0, self.calc.get_memory())
        # Verify history starts empty
        self.assertEqual(0, len(self.calc.get_history()))
    
    def test_add_two_numbers(self):
        """Test adding two numbers."""
        result = self.calc.add(2, 3)
        self.assertEqual(5, result)
        self.assertEqual(0, self.calc.get_memory())  # Memory unchanged
        self.assertEqual(1, len(self.calc.get_history()))
    
    def test_add_to_memory(self):
        """Test adding a number to memory."""
        result = self.calc.add(5)
        self.assertEqual(5, result)
        self.assertEqual(5, self.calc.get_memory())  # Memory updated
        self.assertEqual(1, len(self.calc.get_history()))
    
    def test_subtract_two_numbers(self):
        """Test subtracting one number from another."""
        result = self.calc.subtract(10, 3)
        self.assertEqual(7, result)
        self.assertEqual(0, self.calc.get_memory())  # Memory unchanged
        self.assertEqual(1, len(self.calc.get_history()))
    
    def test_subtract_from_memory(self):
        """Test subtracting a number from memory."""
        # Set up memory
        self.calc.add(10)
        
        result = self.calc.subtract(3)
        self.assertEqual(7, result)
        self.assertEqual(7, self.calc.get_memory())  # Memory updated
        self.assertEqual(2, len(self.calc.get_history()))
    
    def test_multiply_two_numbers(self):
        """Test multiplying two numbers."""
        result = self.calc.multiply(4, 5)
        self.assertEqual(20, result)
        self.assertEqual(0, self.calc.get_memory())  # Memory unchanged
        self.assertEqual(1, len(self.calc.get_history()))
    
    def test_multiply_memory(self):
        """Test multiplying memory by a number."""
        # Set up memory
        self.calc.add(4)
        
        result = self.calc.multiply(5)
        self.assertEqual(20, result)
        self.assertEqual(20, self.calc.get_memory())  # Memory updated
        self.assertEqual(2, len(self.calc.get_history()))
    
    def test_divide_two_numbers(self):
        """Test dividing one number by another."""
        result = self.calc.divide(20, 5)
        self.assertEqual(4, result)
        self.assertEqual(0, self.calc.get_memory())  # Memory unchanged
        self.assertEqual(1, len(self.calc.get_history()))
    
    def test_divide_memory(self):
        """Test dividing memory by a number."""
        # Set up memory
        self.calc.add(20)
        
        result = self.calc.divide(5)
        self.assertEqual(4, result)
        self.assertEqual(4, self.calc.get_memory())  # Memory updated
        self.assertEqual(2, len(self.calc.get_history()))
    
    def test_clear_memory(self):
        """Test clearing the calculator's memory."""
        # Set up memory
        self.calc.add(42)
        self.assertEqual(42, self.calc.get_memory())
        
        # Clear memory
        result = self.calc.clear_memory()
        self.assertEqual(0, result)
        self.assertEqual(0, self.calc.get_memory())
        self.assertEqual(2, len(self.calc.get_history()))
    
    def test_get_history(self):
        """Test retrieving operation history."""
        self.calc.add(5)
        self.calc.subtract(2)
        self.calc.multiply(3)
        
        history = self.calc.get_history()
        self.assertEqual(3, len(history))
        self.assertTrue("Added: 5" in history[0])
        self.assertTrue("Subtracted: 2" in history[1])
        self.assertTrue("Multiplied: 3" in history[2])
    
    # Principle #9: Test error handling paths
    
    def test_add_invalid_type(self):
        """Test error handling when adding non-numeric values."""
        with self.assertRaises(TypeError):
            self.calc.add("not a number")
        
        with self.assertRaises(TypeError):
            self.calc.add(5, "not a number")
    
    def test_subtract_invalid_type(self):
        """Test error handling when subtracting non-numeric values."""
        with self.assertRaises(TypeError):
            self.calc.subtract("not a number")
        
        with self.assertRaises(TypeError):
            self.calc.subtract(5, "not a number")
    
    def test_multiply_invalid_type(self):
        """Test error handling when multiplying non-numeric values."""
        with self.assertRaises(TypeError):
            self.calc.multiply("not a number")
        
        with self.assertRaises(TypeError):
            self.calc.multiply(5, "not a number")
    
    def test_divide_invalid_type(self):
        """Test error handling when dividing non-numeric values."""
        with self.assertRaises(TypeError):
            self.calc.divide("not a number")
        
        with self.assertRaises(TypeError):
            self.calc.divide(5, "not a number")
    
    def test_divide_by_zero(self):
        """Test error handling when dividing by zero."""
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)
        
        # Set up memory
        self.calc.add(5)
        
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(0)


if __name__ == '__main__':
    """
    Run all test cases when this script is executed directly.
    
    This follows principle #10 by providing an automated test framework.
    """
    unittest.main() 