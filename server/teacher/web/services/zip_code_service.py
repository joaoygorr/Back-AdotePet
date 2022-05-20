import pycep_correios

def search_city_zip_Code(zip_code): 
    response = pycep_correios.get_address_from_cep(zip_code)
    return response