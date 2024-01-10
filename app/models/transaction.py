from pydantic import BaseModel, root_validator


class Transaction(BaseModel):
    sender_id: int | None
    recipient_id: int | None
    amount_in_cents: int

    @root_validator
    def validate_content(cls, values):
        if values.get("sender_id") == values.get("recipient_id"):
            raise ValueError("Cannot send money to yourself...")
        elif values.get("amount_in_cents") <= 0:
            raise ValueError("Amount is negative or zero, does not make any sense..")
        return values


if __name__ == "__main__":
    t = Transaction(amount_in_cents=0)
    t = Transaction(amount_in_cents=-1)
    print(t)
