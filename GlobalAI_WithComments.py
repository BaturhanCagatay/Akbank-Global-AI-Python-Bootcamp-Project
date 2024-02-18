class Library():

    def __init__(self,file_name = "books.txt"): 
        self.file_name = file_name
    """Sinifin örneklerini başlatir. Bu kodlar, bir kütüphane temsil etmek için temel bir çerçeve sağlar. Genel yapisal özelliklerini tanimlar. 
    """

    def add_book(self):
        title = input("Enter Book's Title: ")
        author = input("Enter Book's Author: ")
        release_year = input("Enter Book's Release Year: ")
        num_pages = input("Enter Book's Number Pages: ")
        price = input("Enter Book's Price: ")
        publishing_house = input("Enter Book's Publishing House: ")
        with open(self.file_name , 'a+') as file :
            file.write(f"{title},{author},{release_year},{num_pages},{price},{publishing_house}\n")
        print("The book has been added to our library")
    """(*) Kitap eklemek için başlik, yazar, basim yili, sayfa sayisi, deger ve basim evi olarak degerleri alir. Bu sirada dosyanin açilmasi için 'a+' metodu kullanilir.
    (*) 'a+' dosya açma modu, dosyayi hem okuma hem de yazma için açar. İlk önce dosyayi sonuna ekler (append) ve dosyanin başlangicina gitmez. Eğer dosya yoksa, oluşturulur. Eğer dosya varsa, dosyanin sonundan itibaren yazma yapilabilir.
    (*) Islem yapildiği zaman bilgiyi kullaniciya bilgi verilir.
    """

    def remove_book(self):
        deleting_title = input("Which book should we delete from our library?")
        found = False
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
        
        with open(self.file_name, 'w') as file:
            for line in lines:
                if not line.startswith(deleting_title):
                    file.write(line)
                else:
                    found=True
        if found:
            print("Book removed successfully!")
        else:
            print("Book not found in the list!")
    """(*) Kullanicidan silmek için kitap adini aldiktan sonra dosyayi satir satir okuduktan sonra silindikten sonra kalan kitaplari tekrar dosyaya yazar. 
    (*) startswith() yöntemi, bir dize objesinin belirtilen bir önek ile başlayip başlamadiğinistartswith() yöntemi, bir dize objesinin belirtilen bir önek ile başlayip başlamadiğini kontrol eder. Örneğin, str.startswith(prefix) şeklinde kullanilir, burada str kontrol edilecek olan dizeyi temsil ederken, prefix ise başlangiç önekini temsil eder. Eğer dize belirtilen önek ile başliyorsa True değerini döndürür, aksi halde False döner. kontrol eder. Örneğin, str.startswith(prefix) şeklinde kullanılır, burada str kontrol edilecek olan dizeyi temsil ederken, prefix ise başlangiç önekini temsil eder. 
    Eğer dize belirtilen önek ile başliyorsa True değerini döndürür, aksi halde False döner.
    """

    def list_books(self):
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    book_info = line.strip().split(',')
                    print(f"Book's Name : {book_info[0]} | Book's Author : {book_info[1]} | Book's Release Year : {book_info[2]} | Book's Number Pages : {book_info[3]} | Book's Price : {book_info[4]} | Book's Publishing House : {book_info[5]}")
        except IOError as e:
            print("An error occurred while reading the file:", e)
        except IndexError as e:
            print("An error occurred while parsing the file. Make sure each line has all the required fields:", e)
    
    """(*) Dosya açildiktan sonra satir satir çekiliyor, ve bu satirler bilgilerine göre parse edilir. Edilen ifadeler ekrana bastirilir.
    (*)Dosya okuma sirasinda bir hata oluşursa (IOError), kullaniciya bir hata mesaji gösterir.
    (*)Dosyadaki herhangi bir satirin işlenmesi sirasinda bir dize dizin hatasi oluşursa (IndexError), kullaniciya bir hata mesaji gösterir ve işlemi devam ettirir.
    """

    def search_book(self):
        query = input("Enter title or author to search: ")
        found = False
        with open(self.file_name, 'r') as file:
            for line in file:
                book_info = line.strip().split(',')
                if query.lower() in [info.lower() for info in book_info[:2]]:
                    print(f"Book found: {line}")
                    found = True
        if not found:
            print("Book not found in the library.")
    """(*)Search yapabilmek için kullanicidan alinan isme göre dosya tekrardan satir satir çekildikten sonra ya ad ya da yazar adi ile ayni mi diye kontrol edip ekrana bastirir."""

    def update_price(self):
        title = input("Enter the title of the book to update price: ")
        new_price = input("Enter the new price: ")
        found = False
        updated_lines = []
        with open(self.file_name, 'r') as file:
            for line in file:
                if title in line:
                    line_parts = line.strip().split(',')
                    line_parts[-2] = new_price  # Assuming price is the second to last item
                    line = ','.join(line_parts) + '\n'
                    found = True
                updated_lines.append(line)

        with open(self.file_name, 'w') as file:
            file.writelines(updated_lines)

        if found:
            print("Price updated successfully!")
        else:
            print("Book not found in the library.")
    """
    1-Kullanicidan güncellenmesi istenen kitabin adini (title) ve yeni fiyati (new_price) alir.
    2-Eğer güncellenmesi istenen kitap bulunursa, o satiri virgülle ayrilmiş parçalara (line_parts) ayirir ve fiyati günceller.
    3-Güncellenmiş satiri birleştirir ve updated_lines listesine ekler.
    4-Güncellenmiş satiri birleştirir ve updated_lines listesine ekler.
    """

    def count_books(self):
        count = 0
        with open(self.file_name, 'r') as file:
            for _ in file:
                count += 1
        print(f"Total number of books in the library: {count}")
    """
    1- Sistem içindeki satir sayisina göre kitap sayisini ekliyoruz.
    """


import os 
def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
   



def main():
    lib = Library()
    while True:
        print("*** MENU ***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("4) Update Price")
        print("5) Search Book")
        print("6) Count Books")
        print("7) Exit")
        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == '1':
            lib.list_books()
        elif choice == '2':
            lib.add_book()
        elif choice == '3':
            lib.remove_book()
        elif choice == '4':
            lib.update_price()
        elif choice == '5':
            lib.search_book()
        elif choice == '6':
            lib.count_books()
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter again.")
        
        # Wait for user input before clearing the screen
        input("Press enter to continue")
        clear_screen()     
        
        """
        Klasik Menü Tasarimi
        """

if __name__ == "__main__":
    main()

"""
** "Betik" terimi genellikle betik dillerinde yazilmiş olan küçük, otomatize edilmiş görevleri ifade etmek için kullanilir. 
Bir betik, belirli bir görevi gerçekleştirmek için bir dizi komut veya talimat içeren metin tabanli bir dosyadir.**  
**Betiğin doğrudan çaliştirilmasi durumunda main() fonksiyonunun çağrilmasini sağlar. Bu şekilde, betik dosyasi bir modül olarak başka bir betikte 
içe aktarildiğinda main() fonksiyonu otomatik olarak çağrilmaz, bu da modülerlik ve yeniden kullanilabilirlik sağlar. 
Bu tip bir yapi, bir betik dosyasini bir modül olarak kullanmak istediğinizde main() fonksiyonunu çağirmadan betiği içe aktarmanizi sağlar"""