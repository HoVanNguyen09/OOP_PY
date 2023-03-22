# Tạo class có tên Foo
class Foo:

    # Truyền vào thuộc tính có tên Foo, và những thuộc tính này tên có
    #  2 dấu gạch dưới ở đầu và cuối điều này có nghĩa thuộc tính này trở
    # thành thuộc tính ẩn (private) 
    __name__ = "Foo"

    # Tạo hàm khởi tạo
    def __getName(self):
        print(self.__name__)

    def get(self):
        self.__getName()

print(Foo.__getName.__name__)
Foo().__getName
Foo().get()
