#!env/Scripts/python3
import logging
import time

from dependency_injector.wiring import Provide, inject
from telegram import ReplyKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import Application, ContextTypes, PrefixHandler
from nc_py_api import Nextcloud

from src.modules.configuration.containers import Container
from src.modules.entities.joke import Joke
from src.modules.infrastructure.data_provider.joke.joke_api_service import JokeApiService
from src.modules.infrastructure.entry_points.telegram.channel_message import ChannelMessage
from src.modules.infrastructure.entry_points.telegram.sender_message import SenderMessage

BOT_NAME='Nono'

reply_keyboard = [
  ["Blague", "Documents", "Evénements"],
  ["Quitter"],
]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
  await context.bot.send_message(
    chat_id=update.effective_chat.id,
    reply_to_message_id=update.message.message_id, 
    text=f'Salut {update.message.chat.first_name}, c\'est moi {BOT_NAME}',
    reply_markup=markup)
  return CHOOSING

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  await context.bot.send_message(
    chat_id=update.effective_chat.id,
    reply_to_message_id=update.message.message_id, 
    text=f'Salut {update.message.chat.first_name}, c\'est moi {BOT_NAME}')
  return
  
async def event(
    update: Update, 
    context: ContextTypes.DEFAULT_TYPE,
    nextcloud_api : Nextcloud = Provide[Container.nextcloud_api_service]) -> None:
  calendar = nextcloud_api.cal.principal()
  elmts = calendar.calendars()
  for elmt in elmts :
    print(elmt)

  

async def document(
    update: Update, 
    context: ContextTypes.DEFAULT_TYPE,
    nextcloud_api : Nextcloud = Provide[Container.nextcloud_api_service]) -> None:
  
  fileName="Sommaire"
  file = nextcloud_api.files.find(["like", "name", fileName], "Solaris")[0]
  #file = nextcloud_api.files.by_path("Solaris/1-Eau")

  #shared_links = filter(lambda file: fileName in file.full_path, )
  shared_links = nextcloud_api.files.sharing.get_list()

  # for link in shared_links :
  #   print(f'{link.path} {link.url}')
  shared = shared_links[1]
  print(f'path : {file.full_path}, label : {file.name}, is shared : {file.is_shared}, id: {file.file_id} info :{file.info}')
  print(f'shared : {shared.path} {shared.label}, id: {shared.share_id} url :{shared.url}, {shared.mimetype}')

  text = '' #f'<a href="{shared.url}">{shared.path}</a>'
  for link in shared_links :
    text += f'<a href="{link.url}">{link.path}</a>\n'
  
  await context.bot.send_message(
    chat_id=update.effective_chat.id,
    reply_to_message_id=update.message.message_id,
    text=text, 
    parse_mode=ParseMode.HTML, 
    disable_web_page_preview=True)

  await context.bot.send_document(
    chat_id=update.effective_chat.id,
    reply_to_message_id=update.message.message_id,
    document=open(shared_links[1].url, 'rb')
    #document=shared_links[1].url #'https://python-telegram-bot.org/static/testfiles/telegram.gif' 
  )
  return


@inject  
async def joke(
    update: Update, 
    context: ContextTypes.DEFAULT_TYPE,
    joke_api : JokeApiService = Provide[Container.joke_api_service],
  ) -> None:
  joke : Joke = await joke_api.get_joke()
  logging.info(f'blague : {joke.question} {joke.answer}')
  questionMessage = ChannelMessage(bot=context.bot, chat_id=update.message.chat_id, message_id=update.message.message_id, text=joke.question)
  answerMessage = ChannelMessage(bot=context.bot, chat_id=update.message.chat_id, message_id=update.message.message_id, text=joke.answer)
  await SenderMessage.send(questionMessage)
  time.sleep(2)
  await SenderMessage.send (answerMessage)
  return

@inject  
def main(
  bot : Application = Provide[Container.botApplication]) -> Application :
  bot.application.add_handler(PrefixHandler(f"@{BOT_NAME}", ":bonjour", start))
  bot.application.add_handler(PrefixHandler(f"@{BOT_NAME}", ":menu", menu))
  bot.application.add_handler(PrefixHandler(f"@{BOT_NAME}", ":event", event))

  bot.application.add_handler(PrefixHandler(f"@{BOT_NAME}", ":blague", joke))
  bot.application.add_handler(PrefixHandler(f"@{BOT_NAME}", ":document", document))
  return bot

if __name__=='__main__':
  container = Container()
  container.init_resources()
  container.wire(modules=[__name__])
  bot = main()
  bot.application.run_polling()