import requests

# Your CoinCap API key
API_KEY = "your_api_key_here"
URL = "https://rest.coincap.io/v3/assets/bitcoin"


def main():

    try:
        num_bitcoins = float(input("Enter the number of Bitcoins: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Fetch Bitcoin price from API with authorization
    try:
        headers = {"Authorization": f"Bearer {API_KEY}"}
        response = requests.get(URL, headers=headers)
        response.raise_for_status()
    except requests.RequestException:
        print("Error fetching data from API")
        return

    # Parse JSON response
    try:
        data = response.json()
        price_usd = float(data["data"]["priceUsd"])
    except (KeyError, ValueError, TypeError):
        print("Error parsing data from API")
        return

    total_cost = num_bitcoins * price_usd

    print(f"1 BTC = ${price_usd:,.2f}")
    print(f"{num_bitcoins} BTC = ${total_cost:,.2f}")


if __name__ == "__main__":
    main()
