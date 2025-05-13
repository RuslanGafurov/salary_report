from collections import defaultdict

from reports.base_report import BaseReport


class PayoutReport(BaseReport):
    """Класс для генерации отчетов о выплатах на основе данных из файлов."""

    def __init__(self, file_paths: list[str]) -> None:
        """
        Инициализирует экземпляр "PayoutReport" и считывает файлы.
        :param file_paths: Список путей к файлам для чтения.
        """
        super().__init__(file_paths)
        self.read_files()

    def generate_report(self) -> None:
        """Генерирует отчет, группируя данные по отделам и выводя их на экран."""

        grouped_data_by_department: defaultdict[str, list] = self.group_data_by_department()
        lengths: dict[str, int] = self.get_max_lengths()
        self.print_report(grouped_data_by_department, lengths)

    def get_max_lengths(self) -> dict[str, int]:
        """
        Вычисляет максимальные длины строк для каждого поля отчета.
        :return: Словарь с максимальными длинами.
        """

        step: int = 3  # Шаг (отступ в теле отчета).

        department_length: int = len(max([dct['department'] for dct in self.data], key=len)) + step
        name_length: int = len(max([dct['name'] for dct in self.data], key=len)) + step
        hours_length: int = len(max([str(dct['hours']) for dct in self.data], key=len)) + step
        rate_length: int = len(max([str(dct['rate']) for dct in self.data], key=len)) + step
        payout_length: int = len(max([str(dct['payout']) for dct in self.data], key=len)) + step

        return dict(
            department=department_length,
            name=name_length if name_length >= len('name') else len('name'),
            hours=hours_length if hours_length >= len('hours') else len('hours'),
            rate=rate_length if rate_length >= len('rate') else len('rate'),
            payout=payout_length if payout_length >= len('payout') else len('payout'),
            step=step,
        )

    def group_data_by_department(self) -> defaultdict[str, list]:
        """
        Группирует данные по отделам.
        :return: Словарь, где ключи - названия отделов, а значения - списки данных сотрудников.
        """

        grouped_data_by_department: defaultdict[str, list] = defaultdict(list)
        for data in self.data:
            grouped_data_by_department[data.get('department')].append(dict(
                name=data.get('name'),
                hours=data.get('hours'),
                rate=data.get('rate'),
                payout=data.get('payout'),
            ))
        return grouped_data_by_department

    @staticmethod
    def print_report(grouped_data: defaultdict[str, list], lengths: dict[str, int]) -> None:
        """
        Выводит отчет в формате сгруппированной по отделам таблицы.
        :param grouped_data: Словарь с группированными данными по отделам.
        :param lengths: Словарь с максимальными длинами для каждого поля.
        """

        # Вывод наименований колонок.
        print("{:<{}} {:<{}} {:<{}} {:<{}} {:<{}}".format(
            ' ', lengths['department'] + lengths['step'],
            'name', lengths['name'],
            'hours', lengths['hours'],
            'rate', lengths['rate'],
            'payout', lengths['payout']
        ))

        # Отступы.
        indentation: str = '-' * lengths['department'] + '-' * lengths['step']
        total_indentation: str = f"{' ':<{len(indentation) + lengths['name'] + 1}}"

        for department, data_list in grouped_data.items():
            total_hours: int = 0
            total_payout: int = 0

            # Вывод наименования отдела.
            print(f"{department:<{lengths['department']}}")

            for data in data_list:
                # Вывод данных по каждому сотруднику.
                print("{} {:<{}} {:<{}} {:<{}} ${:<{}}".format(
                    indentation,
                    data.get('name'), lengths['name'],
                    data.get('hours'), lengths['hours'],
                    data.get('rate'), lengths['rate'],
                    data.get('payout'), lengths['payout']
                ))

                total_hours += data.get('hours')
                total_payout += data.get('payout')

            # Вывод итоговых данных по отделу.
            print("{} {:<{}} {:<{}} ${:<{}}".format(
                total_indentation,
                total_hours, lengths['hours'],
                '', lengths['rate'],
                total_payout, lengths['payout']
            ))
