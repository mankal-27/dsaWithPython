def floor_log2(n: int) -> int:
    """ Floor of log base 2 (for n >= 1)"""
    if n <= 0:
        raise ValueError("n must be positive")
    result = 0
    while n > 1:
        n >>= 1
        result +=1
    return result

def count_digits(n: int) -> int:
    """ Number of decimal digits in n for (n >= 1) """
    if n <= 0:
        raise ValueError("n must be positive")
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

def count_bits(n: int) -> int:
    """ Number of buts needed to represent n (for n>= 1) """
    if n <= 0:
        raise ValueError("n must be positive")
    return floor_log2(n) + 1

if __name__ == "__main__":
    print(f"floor_log2(16) = {floor_log2(16)}")      # 4
    print(f"floor_log2(100) = {floor_log2(100)}")     # 6
    print(f"count_digits(5000) = {count_digits(5000)}")  # 4
    print(f"count_bits(13) = {count_bits(13)}")        # 4
    print(f"count_bits(16) = {count_bits(16)}")        # 5