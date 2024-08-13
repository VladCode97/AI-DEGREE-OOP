MONTHS = {
    1: 'JANUARY',
    2: 'FEBRUARY',
    3: 'MARCH',
    4: 'APRIL',
    5: 'MAY',
    6: 'JUNE',
    7: 'JULY',
    8: 'AUGUST',
    9: 'SEPTEMBER',
    10: 'OCTOBER',
    11: 'NOVEMBER',
    12: 'DECEMBER',
}

class VoluntarySaving:
    def __init__(self, name_client: str) -> None:
        self._month: int = 1
        self._money: float = 0
        self._profitability: float = 0.01
        self._name_client: str = name_client


    def add_money(self, money: float) -> None:
        self._money += money


    def settle_monthly_profit(self) -> None:
        self._calculate_profitability()
        print(self)
        self._increase_month()


    def _increase_month(self) -> None:
        self._month = (self._month % 12) + 1


    def _calculate_profitability(self) -> None:
        if 400000 < self._money <= 800000:
            self._profitability = 0.02
        elif self._money > 800000:
            self._profitability = 0.03
        else:
            self._profitability = 0.01
        self._money += self._money * self._profitability

    def __str__(self) -> str:
        return (f'------\n'
            f'Name: {self._name_client}\n'
            f'Money in account: {self._money}\n'
            f'Month: {MONTHS[self._month]}\n'
            f'------\n')


luis_client = VoluntarySaving('Luis E Bonilla')
luis_client.add_money(300000)
luis_client.settle_monthly_profit()
luis_client.add_money(600000)
luis_client.settle_monthly_profit()
luis_client.add_money(900000)
luis_client.settle_monthly_profit()
