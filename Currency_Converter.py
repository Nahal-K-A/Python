import decimal


def get_amt():
    while True:
        try:
            amount = decimal.Decimal(input("Enter the amount: "))
            if amount <= 0:
                raise ValueError()
            return amount
        except decimal.InvalidOperation:
            print("Invalid Amount")


def get_currency(label):
    currencies = [
        "USD",
        "INR",
        "AED",
        "EUR",
    ]
    while True:
        currency = input(f"{label} currency (INR/USD/AED/EUR): ").upper()
        if currency not in currencies:
            print("Invalid Currency")
        else:
            return currency


def converter(amount, source, target):
    exchange_rates = {
        "INR": {
            "AED": decimal.Decimal("0.0435"),
            "USD": decimal.Decimal("0.0119"),
            "EUR": decimal.Decimal("0.0111"),
        },
        "USD": {
            "INR": decimal.Decimal("84.98"),
            "AED": decimal.Decimal("3.67"),
            "EUR": decimal.Decimal("0.93"),
        },
        "EUR": {
            "AED": decimal.Decimal("3.94"),
            "USD": decimal.Decimal("1.07"),
            "INR": decimal.Decimal("90.48"),
        },
        "AED": {
            "INR": decimal.Decimal("22.97"),
            "USD": decimal.Decimal("0.2723"),
            "EUR": decimal.Decimal("0.2539"),
        },
    }

    if source == target:
        return amount
    return amount * exchange_rates[source][target]


def main():
    source_cur = get_currency("Source")
    target_cur = get_currency("Target")
    amount = get_amt()
    result = converter(amount, source_cur, target_cur)
    print(f"{amount} {source_cur} = {result} {target_cur}")


if __name__ == "__main__":
    main()
