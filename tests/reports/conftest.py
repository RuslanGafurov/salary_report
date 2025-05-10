from _pytest.fixtures import fixture


@fixture(scope='function')
def data_for_base_report() -> dict[str, str]:
    """Фикстура с данными для тестирования "BaseReport"."""
    return dict(
        data_1="""id,email,name,department,hours_worked,hourly_rate
                1,alice@example.com,Alice Johnson,Marketing,160,50
                2,bob@example.com,Bob Smith,Design,150,40
                3,carol@example.com,Carol Williams,Design,170,60""",
        data_2="""department,id,email,name,hours_worked,rate
                HR,101,grace@example.com,Grace Lee,160,45
                Marketing,102,henry@example.com,Henry Martin,150,35
                HR,103,ivy@example.com,Ivy Clark,158,38""",
        data_3="""email,name,department,hours_worked,salary,id
                karen@example.com,Karen White,Sales,165,50,201
                liam@example.com,Liam Harris,HR,155,42,202
                mia@example.com,Mia Young,Sales,160,37,203""",
    )


@fixture(scope='function')
def data_for_payout_report() -> list[dict[str, str | int]]:
    """Фикстура с данными для тестирования "PayoutReport"."""
    return [
        dict(name='Alice Johnson', department='Marketing', hours=160, rate=50, payout=8000),
        dict(name='Bob Smith',     department='Design',    hours=150, rate=40, payout=6000),
        dict(name='Grace Lee',     department='HR',        hours=160, rate=45, payout=7200),
        dict(name='Karen White',   department='Sales',     hours=165, rate=50, payout=8250),
    ]
