def sum_invalid_in_ranges(ranges, invalid_ids):
    """Given ranges and precomputed invalid IDs, compute the sum."""
    total = 0
    for r in ranges:
        lo, hi = map(int, r.split("-"))
        # binary search to get only invalid IDs inside this range
        for x in invalid_ids:
            if x < lo:
                continue
            if x > hi:
                break
            total += x
    return total


def day_2a_gift_shop_id_checker(filename):
    print(f"Processing {filename}...")
    with open(filename) as f:
        ranges = f.read().strip().split(",")
    invalid = []

    # Only repeated twice -> pattern length = half
    for length in range(2, 12):
        if length % 2 == 0:
            half = length // 2
            for i in range(10 ** (half - 1), 10 ** half):
                s = str(i) * 2
                invalid.append(int(s))

    invalid.sort()
    print(sum_invalid_in_ranges(ranges, invalid))


def day_2b_gift_shop_id_checker(filename, max_len=12):
    print(f"Processing {filename}...")

    with open(filename) as f:
        ranges = f.read().strip().split(",")
    invalid = set()

    for length in range(2, max_len + 1):
        for pat_len in range(1, length // 2 + 1):
            if length % pat_len != 0:
                continue
            repeats = length // pat_len

            # Pattern cannot start with 0 (leading zero invalid)
            for i in range(10 ** (pat_len - 1), 10 ** pat_len):
                s = str(i) * repeats
                invalid.add(int(s))
    invalid = sorted(invalid)

    print(sum_invalid_in_ranges(ranges, invalid))


if __name__ == "__main__":
    print("Part 1:")
    day_2a_gift_shop_id_checker("test_input.txt")
    day_2a_gift_shop_id_checker("input.txt")
    print("Part 2:")
    day_2b_gift_shop_id_checker("test_input.txt")
    day_2b_gift_shop_id_checker("input.txt")

