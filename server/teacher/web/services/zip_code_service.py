import requests

def search_city_zip_Code(zip_code): 
    response = requests.get(
        f"http://viacep.com.br/ws/{zip_code}/json"
    )
    return response