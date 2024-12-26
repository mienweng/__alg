def riemann_integral(func, x_range, y_range, z_range, n):
    """
    使用黎曼積分計算三重積分
    :param func: 被積函數
    :param x_range: x 的範圍 (a, b)
    :param y_range: y 的範圍 (a, b)
    :param z_range: z 的範圍 (a, b)
    :param n: 分割數 (對每個變數)
    :return: 積分結果
    """
    x_start, x_end = x_range
    y_start, y_end = y_range
    z_start, z_end = z_range

    dx = (x_end - x_start) / n
    dy = (y_end - y_start) / n
    dz = (z_end - z_start) / n

    total = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                x = x_start + (i + 0.5) * dx
                y = y_start + (j + 0.5) * dy
                z = z_start + (k + 0.5) * dz
                total += func(x, y, z) * dx * dy * dz

    return total

# 被積函數
def function(x, y, z):
    return 3 * x**2 + y**2 + 2 * z**2

# 計算積分
result_riemann = riemann_integral(function, (0, 1), (0, 1), (0, 1), n=100)
print("黎曼積分結果:", result_riemann)
