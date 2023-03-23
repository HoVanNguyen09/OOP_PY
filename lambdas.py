# Lambda gọi là hàm ẩn không có tên không có def.
num = lambda x: x**2
print(num(2))

# Ngắn gọn đỡ phải hơn cách viết def, kết quả ra đều giống nhau
def num(x):
  print(x**2)
num(4)

# note: lambda có bao nhiêu đối số củng được nhưng chỉ có duy nhất một hàm

#===========================================================
# hàm lambda kết hợp với hàm filter. Hàm lambda lấy 1 đối số là x
# một biểu thức là (x % 2) == 0, trong danh sách lists(thêm s) sử dụng
# filter để lọc và đưa nó vào một list mới
lists = [1, 2, 3, 4, 5, 6]
new_list = list(filter(lambda x: (x % 2==0), lists))
print(new_list)

# Sử dụng map, map trả về danh sách
lists = [1, 2, 3, 4, 5, 6]
new_list = list(map(lambda x: (x * 2), lists))
print(new_list)


#"---ƯU ĐIÊM---#
# KHI SỬ DỤNG HÀM LAMBDA: GIÚP CHƯƠNG TRÌNH TRỞ NÊN NGẮN GỌN DO ĐÓ NÓ 
# TRỞ NÊN LÀ MỘT PHƯƠNG PHÁP GIÚP TỐI ƯU CODE RẤT TỐT VÀ NÓ THƯỜNG ĐƯỢC
# SỬ DỤNG KHI XỬ LÝ CÁI LOGIC Ở TRONG CÁI CHƯƠNG TRÌNH CỦA CHÚNG TA Ở MỘT
# KHOẢNG THỜI GIẮN NHẮN NHẤT ĐỊNH NÀO ĐÓ

#---NHƯỢC ĐIỂM---#
# CÚ PHÁP CÓ VẼ PHỨC TẠP VÀ RẤT KHÓ CHO VIỆC PHẤT HIỆN VÀ XỮA LỖI.
