import pymongo 
#from pymongo import MongoClientclient = MongoClient()

# Conectar ao MongoDB
client = pymongo.MongoClient('mongodb+srv://teste:teste@cluster0.s8d6d.mongodb.net/sample_training?retryWrites=true&w=majority')

db = client['senac']

# Criar uma coleção para os contatos
contacts_collection = db['contacts']

# Função para criar um novo contato
def create_contact(name, phone_numbers):
    new_contact = {"name": name, "phone_numbers": phone_numbers}
    contacts_collection.insert_one(new_contact)
    print("Contato criado com sucesso!")

# Função para criar vários contatos de uma vez
def create_multiple_contacts(contacts):
    contacts_collection.insert_many(contacts)
    print("Contatos criados com sucesso!")

# Função para ler um contato
def read_contact(name):
    contact = contacts_collection.find_one({"name": name})
    if contact:
        print(f"Nome: {contact['name']}, Telefones: {', '.join(contact['phone_numbers'])}")
    else:
        print("Contato não encontrado.")

# Função para ler todos os contatos
def read_contacts():
    contacts = contacts_collection.find()
    if contacts:
        for contact in contacts:
            print(f"Nome: {contact['name']}, Telefones: {', '.join(contact['phone_numbers'])}")
    else:
        print("Nenhum contato encontrado.")

# Função para atualizar os telefones de um contato
def update_contact_phone_numbers(name, new_phone_numbers):
    contacts_collection.update_one({"name": name}, {"$set": {"phone_numbers": new_phone_numbers}})
    print("Telefones do contato atualizados com sucesso!")

# Função para deletar um contato
def delete_contact(name):
    contacts_collection.delete_one({"name": name})
    print("Contato deletado com sucesso!")

# Exemplo de uso
if __name__ == "__main__":
    # Criar alguns contatos de exemplo
    create_contact("João", ["123456789", "987654321"])
    create_contact("Maria", ["111222333", "444555666"])

    # Ler todos os contatos
    print("\nTodos os contatos:")
    read_contacts()

    # Atualizar telefones do contato
    update_contact_phone_numbers("João", ["999999999"])

    # Deletar um contato
    delete_contact("Maria")

    # Ler todos os contatos após as alterações
    print("\nTodos os contatos após alterações:")
    read_contacts()
