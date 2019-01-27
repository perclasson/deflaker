import datetime


class Currency:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def format_value(self):
        if self.currency == 'USD':
            return '${amount}'.format(amount=self.amount)
        elif self.currency == 'EUR':
            return '{amount}€'.format(amount=self.amount)
        else:
            raise NotImplementedError

    def with_date(self):
        return '{value} on {date}'.format(
            value=self.format_value(),
            date=str(datetime.date.today),
        )