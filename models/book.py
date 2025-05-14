class Book:
    id_counter = 1

    def __init__(self, title, author, total_copies, id=None, available_copies=None):
        if id is None:
            self.id = str(Book.id_counter)
            Book.id_counter += 1
        else:
            self.id = str(id)
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = available_copies if available_copies is not None else total_copies

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "total_copies": self.total_copies,
            "available_copies": self.available_copies
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            author=data["author"],
            total_copies=data["total_copies"],
            available_copies=data.get("available_copies", data["total_copies"]),
            id=data["id"]
        )
