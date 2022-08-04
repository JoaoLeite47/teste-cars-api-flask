Cliente_list = [
    {"id": 0, "cpf": 12312343256, "rg": 123456789, "dt_nasc": 12082001,
        "cnh": 123456789, "nome": "João", "endereco": "Rua 1"},
    {"id": 1, "cpf": 12312343257, "rg": 123456789, "dt_nasc": 12082001,
        "cnh": 123456789, "nome": "Maria", "endereco": "Rua 1"},
    {"id": 2, "cpf": 12312343258, "rg": 123456789, "dt_nasc": 12082001,
        "cnh": 123456789, "nome": "Gustavo", "endereco": "Rua 1"},
]

Alocacao_List = [
    {"id": 0, "cpf_cliente": 12312343256, "hr_saida": 12,
        "dt_saida": 12082001, "hr_entrega": 12, "dt_entrega": 12082001, },
    {"id": 1, "cpf_cliente": 12312343256, "hr_saida": 13,
        "dt_saida": 12082001, "hr_entrega": 13, "dt_entrega": 12082001, }
]

Carro_List = [
    {"id": 0, "chassi": 12332123, "cor": "preto", "modelo": "Gol",
        "marca": "Volkswagem", "placa": "ABC-1234", "ano": 2012, "cod_categoria": 4},
    {"id": 1, "chassi": 12332156, "cor": "branco", "modelo": "Fox",
        "marca": "Volkswagem", "placa": "ABC-4321", "ano": 2014, "cod_categoria": 2},
]

categoria_List = [
    {"id": 0, "cod_categoria": 4, "descricao": "Carro de Luxo", "vlr_diaria": 100},
    {"id": 1, "cod_categoria": 2, "descricao": "Carro casual", "vlr_diaria": 60},
]

manutencao_List = [
    {"id": 0, "chassi_carro": 12332123, "cod_oficina": 3454, "date": 12082001,
        "desc_manutencao": "Troca de óleo", "vlr_manutencao": 100},
    {"id": 1, "chassi_carro": 12332123, "cod_oficina": 4565, "date": 12082001,
        "desc_manutencao": "Troca de peça lateral", "vlr_manutencao": 400},
]

oficina_list = [
    {"id": 0, "cod_oficina": 3454, "nome": "Oficina 1"},
    {"id": 1, "cod_oficina": 4565, "nome": "Oficina 3"},
]
