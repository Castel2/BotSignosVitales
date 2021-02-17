import database.db as db
from datetime import datetime
from sqlalchemy import extract
from models.Usuario import Usuario


##################################################################################################
# Eliminar signos”   
def remove_earning (user_id, index):
    record = db.session.query(Earning).filter(
    Earning.accounts_id == user_id
    ).filter(
    Earning.id == index
    ).first()
    
    if not record:
    control = update_account(user_id, record.amount * -1)
    if not control:
    db.session.rollback()
    return False
    db.session.delete(record)
    db.session.commit()
    return True
######################################################################################################