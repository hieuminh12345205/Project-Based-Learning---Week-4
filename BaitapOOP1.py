class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def display_info(self):
        print(f"Tên sách: {self.title}")
        print(f"Tác giả: {self.author}")
        print(f"Năm xuất bản: {self.year}")
        print("-" * 40)


# Tạo các đối tượng Book
book1 = Book("Người Thầy Đáng Kính", "Nguyễn Nhật Ánh", 1992)
book2 = Book("Những Đứa Con Trong Gia Đình Tôi", "Nguyễn Ngọc Tư.", 2018)

# Hiển thị thông tin sách
print("Thông tin sách:")
book1.display_info()
book2.display_info()