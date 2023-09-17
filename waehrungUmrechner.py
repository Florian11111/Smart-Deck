import requests

urlConverter = 'https://api.exchangerate-api.com/v4/latest/USD'

def convert(from_currency, to_currency, amount): 
    try:
        # Anfrage an die API senden
        currencies = requests.get(urlConverter).json()['rates']
    except Exception as e:
        print(f'Ein Fehler ist aufgetreten: {str(e)}')
        return -1
    if from_currency != 'USD' : 
        amount = amount / currencies[from_currency] 
    amount = round(amount * currencies[to_currency], 4) 
    return amount

urlCrypto = 'https://api.coingecko.com/api/v3/simple/price'
paramsCrypto = {
    'ids': 'bitcoin,dogecoin,ethereum',
    'vs_currencies': 'eur',
}
def euro_cryptop():
    try:
        # Anfrage an die API senden
        response = requests.get(urlCrypto, params=paramsCrypto)
    except Exception as e:
        print(f'Ein Fehler ist aufgetreten: {str(e)}')
        return -1

    # Überprüfen, ob die Anfrage erfolgreich war
    if response.status_code == 200:
        data = response.json()
        temp = []
        temp.append(data['bitcoin']['eur'])
        temp.append(data['dogecoin']['eur'])
        temp.append(data['ethereum']['eur'])
        return temp
    else:
        print(response.status_code)
        print('Fehler beim Abrufen der Kurse')
        return -1
    
if __name__ == "__main__":
    print(convert('EUR','USD', 1))
    print(euro_cryptop())