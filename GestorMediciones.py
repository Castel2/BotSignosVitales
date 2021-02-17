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
# Eliminar signos”   
def eliminar_signo (user_id, index):
    record = db.session.query(Medicion).filter(
    Medicion.id_user_tel == user_id
    ).filter(
    Medicion.id == index
    ).first()
    
    print(record)

    '''
    if not record:
        control = update_account(user_id, record.amount * -1)
    if not control:
        db.session.rollback()
    return False
    db.session.delete(record)
    db.session.commit()
    '''
    return True
######################################################################################################
