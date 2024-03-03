# Nono my telegram bot assistant

The aims of this toy project are :

- discover the design and deployment of telegram bot
- experiment hexgonal architecture
- have fun in pyhton
- discover github actions to build and deploy the bot

## Features

Telegram bot can be able to :

- [ ] send jokes
- [ ] get somes documents from nexcloud
- [ ] generate menu to control bot's actions

## Setup project

```powershell
py -m pip install -r requirements.txt
```

## Roadmap

Do a tiny bot to experiment bot design :

- [x] Design a tiny bot quickely and send text
- [x] Call an API to send joke
- [x] Experiment the nexcloud API to find documents
- [ ] Refacto the tiny bot in hexagonal architecture
- [ ] Refacto the handler to :
  - [ ] send joke
  - [ ] send documents : search and get document, get last report, get folders contents
  - [ ] send menu

## Resources

### python-telegram-bot repositories of samples :

- https://stackoverflow.com/questions/71860197/deploy-telegram-bot-pyrogram-on-back4app
- https://github.com/python-telegram-bot/python-telegram-bot/tree/master/examples
- https://github.com/jojo786/Sample-Python-Telegram-Bot-AWS-Serverless
- https://github.com/jojo786/-Sample-Python-Telegram-Bot-AWS-Serverless-PTBv20
- https://github.com/jojo786/TelegramTasweerBot/tree/main
- https://github.com/ets-labs/python-dependency-injector/blob/master/examples/miniapps/movie-lister/movies/entities.py
- https://github.com/PyGithub/PyGithub/blob/main/doc/examples/Authentication.rst
- https://github.com/PyGithub/PyGithub/blob/main/doc/examples/Repository.rst

### nextcloud API :

https://github.com/cloud-py-api/nc_py_api/blob/main/examples/as_client/files/find.py
