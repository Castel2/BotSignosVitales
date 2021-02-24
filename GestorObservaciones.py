import database.db as db
from datetime import datetime
from sqlalchemy import extract
from models.Observacion import Observacion
from config import bot


##################################################################################################
# La confirmación de la eliminación de la medición.-SK
def step_2_Registrar_observacion(message, idMedicion, id_user_tel, observacion):

    observacion = Observacion(idMedicion, id_user_tel, observacion)
    #Confirmacion positiva de registro
    if message.text == "1":
        db.session.add(observacion)
        db.session.commit()

        bot.send_message(message.chat.id,"*Observación añadida con éxito.*",parse_mode="Markdown")
    elif message.text == "2":
        bot.reply_to(message, f"Proceso cancelado por el usuario.")
    else:
        bot.reply_to(message, f"Comando no reconocido, inicie el proceso nuevamente.")
####################################################################################################