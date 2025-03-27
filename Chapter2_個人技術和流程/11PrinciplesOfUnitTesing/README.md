# Unit Testing Demo: The 11 Principles

This project demonstrates the 11 principles of effective unit testing described in the document "單元測試的11原則" (11 Principles of Unit Testing).

## Project Structure

- `calculator.py` - Main module containing the Calculator class
- `test_calculator.py` - Unit tests for the Calculator class
- `run_tests.py` - Script to run all tests with coverage reporting
- `requirements.txt` - Dependencies needed to run tests
- `單元測試的11原則.txt` - Original principles document (in Traditional Chinese)

## The 11 Principles Demonstrated

1. **Detailed Specifications**: Tests in `test_calculator.py` serve as detailed specifications for what the Calculator module should do.

2. **Clear Documentation**: Tests document what the Calculator can and cannot do, serving as both examples and requirements.

3. **Basic Functionality Testing**: Tests verify the most basic operations and parameters of the Calculator class.

4. **Written by Code Author**: Tests are maintained alongside the code they test.

5. **Unchanged Machine State**: `setUp()` and `tearDown()` methods ensure tests leave no lingering state changes.

6. **Fast Tests**: All tests are designed to run quickly (milliseconds each).

7. **Repeatable Results**: Tests produce consistent, deterministic results on each run.

8. **Independent Tests**: Each test function is self-contained and doesn't depend on other tests.

9. **Complete Code Path Coverage**: Tests cover both normal operation and error handling paths.

10. **Automated Testing Framework**: Tests integrate with unittest and can be run automatically via `run_tests.py`.

11. **Stored with Product Code**: Tests are maintained in the same repository as the code they test.

## How to Run the Tests

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run tests with coverage:
   ```
   python run_tests.py
   ```

   Or using pytest directly:
   ```
   pytest -v --cov=calculator
   ```

## Code Coverage

The run_tests.py script generates an HTML coverage report showing which parts of the code are covered by the tests. This demonstrates Principle #9 (Complete Code Path Coverage).

## Using the Calculator

```python
from calculator import Calculator

# Create a calculator
calc = Calculator()

# Perform operations
result = calc.add(5, 3)  # 8
memory = calc.add(10)    # Memory becomes 10
result = calc.multiply(5)  # 50 (memory * 5)
calc.clear_memory()      # Memory reset to 0

# Get history of operations
history = calc.get_history()
``` 