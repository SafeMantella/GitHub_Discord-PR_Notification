# GitHub+Discord - PR Notification
# Monitoramento de Pull Requests no GitHub e Notificação no Discord

Este script Python monitora um repositório GitHub em busca de novos Pull Requests (PRs) e envia notificações para um canal do Discord utilizando Webhooks.

## Pré-requisitos

- Python 3.x
- Biblioteca `requests` instalada

## Instalação

1. **Clone o repositório ou copie o script para seu ambiente local.**

2. **Instale a biblioteca `requests` se ainda não estiver instalada:**
   ```bash
   pip install requests
   ```

3. **Crie um Personal Access Token (PAT) no GitHub:**
   - Vá para [GitHub Settings > Developer settings > Personal access tokens > Fine Grained Tokens]([https://github.com/settings/tokens?type=beta]).
   - Clique em "Generate new token".
   - Dê um nome ao token, selecione as permissões Read-Only `metadata` e `pull requests`.
   - Clique em "Generate token" e copie o token gerado.

4. **Crie um Webhook no Discord:**
   - Vá até o servidor do Discord onde deseja enviar as mensagens.
   - Vá até o canal onde deseja enviar as mensagens e clique no ícone de configurações do canal.
   - Clique na opção "Webhooks".
   - Clique em "Criar Webhook".
   - Dê um nome ao Webhook, selecione o canal desejado e clique em "Copiar URL do Webhook".

## Configuração

1. **Atualize o script com suas informações:**
   - Abra o arquivo do script.
   - Substitua `seu_token_aqui` pelo seu token de acesso pessoal do GitHub.
   - Substitua `nome_do_dono_do_repositorio` pelo nome do dono do repositório.
   - Substitua `nome_do_repositorio_1` pelo nome do repositório. Você pode adicionar mais repositórios na lista e o bot checará todos eles.
   - Substitua `sua_webhook_url_aqui` pela URL do seu Webhook do Discord.

### Exemplo de configuração:

```python
GITHUB_TOKEN = 'seu_token_aqui'  # Substitua pelo seu token
REPO_OWNER = 'nome_do_dono_do_repositorio'  # Substitua pelo nome do dono do repositório
REPO_NAME = ['nome_do_repositorio_1', 'nome_do_repositorio_2']  # Substitua pelo nome do repositório
DISCORD_WEBHOOK_URL = 'sua_webhook_url_aqui'  # Substitua pela URL do seu Webhook do Discord
```

## Uso

1. **Execute o script Python:**
   ```bash
   python bot.py
   ```

O script irá monitorar o repositório especificado em busca de novos Pull Requests. Quando um novo PR for detectado, uma mensagem com as informações do PR será enviada ao canal do Discord especificado.

## Observações

- O intervalo de verificação dos Pull Requests é definido pela variável `CHECK_INTERVAL` (em segundos). O valor padrão é 60 segundos, mas você pode alterar conforme seu gosto.
- Certifique-se de que o token de acesso pessoal do GitHub e a URL do Webhook do Discord sejam mantidos em segurança e não sejam compartilhados publicamente.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
