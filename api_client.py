import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("api.log"),
        logging.StreamHandler()
    ]
)

ASSETS = {
    "Selic" : 11,
    "CDI" : 12,
    "USD/BRL" : 1,
    "EUR/BRL" : 21619,
}

def get_asset(code:int) -> float:
    try:
        data = requests.get(f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{code}/dados/ultimos/1?formato=json")
        data_json = data.json()

        return float(data_json[0]['valor'])
    
    except requests.exceptions.ConnectionError:
        logging.error("API fora de ar!")
        raise
    
    except IndexError:
        logging.error("API retornou lista vazia")
        raise