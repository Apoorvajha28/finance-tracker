import requests


def get_rate(from_currency, to_currency):
    url = f"https://api.frankfurter.dev/v1/latest?base={from_currency}&symbols={to_currency}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()      # Raises an error if request failed
    data = response.json()           # Turns the JSON response into a Python dictionary
    return data["rates"][to_currency]


if __name__ == "__main__":
    try:
        rate = get_rate("EUR", "INR")
        print(f"1 EUR = {rate} INR (today's live rate)")

        total_eur = 1127.49
        total_inr = total_eur * rate
        print(f"Your total of {total_eur} EUR = {total_inr: .2f} INR")
    except requests.RequestException as error:
        print(f"Could not fetch exchange rate: {error}")


      