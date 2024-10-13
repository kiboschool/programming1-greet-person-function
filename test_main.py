from unittest.mock import patch, call
from unittest import TestCase
import unittest
from main import *

class Test(TestCase):
    @patch('builtins.print')
    def test_keno(self, mock_print):
        greet("Keno")
        mock_print.assert_has_calls([
            call("Welcome to Kibo, Keno"),
            call("We're glad you're here, Keno"),
            call("Keno, how did you hear about us?")
        ])

    @patch('builtins.print')
    def test_unusual_name(self, mock_print):
        greet("6🚀eeLLo👽")
        mock_print.assert_has_calls([
            call("Welcome to Kibo, 6🚀eeLLo👽"),
            call("We're glad you're here, 6🚀eeLLo👽"),
            call("6🚀eeLLo👽, how did you hear about us?")
        ])

if __name__ == '__main__':
    unittest.main()
