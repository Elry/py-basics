from forex_python.converter import CurrencyRates

# Create a CurrencyRates object
c = CurrencyRates()

# Replace 'USD' and 'EUR' with the currency codes for the conversion you want
source_currency = 'USD'
target_currency = 'EUR'

# Get the exchange rate from source_currency to target_currency
exchange_rate = c.get_rate(source_currency, target_currency)

print(f"1 {source_currency} = {exchange_rate:.2f} {target_currency}")
