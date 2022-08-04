from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import json
from List import *

class Cliente(Resource):
    def get(self, id):
        try:
            res = Cliente_list[id]
        except IndexError:
            res = {'status': 'error', 'message': 'Cliente not found'}
        except Exception:
            res = {'status': 'error', 'message': 'Unexpected error'}
        return(res)

    def put(self):
        dados = json.loads(request.data)
        Cliente_list[id] = dados
        return jsonify(dados)

    def delete(self):
        Cliente_list.pop(id)
        return({"status": "ok"})


class NewClientList(Resource):
    def get(self):
        return(Cliente_list)

    def post(self):
        dados = json.loads(request.data)
        position = len(Cliente_list)
        dados['id'] = position
        Cliente_list.append(dados)
        return (Cliente_list[position])

class Alocacao(Resource):
    def get(self, id):
        try:
            res = Alocacao_List[id]
        except IndexError:
            res = {'status': 'error', 'message': 'alocacao not found'}
        except Exception:
            res = {'status': 'error', 'message': 'Unexpected error'}
        return(res)

    def put(self):
        dados = json.loads(request.data)
        Alocacao_List[id] = dados
        return jsonify(dados)

    def delete(self):
        Alocacao_List.pop(id)
        return({"status": "ok"})

class NewAlocacaoList(Resource):
    def get(self):
        return(Alocacao_List)

    def post(self):
        dados = json.loads(request.data)
        position = len(Alocacao_List)
        dados['id'] = position
        Alocacao_List.append(dados)
        return (Alocacao_List[position])

class Carro(Resource):
    def get(self, id):
        try:
            res = Carro_List[id]
        except IndexError:
            res = {'status': 'error', 'message': 'Carro not found'}
        except Exception:
            res = {'status': 'error', 'message': 'Unexpected error'}
        return(res)

    def put(self):
        dados = json.loads(request.data)
        Carro_List[id] = dados
        return jsonify(dados)

    def delete(self):
        Carro_List.pop(id)
        return({"status": "ok"})

class NewCarroList(Resource):
    def get(self):
        return(Carro_List)

    def post(self):
        dados = json.loads(request.data)
        position = len(Carro_List)
        dados['id'] = position
        Carro_List.append(dados)
        return (Carro_List[position])

class Categoria(Resource):
    def get(self, id):
        try:
            res = categoria_List[id]
        except IndexError:
            res = {'status': 'error', 'message': 'Categoria not found'}
        except Exception:
            res = {'status': 'error', 'message': 'Unexpected error'}
        return(res)

    def put(self):
        dados = json.loads(request.data)
        categoria_List[id] = dados
        return jsonify(dados)

    def delete(self):
        categoria_List.pop(id)
        return({"status": "ok"})

class NewCategoriaList(Resource): 
    def get(self):
        return(categoria_List)

    def post(self):
        dados = json.loads(request.data)
        position = len(categoria_List)
        dados['id'] = position
        categoria_List.append(dados)
        return (categoria_List[position])

class Manutencao(Resource):
    def get(self, id):
        try:
            res = manutencao_List[id]
        except IndexError:
            res = {'status': 'error', 'message': 'Manutenção not found'}
        except Exception:
            res = {'status': 'error', 'message': 'Unexpected error'}
        return(res)

    def put(self):
        dados = json.loads(request.data)
        manutencao_List[id] = dados
        return jsonify(dados)

    def delete(self):
        manutencao_List.pop(id)
        return({"status": "ok"})

class NewManutencaoList(Resource):
    def get(self):
        return(manutencao_List)

    def post(self):
        dados = json.loads(request.data)
        position = len(manutencao_List)
        dados['id'] = position
        manutencao_List.append(dados)
        return (manutencao_List[position])

class Oficina(Resource):
    def get(self, id):
        try:
            res = oficina_list[id]
        except IndexError:
            res = {'status': 'error', 'message': 'Manutenção not found'}
        except Exception:
            res = {'status': 'error', 'message': 'Unexpected error'}
        return(res)

    def put(self):
        dados = json.loads(request.data)
        oficina_list[id] = dados
        return jsonify(dados)

    def delete(self):
        oficina_list.pop(id)
        return({"status": "ok"})

class NewOficinaList(Resource):
    def get(self):
        return(oficina_list)

    def post(self):
        dados = json.loads(request.data)
        position = len(oficina_list)
        dados['id'] = position
        oficina_list.append(dados)
        return (oficina_list[position])