from contextlib import nullcontext as does_not_raise
from unittest.mock import patch

import pytest

from validators.input_data_validator import InputDataValidator


class TestInputDataValidator:
    """Тестирует класс "InputDataValidator"."""

    @pytest.mark.parametrize('input_file_paths, valid_file_paths,  report_type, exception', [
        (['folder/file_1.format'], ['folder/file_1.format'], 'valid_report', does_not_raise()),
        (['folder/file_2.format'], ['folder/file_2.format'], 'invalid_report', pytest.raises(ValueError)),
        (['folder/file_3.format'], ['folder/file_1.format'], 'valid_report', pytest.raises(FileNotFoundError)),
    ])
    @patch(target='os.path.isfile')
    @patch.object(InputDataValidator, 'VALID_REPORTS', new={'valid_report'})
    def test_validate(self, mock_isfile, input_file_paths, valid_file_paths, report_type, exception):
        """Тестирует метод "validate"."""

        mock_isfile.side_effect = lambda path: path in valid_file_paths
        validator = InputDataValidator(input_file_paths, report_type)
        with exception:
            validator.validate()

    @pytest.mark.parametrize('file_paths, valid_file_paths, report_type, exception', [
        (['folder/file_1.format'], ['folder/file_1.format'], 'report', does_not_raise()),
        (['folder/file_2.format'], ['folder/file_1.format'], 'report', pytest.raises(FileNotFoundError)),
    ])
    @patch('os.path.isfile')
    def test_validate_files(self, mock_isfile, file_paths, valid_file_paths, report_type, exception):
        """Тестирует метод "validate_files"."""

        mock_isfile.side_effect = lambda path: path in valid_file_paths
        validator = InputDataValidator(file_paths, report_type)
        with exception:
            validator.validate_files()

    @pytest.mark.parametrize('file_paths, report_type, exception', [
        (['folder/file_1.format'], 'valid_report', does_not_raise()),
        (['folder/file_1.format'], 'invalid_report', pytest.raises(ValueError)),
    ])
    @patch.object(InputDataValidator, 'VALID_REPORTS', new={'valid_report'})
    def test_validate_report_type(self, file_paths, report_type, exception):
        """Тестирует метод "validate_report_type"."""

        validator = InputDataValidator(file_paths, report_type)
        with exception:
            validator.validate_report_type()
