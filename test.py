# test.py
# 简单测试：计算 1 + 1

def add(a: int, b: int) -> int:
    """返回两个整数的和。"""
    return a + b


if __name__ == "__main__":
    result = add(1, 1)
    print(f"1 + 1 = {result}")