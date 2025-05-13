import argparse

from reports.payout_report import PayoutReport
from validators.csv_files_validator import ValidateCSVFile
from validators.input_data_validator import InputDataValidator


def main() -> None:
    """
    Функция запуска скрипта по формированию отчетов.

    Параметры:
        - files: Один или несколько путей к CSV-файлам, содержащим данные сотрудников.
        - --report: Тип отчета. Поддерживаемые типы: 'payout' - отчет о выплатах.
    """
    parser = argparse.ArgumentParser(description="Скрипт для подсчета зарплаты сотрудников.")
    parser.add_argument(
        'files',
        nargs='+',
        help='Пути к CSV-файлам с данными сотрудников',
        action=ValidateCSVFile,
    )
    parser.add_argument(
        '--report',
        required=True,
        help='Тип отчета для формирования',
        choices=('payout',)
    )
    args = parser.parse_args()

    validator = InputDataValidator(args.files, args.report)
    validator.validate()

    match args.report:

        case 'payout':
            report = PayoutReport(args.files)
            report.generate_report()

        # Можно добавить любой другой тип отчёта.


if __name__ == '__main__':
    main()
