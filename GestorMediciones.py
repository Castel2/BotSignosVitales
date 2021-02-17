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

def get_paciente (documento):

    pass


##################################################################################################
# Mensaje del Comando “ABOUT”   
def get_about(VERSION):
    response = (
        f"Bot Registro Signos Vitales (pyTelegramBot) v{VERSION}"
        "\n\n"
        "Desarrollado por los estudiantes de la Especializacion de Ingeniería de Software de la Universidad Autónoma de Manizales:\n\n"
        "   Hector Daniel Cardona <hectord.cardonal@autonoma.edu.co>\n"
        "   Yordan Castelblanco<yordan.castelblancoj@autonoma.edu.co> \n"
        "   Juan Alberto Vidal <juana.vidalg@autonoma.edu.co> \n"
        "   Elan Fco. Perea <elanf.pereaa@autonoma.edu.co> \n\n"

        "2021"
    )
    return response

######################################################################################################
