# Live Bitcoin Price Tracker

A simple Python script (bitcoin_price.py) that fetches the live Bitcoin price from the CoinCap API
 and calculates the value of any number of Bitcoins you enter.

## Features

- Fetches real-time Bitcoin price in USD.
- Lets you input the number of Bitcoins and shows their total value.
- Handles invalid inputs and API errors.
- Easy to extend for other cryptocurrencies.

## Install the dependency using:
```bash
pip install requests
```
## Getting an API Key

visit [CoinCAP](https://pro.coincap.io/dashboard) to get your API key
Navigate to your API settings.
Generate a new API key.

Open bitcoin_price.py and replace the placeholder with your key:
```python
API_KEY = "your_api_key_here"
```

## Usage

- Clone this repository
- Add your API key as shown above.
- Run the script:
```bash
python bitcoin_price.py
```
- Enter the number of Bitcoins when prompted.

### Example
```bash
Enter the number of Bitcoins: 2
1 BTC = $58,123.45
2 BTC = $116,246.90
```
