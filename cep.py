import pycep_correios

endereco = pycep_correios.get_address_from_cep('78095394')

print(endereco['bairro'])
print(endereco['cidade'])
print(endereco['complemento'])
print(endereco['uf'])
print(endereco['cep'])
print(endereco)