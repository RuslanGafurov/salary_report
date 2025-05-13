import argparse


class ValidateCSVFile(argparse.Action):
    """Класс валидации CSV-файлов."""

    def __call__(self, parser, namespace, values, option_string=None) -> None:
        for file_path in values:
            if not file_path.endswith('.csv'):
                raise argparse.ArgumentTypeError(f"{file_path} не является CSV файлом.")
        setattr(namespace, self.dest, values)
