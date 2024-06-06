import requests
import time

# Configurações - cole aqui os seus dados
GITHUB_TOKEN = 'seu_token_aqui'  # Substitua pelo seu token
REPO_OWNER = 'nome_do_dono_do_repositorio'  # Substitua pelo nome do dono do repositório
REPO_NAME = ['nome_do_repositorio_1', 'nome_do_repositorio_2']  # Substitua pelo nome do repositório
DISCORD_WEBHOOK_URL = 'sua_webhook_url_aqui'  # Substitua pela URL do seu Webhook do Discord
CHECK_INTERVAL = 60  # Intervalo de tempo em segundos para verificar novos PRs

# Cabeçalhos para autenticação
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def get_pull_requests(i):
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME[i]}/pulls'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Erro ao acessar a API do GitHub: {response.status_code}')
        return []

def send_discord_message(pr):
    data = {
        "content": f"**Novo Pull Request encontrado:**\n"
                   f"**Título:** {pr['title']}\n"
                   f"**Autor:** {pr['user']['login']}\n"
                   f"**URL:** {pr['html_url']}\n"
                   f"**Descrição:** {pr['body']}"
    }
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print("Mensagem enviada ao Discord com sucesso!")
    else:
        print(f"Falha ao enviar mensagem ao Discord: {response.status_code}, {response.content}")

def print_pr_info(pr):
    print(f"Novo Pull Request encontrado:")
    print(f"Título: {pr['title']}")
    print(f"Autor: {pr['user']['login']}")
    print(f"Descrição: {pr['body']}")
    print('-' * 80)
    send_discord_message(pr)

def main():
    active = {
        "content": "Monitorando Pull Requests no repositório..."
    }
    print("Monitorando Pull Requests no repositório...")
    response = requests.post(DISCORD_WEBHOOK_URL, json=active)
    if response.status_code == 204:
        print("Mensagem enviada ao Discord com sucesso!")
    else:
        print(f"Falha ao enviar mensagem ao Discord: {response.status_code}, {response.content}")
    processed_prs = set()

    while True:
        for i in range(0, len(REPO_NAME)):
            prs = get_pull_requests(i)
            for pr in prs:
                if pr['id'] not in processed_prs:
                    print_pr_info(pr)
                    processed_prs.add(pr['id'])
        time.sleep(CHECK_INTERVAL)

if __name__ == '__main__':
    main()
