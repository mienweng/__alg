import random

def monte_carlo_integral(func, x_range, y_range, z_range, num_samples):
    """
    使用蒙地卡羅方法計算三重積分
    :param func: 被積函數
    :param x_range: x 的範圍 (a, b)
    :param y_range: y 的範圍 (a, b)
    :param z_range: z 的範圍 (a, b)
    :param num_samples: 隨機樣本數
    :return: 積分結果
    """
    x_start, x_end = x_range
    y_start, y_end = y_range
    z_start, z_end = z_range

    volume = (x_end - x_start) * (y_end - y_start) * (z_end - z_start)
    total = 0

    for _ in range(num_samples):
        x = random.uniform(x_start, x_end)
        y = random.uniform(y_start, y_end)
        z = random.uniform(z_start, z_end)
        total += func(x, y, z)

    return total * volume / num_samples

# 計算積分
result_monte_carlo = monte_carlo_integral(function, (0, 1), (0, 1), (0, 1), num_samples=100000)
print("蒙地卡羅積分結果:", result_monte_carlo)
