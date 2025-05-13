import argparse
from contextlib import nullcontext as does_not_raise
from unittest.mock import MagicMock

import pytest

from validators.csv_files_validator import ValidateCSVFile


class TestValidateCSVFile:
    """Тестирует класс "ValidateCSVFile"."""

    @pytest.mark.parametrize('file_paths, expected_exception', [
        (['file_1.csv', 'file_2.csv'], does_not_raise()),
        (['file_1.txt', 'file_2.csv'], pytest.raises(argparse.ArgumentTypeError)),
        (['file_1.csv', 'file_2.txt'], pytest.raises(argparse.ArgumentTypeError)),
        (['file_1.txt', 'file_2.txt'], pytest.raises(argparse.ArgumentTypeError)),
    ])
    def test_validate_csv_file(self, file_paths, expected_exception):
        """Тестирует метод "validate_csv_file"."""

        parser = MagicMock()
        namespace = MagicMock()

        action = ValidateCSVFile(option_strings=['--files'], dest='files')

        with expected_exception:
            action(parser, namespace, file_paths)

        if not expected_exception:
            assert namespace.files == file_paths
