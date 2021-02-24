import database.db as db
from datetime import datetime
from sqlalchemy import extract
from models.Usuario import Usuario
from models.Medicion import Medicion
from config import bot

def step_2_registro_signos(message, pas, pad, fc, peso, fecha_toma):

    #print(pas)
    #print(pad)
    #print(fc)
    #print(peso)
    #print(fecha_toma)

    if message.text == "1":

        #Registro de medicion al id del chat del usuario    
        #Formateo de la fecha en string a objeto datetime
        date_time_obj = datetime.strptime(fecha_toma, '%Y-%m-%d %H:%M:%S')
        medicion = Medicion(message.from_user.id, pas, pad, fc, peso, date_time_obj)
    
        db.session.add(medicion)    
        db.session.commit()

        bot.send_message(message.chat.id,"*Datos registrados con exito.*",parse_mode="Markdown")
    elif message.text == "2":
        bot.reply_to(message, f"Proceso cancelado por el usuario.")
    else:
        bot.reply_to(message, f"Comando no reconocido, inicie el proceso nuevamente.")

##################################################################################################
# La confirmación de la eliminación de la medición.-SK
def step_2_eliminar_signos(message, index):
    signo = db.session.query(Medicion).get(index)

    print(signo.id)

    #Confirmacion positiva de eliminar
    if message.text == "1":
        db.session.delete(signo)
        db.session.commit()

        bot.send_message(message.chat.id,"*Registro eliminado con éxito.*",parse_mode="Markdown")
    elif message.text == "2":
        bot.reply_to(message, f"Proceso cancelado por el usuario.")
    else:
        bot.reply_to(message, f"Comando no reconocido, inicie el proceso nuevamente.")

######################################################################################################
