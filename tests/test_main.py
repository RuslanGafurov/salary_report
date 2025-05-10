from unittest.mock import patch, MagicMock

import pytest

from main import main


@pytest.mark.parametrize('file_paths, report_type', [
    (['data.data1.csv', 'data.data2.csv', 'data.data3.csv'], 'payout'),
])
@patch('argparse.ArgumentParser.parse_args')
@patch('validators.input_data_validator.InputDataValidator.validate')
@patch('reports.payout_report.PayoutReport.generate_report')
@patch('reports.base_report.BaseReport.read_files')
def test_main_payout_report(mock_read_files, mock_payout_report, mock_input_data_validator, mock_parse_args, file_paths, report_type):

    mock_parse_args.return_value = MagicMock(files=file_paths, report=report_type)
    mock_input_data_validator.return_value = None
    mock_payout_report.return_value = None
    mock_read_files.return_value = None

    main()

    mock_input_data_validator.assert_called_once()
    mock_payout_report.assert_called_once()
