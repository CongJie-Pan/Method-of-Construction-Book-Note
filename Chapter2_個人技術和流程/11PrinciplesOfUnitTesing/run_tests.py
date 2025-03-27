#!/usr/bin/env python
"""
Test Runner Script

This script demonstrates Principle #10: Integration with automated testing framework.
It runs all unit tests and generates a coverage report to verify Principle #9:
Complete code path coverage.

Usage:
    python run_tests.py
"""

import unittest
import coverage
import sys
import os


def run_tests_with_coverage():
    """
    Run all tests with coverage analysis.
    
    This function demonstrates automated test execution with code coverage
    reporting, showing how well our tests adhere to Principle #9 (complete
    code path coverage).
    
    Returns:
        True if all tests passed, False otherwise
    """
    # Start code coverage measurement
    cov = coverage.Coverage(
        source=['calculator'],
        omit=['*test*'],
    )
    cov.start()
    
    # Discover and run all tests
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('.', pattern='test_*.py')
    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(test_suite)
    
    # Stop coverage and generate report
    cov.stop()
    cov.save()
    
    print("\n\n===== Code Coverage Report =====")
    
    # Terminal report
    cov.report()
    
    # Generate HTML report
    html_dir = os.path.join(os.path.dirname(__file__), 'coverage_html')
    if not os.path.exists(html_dir):
        os.makedirs(html_dir)
    
    cov.html_report(directory=html_dir)
    print(f"\nHTML coverage report generated in: {html_dir}")
    
    return len(result.failures) == 0 and len(result.errors) == 0


if __name__ == "__main__":
    """
    Main entry point for the test runner.
    """
    print("===== Running Calculator Unit Tests =====")
    success = run_tests_with_coverage()
    
    # Exit with appropriate status code for CI/CD integration
    sys.exit(0 if success else 1) 