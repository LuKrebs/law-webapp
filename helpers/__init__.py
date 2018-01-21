from laracunha import app, db
from sqlalchemy.sql import or_, and_, desc, asc

from home.models import History

def get_history(history_id=None):
    if not history_id:
        history = History.query.filter_by(active=True).order_by(desc(History.id)).first()
    else:
        history = History.query.filter(and_(History.active==True, History.id==history_id)).first()

    return history
