from datetime import datetime, timedelta

from app.config import settings
from app.deposit.schema import DepositSchema


def month_rate(rate: float) -> float:
    return rate / 100 / 12


def calculate_deposit(schema: DepositSchema) -> dict[str, float]:
    start_date: datetime = datetime.strptime(schema.date, settings.DATE_FORMAT)

    monthly_rate: float = month_rate(schema.rate)

    results: dict[str, float] = {}

    current_amount: float = schema.amount
    for period in range(schema.periods):
        interest: float = current_amount * monthly_rate
        current_amount += interest

        next_date = start_date + timedelta(days=30 * (period + 1))

        formatted_date = next_date.strftime(settings.DATE_FORMAT)

        results[formatted_date] = round(current_amount, 2)

    return results
