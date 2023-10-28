# Discord.py Bot Template

Este é um template para criar um bot Discord usando discord.py, com suporte para comandos em slash, prefixo, híbridos, eventos, componentes, alguns comandos já prontos para começar e exemplos para ajudá-lo a começar.

## Sumário

1. [Introdução](#discordpy-bot-template)
2. [Instalação](#instalação)
   - [Clone ou Download](#clone-ou-download)
3. [Configuração](#configuração)
   - [Token Bot](#token-bot)
   - [Convite do Bot](#convite-do-bot)
   - [Arquivo `.env`](#arquivo-env)
4. [Dependências](#dependências)
5. [Licença](#licença)

## Instalação

Clone o repositório usando `git clone` ou faça o download

- Você pode usar o seguinte comando para clonar:
```bash
git clone https://github.com/Nanyuss/Discord.py-Bot-Template.git
```
- Fazer o Download do repositório no botão verde com o nome `<> code`, `Download Zip` e Extrair com o seu `Explorador de Arquivos`

## Configuração

Antes de executar o bot, você precisará configurar seu bot do Discord e seu arquivo `.env`.

### Token Bot

  - Crie sua aplicação no [Portal do Desenvolvedor](https://discord.com/developers/applications)
  - Na sua aplicação vá na seção "Bot" e Pegue o Token do bot

> **Atenção**: Nunca compartilhe esse token com ninguém. Em caso de vazamento, redefina-o o mais rápido possível. Mantenha o token em sigilo para manter a segurança do seu bot Discord.

### Convite do Bot

Para adicionar o bot ao seu servidor Discord, acesse o [Portal do Desenvolvedor](https://discord.com/developers/applications), selecione o seu aplicativo, vá para a seção "OAuth2", "URL Generator", selecione os escopos `bot, applications.commands`, defina as permissões e adicione o bot ao servidor a partir daí.

Certifique-se de que seu bot Discord esteja configurado corretamente e tenha as permissões adequadas antes de adicioná-lo ao servidor.

### Arquivo `.env`

Certifique-se de substituir `PREFIXO_DO_SEU_BOT` pelo prefixo que você deseja atribuir ao seu bot, `TOKEN_SEU_BOT` pelo token do seu bot Discord e `ID_DO_BOT` pelo ID do seu bot Discord. 

```
PREFIX = PREFIXO_DO_SEU_BOT
TOKEN = TOKEN_SEU_BOT
BOT_ID = ID_DO_BOT
```
> **Atenção**: Mantenha o arquivo `.env` em sigilo para garantir a segurança do seu bot.

## Dependências 

Você pode instalar as dependências iniciais de duas maneiras.

1. Instalando uma por uma:
  ```
  pip install discord.py
  pip install python-decouple
  ```
2. Todas que estão no `requirements.txt`:
  ```
  pip install -r requirements.txt
  ```

## Licença

Este projeto é licenciado sob a [GNU General Public License (GPL)](LICENSE). A GPL é uma licença de código aberto que garante a liberdade de uso, modificação e distribuição do software, desde que quaisquer modificações ou extensões também sejam disponibilizadas sob os termos da GPL.

Certifique-se de ler e entender completamente os termos da licença GPL antes de utilizar ou contribuir para este projeto. Você pode encontrar mais informações sobre a GPL em [https://www.gnu.org/licenses/gpl-3.0.en.html](https://www.gnu.org/licenses/gpl-3.0.en.html).

Consulte o arquivo [LICENSE](LICENSE) para obter o texto completo da licença GPL.
