from pydantic import BaseModel


class Transaction(BaseModel):
    sender_id: int
    recipient_id: int
    amount_in_cents: int