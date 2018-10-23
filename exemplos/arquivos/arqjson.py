import json

pessoa = {
    "nome": "Antonio",
    "sobrenome": "Dias",
    "cargo": "Professor",
    "endereco": {
        "rua": "Rua XYZ",
        "numero": 123
    },
    "matricula": 12345
}

with open('meujson', 'w') as file:
    json.dump(pessoa, file)
