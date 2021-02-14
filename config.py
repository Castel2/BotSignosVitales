import telebot
import logging
from decouple import config

#########################################################
# Versión del bot
VERSION = 0.1

# Nombre del asistente virtual del bot de signos vitales que lo guiara durante su interacción
ASISTENTE_VIRTUAL = 'Yoda'

# Nombre de la compañia de signos vitales para pacientes hipertensos
COMPANIA_SIGNOS = 'Vidalan'

# Obtiene el token desde el archivo de configuración

TELEGRAM_TOKEN = config('TELEGRAM_TOKEN')

#########################################################
# Crea el objeto bot utilizando el token

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Determina el nivel de los mensajes que se van a mostrar (debug)

telebot.logger.setLevel(logging.INFO)
#########################################################