import pandas as pd
import json

# ESTRACT
# Lê o arquivo CSV 'SDW2023.csv' e armazena seus dados em um DataFrame do Pandas chamado df.
df = pd.read_csv('person_ids.csv')
# Extrai a coluna 'UserID' do DataFrame df e converte seus valores em uma lista, armazenada na variável user_ids.
user_ids = df['UserID'].tolist()


def get_user(id):
    # Define uma função chamada get_user que recebe um parâmetro id.
    with open('ids.json', 'r') as arquivo:
        # Abre o arquivo JSON 'ids.json' em modo de leitura ('r') e o associa à variável arquivo.
        # O uso do with garante que o arquivo será fechado automaticamente após seu uso.
        users_data = json.load(arquivo)
        # Carrega os dados do arquivo JSON arquivo em um objeto Python, armazenado na variável users_data.
    for user_data in users_data:
        # Itera sobre cada elemento do objeto users_data, que contém os dados dos usuários no formato JSON.
        if user_data['id'] == id:
            # Verifica se o ID do usuário atual (user_data['id']) é igual ao ID passado como argumento para a função (id).
            return user_data
            # Retorna os dados do usuário correspondente se o ID for encontrado no arquivo JSON.
    return None
    # Retorna None se o ID não for encontrado no arquivo JSON.

users = []
# Inicializa uma lista vazia chamada users para armazenar os dados dos usuários encontrados.
for id in user_ids:
    # Itera sobre cada ID de usuário na lista user_ids.
    user = get_user(id)
    # Chama a função get_user passando o ID atual e armazena o resultado na variável user.
    if user is not None:
        # Verifica se o resultado retornado da função get_user não é None.
        users.append(user)
        # Adiciona os dados do usuário à lista users se o usuário não for None.

# print(json.dumps(users, indent=2))


# TRANSFORM
import random

def generate_random_message(name):
    # Define uma função para gerar mensagens aleatórias com base no nome fornecido.
    messages = [
    f"Olá {name}, o mundo dos investimentos está cheio de oportunidades esperando por você. Vamos começar?",
    f"Não espere mais, {name}! Comece a investir hoje e construa um amanhã próspero.",
    f"Seja inteligente com seu dinheiro, {name}. Invista agora e colha os frutos no futuro!",
    f"Você sabia, {name}, que investir pode ser mais fácil do que parece? Vamos descobrir juntos!",
    f"Invista com sabedoria, {name}. O futuro é uma página em branco esperando pela sua história.",
    f"{name}, o momento para investir é agora! Não deixe para depois o que pode te trazer prosperidade hoje.",
    f"Não perca tempo, {name}! Comece a investir e construa a vida dos seus sonhos.",
    f"Seu futuro começa hoje, {name}. Invista agora e garanta uma aposentadoria tranquila.",
    f"Você já parou para pensar, {name}, que o dinheiro pode trabalhar para você? Vamos fazer isso acontecer!",
    f"{name}, não subestime o poder dos investimentos. Eles podem transformar sua vida!",
    f"Invista com inteligência, {name}, e colha os frutos de um futuro financeiro sólido.",
    f"Não deixe para depois, {name}! Comece a investir agora e conquiste seus objetivos.",
    f"{name}, a vida é feita de escolhas. Escolha investir no seu futuro e garanta tranquilidade.",
    f"Invista com estratégia, {name}, e veja seu patrimônio crescer ao longo do tempo.",
    f"Você merece um futuro financeiro seguro, {name}. Invista hoje e realize seus sonhos!",
    f"{name}, o tempo está do seu lado. Comece a investir agora e aproveite os benefícios no futuro.",
    f"Acredite no poder dos investimentos, {name}. Eles podem mudar sua vida para melhor!",
    f"Não adie mais, {name}! Comece a investir agora e construa um futuro próspero.",
    f"Seu futuro financeiro está em suas mãos, {name}. Faça escolhas inteligentes e invista hoje!",
    f"Invista com confiança, {name}. O futuro é promissor para quem sabe aproveitar as oportunidades.",
    f"Não perca mais tempo, {name}! O momento para investir é agora.",
    f"{name}, sua jornada rumo à independência financeira começa com um simples passo: investir!",
    f"Faça seu dinheiro trabalhar por você, {name}. Comece a investir hoje mesmo!",
    f"O futuro é incerto, {name}, mas seus investimentos podem trazer estabilidade e segurança.",
    f"{name}, cada centavo investido hoje é uma semente plantada para um futuro próspero.",
]

    return random.choice(messages)
    # Retorna uma mensagem aleatória da lista de mensagens.

def generate_ai_news(user):
    # Define uma função para gerar notícias AI com base nos dados do usuário fornecidos.
    message = generate_random_message(user['name'])
    # Gera uma mensagem aleatória com base no nome do usuário.
    print(f"Gerando mensagem para {user['name']}: {message}")
    # Imprime a mensagem gerada para o usuário.
    news_item = {
        "id": user['id'],  
        # Mantém o mesmo ID da notícia
        "icon": "",
        "description": message
    }

    # Carregar mensagens existentes do arquivo JSON
    with open('mensagens.json', 'r') as json_file:
        existing_messages = json.load(json_file)

    existing_messages.append(news_item)

    # Salvar as mensagens atualizadas em um arquivo JSON
    with open('mensagens.json', 'w') as json_file:
        json.dump(existing_messages, json_file, indent=4)
        # Salva as mensagens atualizadas no arquivo JSON com indentação de 4 espaços.

# LOAD
for user in users:
    # Itera sobre cada usuário na lista de usuários.
    generate_ai_news(user)
    # Gera notícias AI para o usuário atual.

print("Mensagens geradas e salvas com sucesso no arquivo 'mensagens.json'!")
# Imprime uma mensagem indicando que as mensagens foram geradas e salvas com sucesso no arquivo JSON.
