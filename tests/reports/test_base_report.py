from unittest.mock import patch

import pytest

from reports.base_report import BaseReport


class TestPayoutReport:

    @patch(target='reports.base_report.BaseReport.parse_data')
    @patch(target='builtins.open')
    def test_read_files(self, mock_file, mock_parse):

        mock_file.return_value.__iter__.return_value = None
        mock_parse.return_value = None

        report = BaseReport(['folder/file.format'])
        report.read_files()

        mock_file.assert_called_once()
        mock_parse.assert_called_once()

    @pytest.mark.parametrize('data_key', ['data_1', 'data_2', 'data_3'])
    @patch(target='reports.base_report.BaseReport.parse_line')
    def test_parse_data(self, mock_parse_line, data_for_base_report, data_key):

        mock_parse_line.return_value = None

        report = BaseReport(['folder/file.format'])
        report.parse_data(data_for_base_report[data_key].split('\n'))

        assert mock_parse_line.call_count == 3

    @pytest.mark.parametrize('data_key, expected_result', [
        (
                'data_1', dict(name='Alice Johnson', email='alice@example.com',
                               department='Marketing', hours=160, rate=50, payout=160 * 50)
        ),
        (
                'data_2', dict(name='Grace Lee', email='grace@example.com',
                               department='HR', hours=160, rate=45, payout=160 * 45)
        ),
        (
                'data_3', dict(name='Karen White', email='karen@example.com',
                               department='Sales', hours=165, rate=50, payout=165 * 50)
        ),
    ])
    def test_parse_line(self, data_for_base_report, data_key, expected_result):

        line = data_for_base_report[data_key].split('\n')[1]
        headers = data_for_base_report[data_key].split('\n')[0].split(',')
        col_map = {column.lower(): idx for idx, column in enumerate(headers)}

        result_data = BaseReport.parse_line(line, col_map)

        assert result_data == expected_result
