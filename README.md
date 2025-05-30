![image](https://github.com/user-attachments/assets/3e677703-c32a-4774-925d-dd26d29aa7c6)
![image](https://github.com/user-attachments/assets/c53898ed-b988-44bb-8ea9-bf3a7a698d11)

# Kütüphane Otomasyon Sistemi

## Özellikler

* **Kullanıcı Kimlik Doğrulama:** Üye ve Yönetici olmak üzere iki farklı rol için güvenli giriş sistemi.
* **Kullanıcı Kayıt:** Yeni üyelerin doğrudan giriş ekranından kolayca kayıt olabilmesi.
* **Kullanıcı Yönetimi (Admin):**
    * Sistemdeki tüm kullanıcıları listeleme ve arama.
    * Mevcut kullanıcı bilgilerini (ad, e-posta, şifre, kullanıcı tipi) güncelleme.
    * Kullanıcıları silme.
* **Kitap Yönetimi (Admin):**
    * Yeni kitap ekleme.
    * Kütüphanedeki tüm kitapları listeleme ve arama.
* **Kitap Ödünç Alma/İade Etme:**
    * Kullanıcıların kitap ödünç alması.
    * Ödünç alınan kitapların iade edilmesi.
    * Bir kullanıcının ödünç aldığı kitapları takip etme.
* **Veri Kalıcılığı:** Tüm kullanıcı, kitap ve işlem verileri, uygulama kapatıldığında bile kalıcı depolama için `database.json` dosyasında saklanır.
* **Modüler Mimari:** Proje, Model-Service-UI katmanlarına ayrılmış, okunabilir ve bakımı kolay bir yapıya sahiptir.

## Kullanılan Teknolojiler

* **Python 3.x**
* **CustomTkinter:** Modern ve özelleştirilebilir bir masaüstü GUI kütüphanesi.
* **JSON:** Veri depolama formatı olarak kullanılır.

## Kurulum

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

1.  **Projeyi Klonlayın:**
    ```bash
    git clone [https://github.com/KULLANICI_ADINIZ/proje_adi.git](https://github.com/KULLANICI_ADINIZ/proje_adi.git)
    cd proje_adi
    ```
    (Buradaki `KULLANICI_ADINIZ` ve `proje_adi` kısımlarını kendi GitHub kullanıcı adınız ve projenizin adıyla değiştirin.)

2.  **Gerekli Kütüphaneleri Yükleyin:**
    ```bash
    pip install customtkinter
    ```
## Çalıştırma

Projeyi çalıştırmak için `main.py` dosyasını çalıştırın:

```bash
python main.py
