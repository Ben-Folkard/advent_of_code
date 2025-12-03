from numpy import array_split, array_equal


def day_2a_gift_shop_id_checker(filename: str) -> None:
    """Checks whether the first half of the number is equal to the 2nd"""
    print(f"Processing {filename}...")
    sum_ids = 0
    with open(filename, "r") as f:
        id_ranges = f.readline().split(",")
        for id_range in id_ranges:
            id_min, id_max = id_range.split("-")
            for ID in range(int(id_min), int(id_max)+1):
                ID_str = str(ID)
                midpoint = len(ID_str)//2
                if ID_str[:midpoint] == ID_str[midpoint:]:
                    sum_ids += ID
    print(sum_ids)


def day_2b_gift_shop_id_checker(filename: str) -> None:
    """Checks if the number is made up of repeating numbers in a sequence"""
    print(f"Processing {filename}...")
    sum_ids = 0
    with open(filename, "r") as f:
        id_ranges = f.readline().split(",")
        for id_range in id_ranges:
            id_min, id_max = id_range.split("-")
            for ID in range(int(id_min), int(id_max)+1):
                ID_str = str(ID)
                ID_len = len(ID_str)
                if ID_len == 2:
                    if ID_str[0] == ID_str[1]:
                        sum_ids += ID
                else:
                    # As soon as it finds the the ID is made up of a repeating sequence it stops looking
                    for factor in range(2, ID_len+1):
                        if ID_len % factor == 0:
                            chunks = array_split(list(ID_str), factor)
                            for i in range(len(chunks)-1):
                                if not array_equal(chunks[i], chunks[i+1]):
                                    break
                            else:
                                sum_ids += ID
                                break
    print(sum_ids)


if __name__ == "__main__":
    print("Part 1:")
    day_2a_gift_shop_id_checker("test_input.txt")
    day_2a_gift_shop_id_checker("input.txt")
    print("Part 2:")
    day_2b_gift_shop_id_checker("test_input.txt")
    day_2b_gift_shop_id_checker("input.txt")
