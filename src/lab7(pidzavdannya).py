def rabin_karp(text: str, pattern: str, base: int = 256, prime: int = 101) -> bool:
    m, n = len(pattern), len(text)
    if m > n:
        return False

    pattern_hash = 0
    text_hash = 0
    h = 1

    for _ in range(m - 1):
        h = (h * base) % prime

    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime

    for i in range(n - m + 1):
        if pattern_hash == text_hash and text[i:i + m] == pattern:
            return True
        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if text_hash < 0:
                text_hash += prime

    return False


def main():
    input_file = "c:/IT/lab7.2semestr/bus_routes_ukraine.csv"
    output_file_from = "routes_from_Lviv_rk.txt"
    output_file_to = "routes_to_Lviv_rk.txt"

    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    routes_from_lviv = []
    routes_to_lviv = []

    for line in lines:
        parts = line.strip().split(",")
        if len(parts) != 3:
            continue
        from_city, to_city, _ = parts
        if rabin_karp(from_city, "Львів"):
            routes_from_lviv.append(line)
        if rabin_karp(to_city, "Львів"):
            routes_to_lviv.append(line)

    with open(output_file_from, "w", encoding="utf-8") as file:
        file.writelines(routes_from_lviv)

    with open(output_file_to, "w", encoding="utf-8") as file:
        file.writelines(routes_to_lviv)

    print(f"{len(routes_from_lviv)} маршрути з Львова у {output_file_from}")
    print(f"{len(routes_to_lviv)} маршрути до Львова у {output_file_to}")


if __name__ == "__main__":
    main()
