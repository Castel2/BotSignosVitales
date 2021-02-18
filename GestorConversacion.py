import database.db as db
from datetime import datetime
from sqlalchemy import extract
from models.Usuario import Usuario

#########################################################
# Mensaje de bienvenida e inicio al bot
def get_welcome_message(ASISTENTE_VIRTUAL,COMPANIA_SIGNOS):
    response = (
            f"Hola, soy *{ASISTENTE_VIRTUAL}* el asistente virtual de *{COMPANIA_SIGNOS}* "
            f"y quiero ayudarte con el registro y/o consulta de los signos vitales.\n\n"
            "¡Recuerda que nuestra comunicación debe ser por texto !"
        )
    return response

#########################################################
#Lógica de validación de existencia de usuario registrado en el bot
def get_validacion_paciente(user_id_telegram, nombre_user,COMPANIA_SIGNOS):
    usuario = db.session.query(Usuario).get(user_id_telegram)
    db.session.commit()

    if not usuario:
        response = (
            f"*{nombre_user}*, hemos identificado que no estás registrado en el sistema.\n\n"
            f"*{COMPANIA_SIGNOS}* te brinda la bienvenida y para guiarte en el registro de tus signos vitales, " 
            f"escribe tu número de identificación (sin puntos o comas).\n\n" 
            
            "¡Usa el comando: registrar paciente !"
        )
    else:
        response = (
             f"*{nombre_user}*, bienvenido y quiero ayudarte con el registro de tus signos vitales. \n\n"

              "¡Por favor escriba el comando para registrar o consultar sus datos !"
        )
    return response

    
#########################################################
# Lógica de registro del ID del usuario de telegram a la base de datos
'''
def register_account(user_id):
    account = db.session.query(Account).get(user_id)
    db.session.commit()

    if account == None:
        account = Account(user_id, 0)
        db.session.add(account)
        db.session.commit()
        return True

    return False
'''
##################################################################################################
# Mensaje del Comando “HELP”  
def get_help():
    response = (
        "Estos son los comandos disponibles:\n"
        "\n"
        "*/start* - Inicio de la interacción con el bot\n\n"
        "*/help* - Muestra este mensaje de ayuda\n\n"
        "*/about* - Muestra detalles de esta aplicación y su equipo de desarrollo\n\n"
        "*registrar paciente|rp {documento} {nombre completo}* - para registro de paciente\n\n"
        "*registrar signos|rs {Presión arterial sistólica} {presión arterial diastólica} {frecuencia cardiaca, peso (kg)} {fecha (dd-mm-aaaa)} {hora (hh--mm AM/PM)}* - Para registro de signos vitales\n\n"
        "*consultar signos|cs {Fecha inicial (dd-mm-aaaa)} {Fecha Final (dd-mm-aaaa)}* - para consultar sus signos registrados\n\n"
        "*eliminar signos|es {número de la medición}* - eliminar medición, se recomienda consultar la medición para conocer su númeración\n\n"
        "*consultar pacientes|cp {documento} {Fecha inicial (dd-mm-aaaa)} {Fecha Final (dd-mm-aaaa)}* - para realizar esta consulta debe estar habilitado como medico en nuestro sistema, permite consultar datos de pacientes \n\n"
        "*ingresar observaciones|io {número de la medición} {observación asociada}* - permite a asociar una observación a una medición registrada por un paciente, funcionalidad solo disponible para medicos autorizados\n\n"
        )

    return response

 
##################################################################################################
# Mensaje del Comando “ABOUT”  
def get_about(VERSION):
    response = (
        f"Bot Registro Signos Vitales (pyTelegramBot) v*{VERSION}*"
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
# Mensaje del Comando “FALLBACK”
def get_fallback_message (text,nombrePaciente,COMPANIA_SIGNOS):
    response = (
            f"\U0001F912 *{nombrePaciente}*, el comando o instrucción registrada no se identifica, "
            f"revisa e intenta nuevamente.\n\n"
            f"En *{COMPANIA_SIGNOS}* te acompañamos en el camino a tu bienestar, si requieres ayuda en cualquier "
            f"momento puedes ejecutar el comando /help"
   
        )
   
    return response

def get_registro_signos (nombrePaciente, pas, pad, fc, peso, fecha_toma):
    response = (
            f"\U0001F912 *{nombrePaciente}*, los datos registrados son: \n\n"
            f"Presión arterial sistólica: {pas} mmHg\n"
            f"Presión arterial diastólica: {pad} mmHg\n"
            f"Frecuencia cardiaca: {fc} latidos por minuto\n"
            f"Peso: {peso} kg\n"
            f"Fecha y Hora de toma: {fecha_toma}\n"
            f"\n"
            f"*1.* Guardar\n"
            f"*2.* Cancelar\n"
        )
   
    return response

def get_signo_eliminar (nombrePaciente, id_medicion, pas, pad, fc, peso, fecha_toma, fecha_registro):
    response = (
            f"\U0001F4C6 *Fecha y Hora del registro: {fecha_registro}*\n\n"
            f"  *{nombrePaciente}*, los datos de la medicion con *ID: {id_medicion}*\n\n"
            f"  Presión arterial sistólica: {pas} mmHg\n"
            f"  Presión arterial diastólica: {pad} mmHg\n"
            f"  Frecuencia cardiaca: {fc} latidos por minuto\n"
            f"  Peso: {peso} kg\n"
            f"  Fecha y Hora de toma: {fecha_toma}\n\n"
            
            f"\U000026A0¿Desea eliminar la medición?\n\n"
            f"*1.* Eliminar\n"
            f"*2.* Cancelar\n"
        )
   
    return response