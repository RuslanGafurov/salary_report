from collections import defaultdict
from unittest.mock import patch
import pytest

from reports.payout_report import PayoutReport


class TestPayoutReport:

    @patch('reports.payout_report.PayoutReport.group_data_by_department')
    @patch('reports.payout_report.PayoutReport.get_max_lengths')
    @patch('reports.payout_report.PayoutReport.print_report')
    @patch('reports.base_report.BaseReport.read_files')
    def test_generate_report(self, mock_read_files, mock_print_report, mock_group_data, mock_lengths,
                                                                                data_for_payout_report):

        mock_read_files.return_value = None
        mock_group_data.return_value = None
        mock_lengths.return_value = None

        report = PayoutReport(['folder/file.format'])
        report.data = data_for_payout_report
        report.generate_report()

        mock_group_data.assert_called_once()
        mock_lengths.assert_called_once()
        mock_print_report.assert_called_once()

    @patch('reports.base_report.BaseReport.read_files')
    def test_get_max_lengths(self, mock_read_files, data_for_payout_report):

        mock_read_files.return_value = None

        report = PayoutReport(['folder/file.format'])
        report.data = data_for_payout_report
        lengths = report.get_max_lengths()

        assert lengths['department'] == 12  # 'Marketing' + step
        assert lengths['name'] == 16        # 'Alice Johnson' + step
        assert lengths['hours'] == 6        # '160' + step
        assert lengths['rate'] == 5         # '50' + step
        assert lengths['payout'] == 7       # '8250' + step
        assert lengths['step'] == 3         # Шаг = 3

    @pytest.mark.parametrize('expected_data', [
        {'Marketing': [dict(name='Alice Johnson', hours=160, rate=50, payout=8_000)]},
    ])
    @patch('reports.base_report.BaseReport.read_files')
    def test_group_data_by_department(self, mock_read_files, data_for_payout_report, expected_data):

        mock_read_files.return_value = None

        report = PayoutReport(['folder/file.format'])
        report.data = data_for_payout_report
        grouped_data = report.group_data_by_department()

        assert isinstance(grouped_data, defaultdict)
        assert len(grouped_data) == 4               # 4 отдела
        assert len(grouped_data['Marketing']) == 1  # 1 сотрудник в Marketing
        assert len(grouped_data['Design']) == 1     # 1 сотрудник в Design
        assert len(grouped_data['HR']) == 1         # 1 сотрудник в HR
        assert len(grouped_data['Sales']) == 1      # 1 сотрудник в Sales

        assert grouped_data['Marketing'] == expected_data['Marketing']

    @patch('builtins.print')
    @patch('reports.base_report.BaseReport.read_files')
    def test_print_report(self, mock_read_files, mock_print, data_for_payout_report):

        mock_read_files.return_value = None

        report = PayoutReport(['folder/file.format'])
        report.data = data_for_payout_report
        lengths = report.get_max_lengths()
        grouped_data = report.group_data_by_department()

        report.print_report(grouped_data, lengths)

        assert mock_print.call_count == 13
