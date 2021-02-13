from config import bot
import config
from time import sleep
import re
import database.db as db

#########################################################
if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
#########################################################

@bot.message_handler(commands=['start'])
def on_command_start(message):
    pass

@bot.message_handler(commands=['help'])
def on_command_help(message):
    pass

@bot.message_handler(commands=['about'])
def on_command_about(message):
    pass


@bot.message_handler(regexp=r"^(registrar signos|rs)$")
def on_get_balance(message):
    pass

@bot.message_handler(regexp=r"^(registrar paciente|rp)$")
def on_get_balance(message):
    pass

@bot.message_handler(regexp=r"^(consultar signos|cs)$")
def on_earn_money(message):
    pass

@bot.message_handler(regexp=r"^(eliminar signos|es)$")
def on_spend_money(message):
    pass

@bot.message_handler(regexp=r"^(consultar pacientes|cp)$")
def on_list_earnings(message):
    pass

@bot.message_handler(regexp=r"^(listar registros|lr)$")
def on_list_spendings(message):
    pass

@bot.message_handler(regexp=r"^(ingresar observaciones|io)$")
def on_remove_record(message):
    pass

@bot.message_handler(regexp=r"^(listar cuentas|lc)$")
def on_list_accounts(message):
    pass


@bot.message_handler(func=lambda message: True)
def on_fallback(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    bot.reply_to(
        message,
        "\U0001F63F Ups, no entendí lo que me dijiste.")

#########################################################

if __name__ == '__main__':
    bot.polling(timeout=1)
#########################################################

