from services.user_service import UserService
from services.book_service import BookService
from services.transaction_service import TransactionService
from utils.helpers import load_data, update_counters

data = load_data()
update_counters(data)

def main():
    print("📚 Kütüphane Yönetim Sistemine Hoşgeldiniz")

    while True:
        print("\n1. Kullanıcı Ekle")
        print("2. Kitap Ekle")
        print("3. Kitapları Listele")
        print("4. Kitap Ödünç Al")
        print("5. Kitap Geri Ver")
        print("6. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            name = input("Ad: ")
            email = input("E-mail: ")
            user_type = input("Tip (admin/member): ")
            user = UserService.add_user(name, email, user_type)
            print("✅ Kullanıcı eklendi:", user.name)

        elif choice == "2":
            title = input("Kitap adı: ")
            author = input("Yazar: ")
            total = int(input("Adet: "))
            book = BookService.add_book(title, author, total)
            print("✅ Kitap eklendi:", book.title)

        elif choice == "3":
            books = BookService.list_books()
            

        elif choice == "4":
            BookService.list_books()  # Önce kitapları listele
            user_id = input("Kullanıcı ID: ")
            book_id = input("Kitap ID: ")
            tx = TransactionService.borrow_book(user_id, book_id)
            if tx:
                print("✅ Kitap ödünç alındı.")
            else:
                print("❌ Kitap ödünç alınamadı.")

        elif choice == "5":
            tx_id = input("İşlem (transaction) ID: ")
            result = TransactionService.return_book(tx_id)
            if result:
                print("✅ Kitap iade edildi.")
            else:
                print("❌ Geçersiz işlem.")

        elif choice == "6":
            print("Çıkılıyor...")
            break

        else:
            print("❌ Geçersiz seçim!")

if __name__ == "__main__":
    main()
