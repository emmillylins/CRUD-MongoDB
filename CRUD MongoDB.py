import pymongo
from pymongo import MongoClient
client = MongoClient()

# Conectar ao banco de dados
client = pymongo.MongoClient('mongodb+srv://teste:teste@cluster0.s8d6d.mongodb.net/sample_training?retryWrites=true&w=majority')
db = client['senac']

# Definir a coleção
contacts = db['contacts']

# Função para criar um novo contato
def create_contact(name, number):
    new_contact = {"name": name, "number": number}   
    result = contacts.insert_one(new_contact)
    print("Contato criado: {}".format(result.inserted_id))

# Função para buscar um contato pelo nome
def find_contact_by_name(name):
    contact = contacts.find_one({"name": name})
    if contact:
        print("Contato encontrado:")
        print(contact)
    else:
        print("Contato não encontrado.")

# Função para listar todos os contatos
def list_contacts():
    contacts = contacts.find()
    print("Lista de contatos:")
    for contact in contacts:
        print(contact)

# Função para atualizar o telefone de um contato
def update_contact_number(name, new_number):
    contacts.update_one({"name": name}, {"$set": {"number": new_number}})
    print("Telefone do contato atualizado com sucesso!")

# Função para deletar um contato pelo número
def delete_contact_by_number(number):
    contacts.delete_one({"number": number})
    print("Contato excluído com sucesso!")

# Exemplos de uso

# Criar contatos
create_contact("João", "123456789")
create_contact("Maria", "987654321")

# Buscar contato pelo nome
find_contact_by_name("João")

# Listar todos os contatos
list_contacts()

# Atualizar telefone de um contato
update_contact_number("Maria", "999999999")

# Deletar um contato pelo nome
delete_contact_by_number("123456789")
