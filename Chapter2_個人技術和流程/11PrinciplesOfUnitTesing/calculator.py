"""
Calculator Module

This module implements a simple calculator with basic arithmetic operations.
It serves as the subject under test for our unit testing demonstration.
"""


class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations.
    
    This class demonstrates a clean, testable module with clearly defined
    responsibilities and proper error handling for all operations.
    """
    
    def __init__(self):
        """
        Initialize the calculator with a memory value of 0.
        """
        self.memory = 0
        self.history = []
    
    def add(self, a, b=None):
        """
        Add two numbers or add a number to memory.
        
        Args:
            a: First number to add.
            b: Second number to add. If None, adds 'a' to memory.
            
        Returns:
            The sum of the two numbers or the new memory value.
            
        Raises:
            TypeError: If inputs are not numeric.
        """
        if not isinstance(a, (int, float)):
            raise TypeError("First argument must be a number")
            
        if b is not None:
            if not isinstance(b, (int, float)):
                raise TypeError("Second argument must be a number")
            result = a + b
        else:
            result = self.memory + a
            self.memory = result
            
        self.history.append(f"Added: {a}" + (f" and {b}" if b is not None else " to memory"))
        return result
    
    def subtract(self, a, b=None):
        """
        Subtract one number from another or subtract a number from memory.
        
        Args:
            a: First number.
            b: Number to subtract from first number. If None, subtracts 'a' from memory.
            
        Returns:
            The result of subtraction.
            
        Raises:
            TypeError: If inputs are not numeric.
        """
        if not isinstance(a, (int, float)):
            raise TypeError("First argument must be a number")
            
        if b is not None:
            if not isinstance(b, (int, float)):
                raise TypeError("Second argument must be a number")
            result = a - b
        else:
            result = self.memory - a
            self.memory = result
            
        self.history.append(f"Subtracted: {a}" + (f" from {b}" if b is not None else " from memory"))
        return result
    
    def multiply(self, a, b=None):
        """
        Multiply two numbers or multiply memory by a number.
        
        Args:
            a: First number.
            b: Second number. If None, multiplies memory by 'a'.
            
        Returns:
            The product of the two numbers or the new memory value.
            
        Raises:
            TypeError: If inputs are not numeric.
        """
        if not isinstance(a, (int, float)):
            raise TypeError("First argument must be a number")
            
        if b is not None:
            if not isinstance(b, (int, float)):
                raise TypeError("Second argument must be a number")
            result = a * b
        else:
            result = self.memory * a
            self.memory = result
            
        self.history.append(f"Multiplied: {a}" + (f" and {b}" if b is not None else " with memory"))
        return result
    
    def divide(self, a, b=None):
        """
        Divide one number by another or divide memory by a number.
        
        Args:
            a: First number (dividend if b is provided, divisor if b is None).
            b: Second number (divisor). If None, divides memory by 'a'.
            
        Returns:
            The result of division.
            
        Raises:
            TypeError: If inputs are not numeric.
            ZeroDivisionError: If the divisor is zero.
        """
        if not isinstance(a, (int, float)):
            raise TypeError("First argument must be a number")
            
        if b is not None:
            if not isinstance(b, (int, float)):
                raise TypeError("Second argument must be a number")
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = a / b
        else:
            if a == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = self.memory / a
            self.memory = result
            
        self.history.append(f"Divided: {a}" + (f" by {b}" if b is not None else " with memory"))
        return result
    
    def clear_memory(self):
        """
        Reset the memory to zero.
        
        Returns:
            Zero (the new memory value).
        """
        self.memory = 0
        self.history.append("Memory cleared")
        return self.memory
    
    def get_memory(self):
        """
        Get the current memory value.
        
        Returns:
            The current memory value.
        """
        return self.memory
    
    def get_history(self):
        """
        Get the history of operations.
        
        Returns:
            A list of operations performed.
        """
        return self.history 