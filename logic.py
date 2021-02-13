import database.db as db
from datetime import datetime
from sqlalchemy import extract
from models.Usuario import Usuario

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

def get_paciente (documento):
    usuario = db.session.query(Usuario).get(documento)
    db.session.commit()
    
    if not usuario:
        return None
    
    return usuario

def set_paciente(documento, nombreCompleto): 
    usuario = Usuario(documento, nombreCompleto)
    
    db.session.add(usuario)    
    db.session.commit()

    return True