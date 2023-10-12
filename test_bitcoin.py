import unittest
from bitcoin import calculate_bitcoin_value
from unittest.mock import patch, MagicMock

class TestBitcoinConversion(unittest.TestCase):
    @patch('requests.get')
    def test_calculate_bitcoin_value(self, mock_print, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'bpi': {'USD': {'rate_float': 50000.0}}
        }
        mock_get.return_value = mock_response

        bitcoin = 2.5
        expected_value = bitcoin * 50000.0

        result = calculate_bitcoin_value(bitcoin)
        mock_print.assert_called_once_with(result, expected_value)

if __name__ == '__main__':
    unittest.main()
