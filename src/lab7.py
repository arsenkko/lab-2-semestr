def rabin_karp(input_str: str, find_str: str) -> list[int]:
    if not find_str or not input_str or len(find_str) > len(input_str):
        return []

    base = 256
    prime = 101

    m = len(find_str)
    n = len(input_str)
    find_hash = 0
    current_hash = 0
    h = 1

    result = []


    for _ in range(m - 1):
        h = (h * base) % prime

    for i in range(m):
        find_hash = (base * find_hash + ord(find_str[i])) % prime
        current_hash = (base * current_hash + ord(input_str[i])) % prime

    for i in range(n - m + 1):
        if find_hash == current_hash:
            if input_str[i:i + m] == find_str:
                result.append(i)

        if i < n - m:
            current_hash = (base * (current_hash - ord(input_str[i]) * h) + ord(input_str[i + m])) % prime
            if current_hash < 0:
                current_hash += prime

    return result

#є список автобусних рейсів, зберігаються в текстовому файлі(точка відправки, точка прибуття, час в дорозі) треба вивести список рейсів де 1) початкова точка львів, 2) коли точка прибуття львів