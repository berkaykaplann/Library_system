class Transaction:
    id_counter = 1

    def __init__(self, user_id, book_id, action, date, id=None):
        if id is None:
            self.id = str(Transaction.id_counter)
            Transaction.id_counter += 1
        else:
            self.id = str(id)
        self.user_id = user_id
        self.book_id = book_id
        self.action = action  # "borrow" veya "return"
        self.date = date

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "book_id": self.book_id,
            "action": self.action,
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            user_id=data["user_id"],
            book_id=data["book_id"],
            action=data["action"],
            date=data["date"],
            id=data["id"]
        )
