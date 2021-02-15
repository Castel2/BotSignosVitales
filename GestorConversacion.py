from config import bot
import config
from time import sleep
import re
import database.db as db

import logic

#########################################################
if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
#########################################################

# Comando de Inicio del bot
@bot.message_handler(commands=['start'])
def on_command_start(message):
    bot.send_chat_action(message.chat.id, 'typing')

    print (message.from_user)

    bot.send_message (
        message.chat.id,
        logic.get_welcome_message(config.ASISTENTE_VIRTUAL,config.COMPANIA_SIGNOS),
        parse_mode="Markdown")
    
    bot.send_message (
        message.chat.id,
        logic.get_help(),
        parse_mode="Markdown")
    
    #logic.register_account(message.from_user.id)

#########################################################

@bot.message_handler(commands=['help'])
def on_command_help(message):
    bot.send_chat_action(message.chat.id, 'typing')
    
    bot.send_message(
        message.chat.id,
        logic.get_help(),
        parse_mode="Markdown")

@bot.message_handler(commands=['about'])
def on_command_about(message):
    pass


@bot.message_handler(regexp=r"^(registrar signos|rs)$")
def on_get_balance(message):
    pass

@bot.message_handler(regexp=r"^(registrar paciente|rp) ([0-9]*) ([a-zA-Z ]*)$")
def on_get_balance(message):
    bot.send_chat_action(message.chat.id, 'typing')

    parts = re.match(r"^(registrar paciente|rp) ([0-9]*) ([a-zA-Z ]*)$",message.text)
        
    #print(parts[2])
    #print(parts[3])

    documento = int(parts[2])
    nombreCompleto = parts[3]

    usuario = logic.get_paciente(documento)
    if usuario == None:
        #Usuario no existente se procede al registro
        logic.set_paciente(documento, nombreCompleto)
        bot.reply_to(message, f"Paciente registrado.")
    else:
        bot.reply_to(message, f"Paciente ya registrado.")
    


@bot.message_handler(regexp=r"^(consultar signos|cs)$")
def on_earn_money(message):
    pass

@bot.message_handler(regexp=r"^(eliminar signos|es)$")
def on_spend_money(message):
    pass

@bot.message_handler(regexp=r"^(consultar pacientes|cp)$")
def on_list_earnings(message):
    pass

@bot.message_handler(regexp=r"^(ingresar observaciones|io)$")
def on_remove_record(message):
    pass
#############################################################################################
# Mensaje por defecto que procesa los demás mensajes que coincidan 
# con los comandos ingresados por el usuario

@bot.message_handler(func=lambda message: True)
def on_fallback(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1) 

    response = logic.get_fallback_message (message.text, message.from_user.first_name, config.COMPANIA_SIGNOS)
    bot.reply_to(message, response, parse_mode="Markdown")

#########################################################

if __name__ == '__main__':
    bot.polling(timeout=1)
#########################################################
