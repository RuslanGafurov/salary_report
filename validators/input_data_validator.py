import os


class InputDataValidator:
    """
    Класс валидации входных данных для генерации отчетов.
    :var VALID_REPORTS: Множество допустимых типов отчетов.
    """
    VALID_REPORTS: set[str] = {
        'payout',
    }

    def __init__(self, file_paths: list[str], report_type: str) -> None:
        """
        Инициализирует InputDataValidator с путями к файлам и типом отчета.
        :param file_paths: Список путей к файлам для валидации.
        :param report_type: Тип отчета для валидации.
        """
        self.file_paths: list[str] = file_paths
        self.report_type: str = report_type

    def validate(self) -> None:
        """
        Проверяет предоставленные пути к файлам и тип отчета.
        :except FileNotFoundError: Если любой из путей к файлам не существует.
        :except ValueError: Если тип отчета недопустим.
        """
        self.validate_files()
        self.validate_report_type()

    def validate_files(self) -> None:
        """
        Проверяет существование каждого файла в списке file_paths.
        :except FileNotFoundError: Если какой-либо файл не найден по указанному пути.
        """
        for file_path in self.file_paths:
            if not os.path.isfile(file_path):
                raise FileNotFoundError(f"Файл не найден: {file_path}")

    def validate_report_type(self) -> None:
        """
        Проверяет тип отчета по сравнению с множеством допустимых типов отчетов.
        :except ValueError: Если тип отчета не входит в множество допустимых отчетов.
        """
        if self.report_type not in self.VALID_REPORTS:
            raise ValueError("Недопустимый тип отчета: {}. Допустимые типы: {}".format(
                self.report_type, ', '.join(self.VALID_REPORTS)
            ))
