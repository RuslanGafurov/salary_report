from typing import Any


class BaseReport:
    """Базовый класс для обработки отчетов на основе данных из csv-файлов."""

    def __init__(self, file_paths: list[str]):
        """
        Инициализирует экземпляр "BaseReport".
        :param file_paths: Список путей к файлам для чтения.
        """
        self.file_paths: list[str] = file_paths
        self.data: list[dict[str, Any]] = []

    def read_files(self):
        """Считывает файлы, указанные в self.file_paths, и парсит их содержимое."""

        for file_path in self.file_paths:
            with open(file=file_path, mode='r', encoding='utf-8') as file:
                lines: list[str] = file.readlines()
                if not lines:
                    continue
                self.parse_data(lines)

    def parse_data(self, lines: list[str]):
        """
        Парсит данные из строк и добавляет их в self.data.
        :param lines: Список строк с данными для парсинга.
        """
        headers: list[str] = lines[0].strip().split(',')
        col_map: dict[str, int] = {column.lower(): idx for idx, column in enumerate(headers)}
        for line in lines[1:]:
            if line.strip():
                self.data.append(self.parse_line(line, col_map))

    @staticmethod
    def parse_line(line: str, col_map: dict[str, int]) -> dict[str, str | int]:
        """
        Парсит одну строку данных и возвращает словарь с результатами.
        :param line: Строка, содержащая данные.
        :param col_map: Словарь, связывающий названия колонок с их индексами.
        :return: Словарь с данными, включая имя, электронную почту, отдел, отработанные часы, ставку и выплату.
        """

        line: list[str] = line.strip().split(',')

        name: str = line[col_map.get('name')]
        email: str = line[col_map.get('email')]
        department: str = line[col_map.get('department')]
        hours: int = int(line[col_map.get('hours_worked')])
        rate: int = 0

        possible_rate_names: list[str] = ['hourly_rate', 'rate', 'salary']
        for rate_key in possible_rate_names:
            if rate_key in col_map:
                rate = int(line[col_map.get(rate_key)])
                break

        return dict(
            name=name,
            email=email,
            department=department,
            hours=hours,
            rate=rate,
            payout=hours * rate,
        )
