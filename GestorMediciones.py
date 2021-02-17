import database.db as db
from datetime import datetime
from sqlalchemy import extract
from models.Usuario import Usuario


##################################################################################################
# Mensaje del Comando “ABOUT”   
def on_delete_signos(id, ):
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