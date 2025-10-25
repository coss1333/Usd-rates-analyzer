import requests
from datetime import datetime, timedelta

# 10 главных валют мира
CURRENCIES = ["EUR", "GBP", "JPY", "CHF", "CAD", "AUD", "NZD", "CNY", "SEK", "NOK"]

def get_exchange_rates(date):
    """Получить курсы валют по отношению к USD на указанную дату"""
    url = f"https://api.exchangerate.host/{date}?base=USD"
    response = requests.get(url)
    data = response.json()
    return {cur: data["rates"][cur] for cur in CURRENCIES if cur in data["rates"]}

def show_changes():
    today = datetime.utcnow().date()
    yesterday = today - timedelta(days=1)

    today_rates = get_exchange_rates(today)
    yesterday_rates = get_exchange_rates(yesterday)

    print(f"\nИзменение курса USD относительно 10 валют мира ({yesterday} → {today})\n")
    print("{:<8} {:>12} {:>12} {:>12}".format("Валюта", "Вчера", "Сегодня", "Изм. %"))
    print("-" * 46)

    for cur in CURRENCIES:
        old = yesterday_rates.get(cur)
        new = today_rates.get(cur)
        if old and new:
            change = ((new - old) / old) * 100
            print(f"{cur:<8} {old:>12.4f} {new:>12.4f} {change:>11.2f}%")

    print("\nИсточник данных: exchangerate.host\n")

if __name__ == "__main__":
    show_changes()
