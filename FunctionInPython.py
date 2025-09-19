def hello():
    print("Xin chào sinh viên ngành KHDL BK HCM!")
print("-" * 60)
print(hello())
def binhphuong(x):
    return x**2
print(f"hàm đơn giản:{binhphuong(4)}")
print("-" * 60)

f=lambda x: x**(1/5)
print(round(f(5),4))
print("-" * 60)
def add(a, b):
    return a + b
print(add(4,5))
print("-" * 60)

def greet(name="bạn"):
    return f"Xin chào, {name}"
print(greet("Lý Anh Quân"))

