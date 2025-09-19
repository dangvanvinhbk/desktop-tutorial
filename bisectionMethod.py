def bisectionMethod(f, a, b, n):
    """
    Giải gần đúng f(x) = 0 trên [a,b] theo phương pháp chia đôi.
    Trả về nghiệm gần đúng x_n sau n bước lặp.

    f : hàm số f(x)
    a, b : khoảng [a,b], cần thỏa f(a)*f(b) < 0
    n : số bước lặp
    """
    if f(a) * f(b) >= 0:
        raise ValueError("Điều kiện f(a)*f(b) < 0 không thỏa")

    print(f"Bước đầu: a_0 = {a}, b_0 = {b}")

    for i in range(n):
        x = (a + b) / 2  # Điểm chính giữa
        print(f"Bước {i + 1}: x_{i + 1} = {x:.6f}")

        if f(a) * f(x) < 0:
            b = x
        else:
            a = x

        print(f"         a_{i + 1} = {a:.6f}, b_{i + 1} = {b:.6f}")

    # Nghiệm cuối cùng là trung bình cộng của a_n và b_n
    final_solution = (a + b) / 2
    print(f"\nNghiệm gần đúng = (a_{n} + b_{n})/2 = ({a:.6f} + {b:.6f})/2 = {final_solution:.6f}")

    return final_solution
