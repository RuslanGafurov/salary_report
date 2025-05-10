# Salary Report

Проект на основе Python для генерации отчетов из CSV-файлов, содержащих данные о сотрудниках.

## Возможности

- Обработка нескольких CSV-файлов;
- Генерация отчетов;
- Валидация входных данных и типов отчетов.

## Зависимости

- Python 3.x
- pytest==8.3.5
- coverage==7.8.0

## Установка

1. Создание виртуальной среды:
```bash
python -m venv .venv
```
2. Активация виртуальной среды:
- Windows:
```bash
.venv\Scripts\activate
```
- Unix/MacOS:
```bash
source .venv/bin/activate
```
3. Установка зависимостей:
```bash
pip install -r requirements
```

## Использование

Генерация отчета происходит путем запуска скрипта в консоли:

```bash
python main.py <file_paths> --report <report_type>
```

### Аргументы

- `file_paths`: Один или несколько путей к CSV-файлам, содержащим данные о сотрудниках;
- `--report`: Тип отчета для генерации (в настоящее время поддерживает 'payout').

### Формат CSV-файла

Входные CSV-файлы должны содержать следующие столбцы:
- name: Имя сотрудника;
- email: Электронная почта сотрудника;
- department: Наименование отдела;
- hours_worked: Количество отработанных часов;
- hourly_rate/rate/salary: Почасовая ставка или зарплата.

### Пример запуска

```bash
python main.py data/data1.csv data/data2.csv data/data3.csv --report payout
```

## Структура проекта

```
salary_report/
├── data/
├── reports/
│   ├── base_report.py
│   └── payout_report.py
├── tests/
│   ├── test_main.py
│   ├── reports/
│   │   ├── conftest.py
│   │   ├── test_base_report.py
│   │   └── test_payout_report.py
│   ├── validators/
│   │   └── test_input_data_validator.py
├── validators/
│   └── input_data_validator.py
├── main.py
└── requirements
```

## Тестирование

Запуск тестов с использованием pytest:
```bash
pytest
```

Запуск тестов с использованием coverage:
```bash
coverage run -m pytest
coverage report
```

## Добавление новых отчетов

Для добавления нового отчета можно наследоваться от BaseReport, в котором реализован функционал обработки данных.