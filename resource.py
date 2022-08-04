from app import *

app = Flask(__name__)
api = Api(app)


api.add_resource(Cliente, '/client/<int:id>/')
api.add_resource(NewClientList, '/client/')
api.add_resource(Alocacao, '/alocacao/<int:id>/')
api.add_resource(NewAlocacaoList, '/alocacao/')
api.add_resource(Carro, '/carro/<int:id>/')
api.add_resource(NewCarroList, '/carro/')
api.add_resource(Categoria, '/categoria/<int:id>/')
api.add_resource(NewCategoriaList, '/categoria/')
api.add_resource(Manutencao, '/manutencao/<int:id>/')
api.add_resource(NewManutencaoList, '/manutencao/')
api.add_resource(Oficina, '/oficina/<int:id>/')
api.add_resource(NewOficinaList, '/oficina/')

if __name__ == '__main__':
    app.run(debug=True)
