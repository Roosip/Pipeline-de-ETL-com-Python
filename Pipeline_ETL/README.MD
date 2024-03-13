# Projeto de Geração de Mensagens Personalizadas em Python

---

## Descrição
Este projeto em Python é uma aplicação simples feita de acordo com o desafio de código da Digital Inovation One no Santander Dev Week 2023, que consiste na geração de mensagens personalizadas para usuários com base em dados fornecidos em um arquivo CSV e em um arquivo JSON. A aplicação extrai os IDs dos usuários de um arquivo CSV, busca informações detalhadas sobre esses usuários em um arquivo JSON e gera mensagens personalizadas para cada usuário. As mensagens geradas são então adicionadas a um arquivo JSON de histórico.

## Funcionalidades
- Extração dos IDs dos usuários de um arquivo CSV.
- Busca de informações detalhadas sobre os usuários em um arquivo JSON.
- Geração de mensagens personalizadas para cada usuário.
- Armazenamento das mensagens geradas em um arquivo JSON de histórico.

## Tecnologias Utilizadas
- Python
- Pandas
- JSON

## Como Usar
1. Certifique-se de ter o Python instalado em seu sistema.
2. Instale as dependências necessárias usando o comando:
    ```
    pip install pandas
    ```
3. Execute o script Python 'generate_messages.py' para iniciar o processo de geração de mensagens:
    ```
    python generate_messages.py
    ```

## Estrutura do Projeto
- **generate_messages.py**: O script principal responsável pela execução do projeto.
- **SDW2023.csv**: O arquivo CSV contendo os IDs dos usuários.
- **ids.json**: O arquivo JSON contendo informações detalhadas sobre os usuários.
- **mensagens.json**: O arquivo JSON onde as mensagens geradas são armazenadas.

## Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue para discutir sobre novas funcionalidades ou enviar um pull request com melhorias.

## Licença
Este projeto é licenciado sob a Licença MIT.
