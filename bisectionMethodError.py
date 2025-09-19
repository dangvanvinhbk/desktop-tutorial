import math

def bisection_n_and_x(f, a, b, epsilon):
    """
    Trả về (n, x_n) với n là số bước lặp nhỏ nhất sao cho
        (b - a) / 2^(n+1) <= epsilon
    và x_n là nghiệm gần đúng thu được sau đúng n bước chia đôi.

    f: hàm số f(x)
    a, b: khoảng [a,b] với f(a)*f(b) < 0
    epsilon: sai số mong muốn (>0)
    """
    if epsilon <= 0:
        raise ValueError("epsilon phải > 0")
    if f(a) * f(b) >= 0:
        raise ValueError("Điều kiện f(a)*f(b) < 0 không thỏa trên [a,b]")

    # Tính n nhỏ nhất từ cận sai số lý thuyết: (b-a)/2^(n+1) <= epsilon
    raw = math.log2((b - a) / epsilon) - 1
    n = max(0, math.ceil(raw))

    # Thực hiện đúng n bước chia đôi để lấy x_n
    x = (a + b) / 2.0  # phòng khi n = 0
    for _ in range(n):
        x = (a + b) / 2.0
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
    # x_n là trung điểm cuối cùng
    x_n = (a + b) / 2.0
    return n, x_n
