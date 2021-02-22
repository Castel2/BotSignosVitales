from config import bot
import config
from time import sleep
import re
import database.db as db

import GestorConsultas
import GestorConversacion
import GestorMediciones
import GestorObservaciones
import GestorPacientes

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
        GestorConversacion.get_welcome_message(config.ASISTENTE_VIRTUAL,config.COMPANIA_SIGNOS),
        parse_mode="Markdown")
    
    #Mensaje de bienvenida donde valida si el usuario usa el bot y el tipo de perfil (Paciente o médico)
    bot.send_message (
        message.chat.id,
        GestorConversacion.get_validacion_paciente(message.from_user.id,message.from_user.first_name,
            config.COMPANIA_SIGNOS),
        parse_mode="Markdown")  
    
    
#########################################################
# Comando de ayuda para los usuarios del bot

@bot.message_handler(commands=['help'])
def on_command_help(message):
    bot.send_chat_action(message.chat.id, 'typing')
    
    bot.send_message(
        message.chat.id,
        GestorConversacion.get_help(),
        parse_mode="Markdown")

@bot.message_handler(commands=['about'])
def on_command_about(message):
    bot.send_chat_action(message.chat.id, 'typing')
    
    bot.send_message(
        message.chat.id,
        GestorConversacion.get_about(config.VERSION),
        parse_mode="Markdown")

#########################################################
# Comando para registrar los signos vitales el usuario en el cual debe registrar:
'''
Presión arterial sistólica
Presión arterial diastólica
Frecuencia cardiaca
Peso
Fecha y Hora de toma
'''
@bot.message_handler(regexp=r"^(registrar signos|rs) ([0-9]*) ([0-9]*) ([0-9]*) ([0-9]*[.]?[0-9]*) ([0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]))$")
def on_set_signos(message):
    bot.send_chat_action(message.chat.id, 'typing')

    parts = re.match(r"^(registrar signos|rs) ([0-9]*) ([0-9]*) ([0-9]*) ([0-9]*[.]?[0-9]*) ([0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]))$",message.text)
        
    #print(parts[2])
    #print(parts[3])
    #print(parts[4])
    #print(parts[5])
    #print(parts[6])

    pas = int(parts[2])
    pad = int(parts[3])
    fc = int(parts[4])
    peso = float(parts[5])
    fecha_toma = parts[6]

    bot.send_message(
            message.chat.id,
            GestorConversacion.get_registro_signos(message.chat.first_name + " " + message.chat.last_name, pas, pad, fc, peso, fecha_toma),
            parse_mode="Markdown")

    bot.register_next_step_handler(message, GestorMediciones.step_2_registro_signos, pas, pad, fc, peso, fecha_toma)

#########################################################
# Comando para registrar pacientes donde solo debe colocar el número de identificación sin comas y puntos

@bot.message_handler(regexp=r"^(registrar paciente|rp) ([0-9]*)$")
def on_set_paciente(message):
    bot.send_chat_action(message.chat.id, 'typing')

    parts = re.match(r"^(registrar paciente|rp) ([0-9]*)$", message.text)        

    documento = int(parts[2])

    usuario = GestorPacientes.get_paciente(documento)
    if usuario == None:
        #Usuario no existente se procede al registro
        GestorPacientes.set_paciente(message.from_user.id, documento, message.chat.first_name + " " + message.chat.last_name, 1)
        bot.reply_to(message, f"Paciente registrado.")
    else:
        bot.reply_to(message, f"Paciente ya registrado.")

#########################################################
# Comando para eliminar los signos vitales 
  
