def get_amt():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                raise ValueError()
            return amount
        except ValueError:
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
        "INR": {"AED": 0.0435, "USD": 0.0119, "EUR": 0.0111},
        "USD": {"INR": 84.98, "AED": 3.67, "EUR": 0.93},
        "EUR": {"AED": 3.94, "USD": 1.07, "INR": 90.48},
        "AED": {"INR": 22.97, "USD": 0.2723, "EUR": 0.2539},
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
