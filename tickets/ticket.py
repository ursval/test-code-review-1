from datetime import datetime

from tickets.app import db
from tickets.config import TICKET_STATUS_CLOSED, TICKET_STATUS_OPEN, TICKET_STATUS_ANSWERED, \
    TICKET_STATUS_WAITING_FOR_ANSWER


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(256), nullable=False)
    text = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(256), nullable=False)
    status = db.Column(db.String(16), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime)

    def __repr__(self):
        return '<Ticket id={} subject={}>'.format(self.id, self.subject)

    def to_dict(self):
        return {
            'id': self.id,
            'subject': self.subject,
            'text': self.text,
            'email': self.email,
            'status': self.status,
            'created_at': str(self.created_at) if self.created_at else None,
            'updated_at': str(self.updated_at) if self.updated_at else None,
        }


def ticket_status_is_valid(ticket, new_status):
    if ticket.status == TICKET_STATUS_CLOSED:
        return False

    result = (ticket.status == TICKET_STATUS_OPEN and new_status in (TICKET_STATUS_ANSWERED, TICKET_STATUS_CLOSED)) or\
             (ticket.status == TICKET_STATUS_ANSWERED and new_status in (TICKET_STATUS_CLOSED,
                                                                         TICKET_STATUS_WAITING_FOR_ANSWER))
    return result
