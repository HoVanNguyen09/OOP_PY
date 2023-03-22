class dog:
    legs = 4
    place = 'America'
    color = ['Black', 'Yello', 'White']

# __init__  là phương thức khởi tạo của tất cả các lớp hàm, 
# củng mật định và chường trình được bảo mật khá tốt vì người dùng
# cuối không thể nhận biết chương trình của chúng ta, hàm nào tạo ra
# từ phương thức này sẽ tự động được gọi.Bắt cứ __init__ đều phải 
# có tham số self rồi mới đến tham số khác, self ám chỉ đối tượng đã được gọi

    def __init__(self, name):
        self.name = name

# tạo đối tượng "pug"
pug = dog("bug")

print(pug.name)
print(pug.legs)
print(pug.place)
print(pug.color)