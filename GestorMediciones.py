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
# Eliminar signos”  PARA CONSULTAR  -SK
def eliminar_signos_consulta(user_id, index):

    #se guarda la consulta en la variable signo
    signo = db.session.query(Medicion).filter(
    Medicion.id_user_tel == user_id
    ).filter(
    Medicion.id == index
    ).first()

    #si no hay nada en signos
    if not signo:
        db.session.rollback()
        return None
    
    #Si hay un registro en signos
    return signo

# La confirmación de la eliminación de la medición.-SK
def eliminar_signos(message, index):
    signo = db.session.query(Medicion).get(index)

    print(signo.id)

    #Confirmacion positiva de eliminar
    if message.text == "1":
        db.session.delete(signo)
        db.session.commit()

        bot.send_message(message.chat.id,"*Registro eliminado con exito.*",parse_mode="Markdown")
    elif message.text == "2":
        bot.reply_to(message, f"Proceso cancelado por el usuario.")
    else:
        bot.reply_to(message, f"Comando no reconocido, inicie el proceso nuevamente.")

# saber si un usuario es medico -sk
def permiso_medico (user_id):
    #se guarda la consulta en la variable consulta
    consulta = db.session.query(Usuario).filter(
    Usuario.id_user_tel == user_id
    ).filter(
    Usuario.tipoUsuario == 2
    ).first()

    #si no hay nada en la consulta
    if not consulta:
        return False
    
    #si tiene el permiso 
    return True

######################################################################################################
