from datetime import datetime
from models.transaction import Transaction
from utils.helpers import load_data, save_data
from services.book_service import BookService


class TransactionService:
    @staticmethod
    def borrow_book(user_id, book_id):
        data = load_data()

        book = next((b for b in data["books"] if b["id"] == book_id), None)
        if not book or int(book["available_copies"]) <= 0:
            print("Kitap mevcut değil.")
            return None

        book["available_copies"] -= 1

        # Gerekli parametrelerle Transaction nesnesi oluştur
        action = "borrow"
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = Transaction(user_id, book_id, action, date)

        data["transactions"].append(transaction.to_dict())
        save_data(data)

        print(f"Kitap başarıyla ödünç alındı. (İşlem ID: {transaction.id})")
        return transaction

    @staticmethod
    def return_book(transaction_id):
        data = load_data()
        for transaction in data["transactions"]:
            if transaction["id"] == transaction_id and transaction.get("action") == "borrow":
                # Kitap kopyasını geri ekle
                for b in data["books"]:
                    if b["id"] == transaction["book_id"]:
                        b["available_copies"] += 1

                # Yeni bir "return" işlemi olarak kaydet
                return_tx = Transaction(
                    user_id=transaction["user_id"],
                    book_id=transaction["book_id"],
                    action="return",
                    date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )
                data["transactions"].append(return_tx.to_dict())
                save_data(data)
                print(f"Kitap başarıyla geri verildi. (İşlem ID: {return_tx.id})")
                return return_tx
        print("Geçerli işlem bulunamadı.")
        return None