@bot.message_handler(regexp=r"^(eliminar signos|es) ([0-9]+)$")
def on_delete_signos(message):
    #se particiona el mensaje
    parts = re.match(r"^(eliminar signos|es) ([0-9]+)$", message.text, flags=re.IGNORECASE)

    #se guarda el id del usuario y id de la medicion
    id_usuario = int(message.from_user.id)
    id_medicion = int(parts[2])

    #Se llama la funcion que consulta en la base de datos las mediciones. 
    signo_borrar = GestorMediciones.eliminar_signos_consulta(id_usuario,id_medicion)
    
    #Si el paciente no está registrado
    if not GestorPacientes.existencia_paciente(id_usuario):
        bot.reply_to(message, f"\U0001F614 *{message.from_user.first_name}*, no puedes implementar este comando, ya que no esta registrado.", parse_mode="Markdown")

        return bot.send_message (
        message.chat.id,
        GestorConversacion.get_validacion_paciente(message.from_user.id,message.from_user.first_name, config.COMPANIA_SIGNOS),
        parse_mode="Markdown")  
    
    if not signo_borrar:
        return bot.reply_to(message, 
        f"\U0001F928 *{message.from_user.first_name}*, "
        f"No has regitrado signos con el id: {id_medicion}\n\n" "Verifica e intenta nuevamente, puedes usar el comando:\n\n"
        "*consultar signos|cs {Fecha inicial (dd-mm-aaaa)} {Fecha Final (dd-mm-aaaa)}* - para consultar sus signos registrados"
        ,parse_mode="Markdown")    
    
    #Mostar Signo a Eliminar y solicitar confimacion de eliminacion
    bot.send_message(message.chat.id,
    GestorConversacion.get_signo_eliminar (
    message.chat.first_name + " " + message.chat.last_name, 
    signo_borrar.id,
    signo_borrar.pas, 
    signo_borrar.pad, 
    signo_borrar.fc, 
    signo_borrar.peso, 
    signo_borrar.fecha_toma,
    signo_borrar.fecha_registro),
    parse_mode="Markdown")

    #Recibir confirmacion de elminiacion y ejecutar la acción
    bot.register_next_step_handler(message, GestorMediciones.eliminar_signos, signo_borrar.id)
 

#########################################################
# Comando para comnsultar mis signos vitales, recibe dos fechas como parametros inicial y final respectivamente en formato yyyy-mm-dd
      
@bot.message_handler(regexp=r"^(consultar signos|cs) ([0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])) ([0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]))$")
def on_get_signos(message):
    bot.send_chat_action(message.chat.id, 'typing')
    id_usuario = int(message.from_user.id)
    # Antes de realizar las operaciones se valida que el usuario este registrado
    if GestorPacientes.existencia_paciente(id_usuario):
        text = message.chat.first_name
        parts = re.match(r"^(consultar signos|cs) ([0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])) ([0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]))$", message.text, flags=re.IGNORECASE)
        fecha_inicial = parts[2]
        fecha_final = parts[5]
        signos = GestorConsultas.get_signos(message.from_user.id, fecha_inicial, fecha_final) 
        # En caso de que el usuario este registrado pero no tenga registros de signos vitales se le mostrara un mensaje
        if signos is None:
            bot.reply_to(message, "No existe registro de signos para el usuario " + text + "\n\n", parse_mode="Markdown")
        else:
            text = "``` Listado de los signos del usuario: " + text + "\n\n"
            text += f"| ID | Sistolica | Diastolica | F.Cardiaca | Peso |\n"
            for sv in signos:
                text += f"| {sv.id}  | {sv.pas}       | {sv.pad}         | {sv.fc}         | {sv.peso} |\n"
            text += "```"
            bot.reply_to(message, text, parse_mode="Markdown")
    else:
        bot.send_message (
            message.chat.id,
            GestorConversacion.get_validacion_paciente(message.from_user.id,message.from_user.first_name, config.COMPANIA_SIGNOS),parse_mode="Markdown")

@bot.message_handler(regexp=r"^(consultar pacientes|cp)$")
def on_get_paciente(message):
    pass

############################################################################################################
#Funcino para que los medicos puedan revisar las mediciones de un paciente en un determinado tiempo -sk
@bot.message_handler(regexp=r"^(listar registros pacientes|lrp) ([0-9]+) ([0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])) ([0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]))$")
def on_get_resgistro_paciente(message):
    bot.send_chat_action(message.chat.id, 'typing')

    bot.reply_to(message,"te esceché fuerte  y claro sk",parse_mode="Markdown")

#############################################################################################
@bot.message_handler(regexp=r"^(ingresar observaciones|io)$")
def on_set_observaciones(message):
    pass
#############################################################################################
# Mensaje por defecto que procesa los demás mensajes que coincidan 
# con los comandos ingresados por el usuario

@bot.message_handler(func=lambda message: True)
def on_fallback(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1) 

    response = GestorConversacion.get_fallback_message (message.text, message.from_user.first_name, config.COMPANIA_SIGNOS)
    bot.reply_to(message, response, parse_mode="Markdown")

#########################################################

if __name__ == '__main__':
    bot.polling(timeout=1)
#########################################################

