import requests


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
    return input(f"{label} currency (e.g., INR, USA, AED, EUR, etc.): ").upper()


def get_exchange_rate(source, target):
    api_key = "80f3eadcff3fc22406535b8d42b63322"
    url = f"https://api.exchangeratesapi.io/v1/latest?access_key={api_key}&base={source}&symbols={target}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return float(data["rates"][target])
    except requests.exceptions.RequestException as e:
        print(f"error: {e}")
        return None


def convert(amount, source_cur, target_cur):
    exchange_rate = get_exchange_rate(source_cur, target_cur)
    if exchange_rate is not None:
        return amount * exchange_rate
    else:
        return None


def main():
    amount = get_amt()
    source_cur = get_currency("Source")
    target_cur = get_currency("Target")
    converted_amount = convert(amount, source_cur, target_cur)
    if converted_amount is not None:
        print(f"{amount} {source_cur} = {converted_amount} {target_cur}")
    else:
        print("Error")


if __name__ == "__main__":
    main()
