def secret_entrance_password_finder_part_1(file: str, num_comb: int = 100, init_val: int = 50) -> None:
    """Counts how many times the cracker follows the given movements and gets 0"""
    print(f"Cracking the password of {file}...")
    value = init_val
    password = 0
    with open(file, "r") as f:
        for line in f:
            if line[0] == "L":
                value = (value - int(line[1:])) % num_comb
            else:
                value = (value + int(line[1:])) % num_comb
            if value == 0:
                password += 1
    print(f"The password is {password}")


def secret_entrance_password_finder_part_2(file: str, num_comb: int = 100, init_val: int = 50) -> None:
    """Counts how many times the cracker rolls over 0 whilst following the given movements"""
    print(f"Cracking the password of {file}...")
    value = init_val
    password = 0
    with open(file, "r") as f:
        i = 0
        for line in f:
            i += 1
            diff = int(line[1:])
            password += (diff // num_comb)  # Accounts for if it'd pass 0 multiple times
            diff %= num_comb
            if line[0] == "L":
                value -= diff
                # Valid if it passes 0 on the left but only if it wasn't already 0
                if (value <= 0) and (value != -diff):
                    password += 1
            else:
                value += diff
                # Valid if it passes 0 on the right
                if (value >= num_comb):
                    password += 1
            value %= num_comb
    print(f"The password is {password}")


if __name__ == "__main__":
    print("Part 1:")
    secret_entrance_password_finder_part_1("test_input.txt")
    secret_entrance_password_finder_part_1("input.txt")

    print("Part 2:")
    secret_entrance_password_finder_part_2("test_input.txt")
    secret_entrance_password_finder_part_2("input.txt")
