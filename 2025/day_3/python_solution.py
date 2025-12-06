def day_3a_lobby(filename: str) -> None:
    """
    Finds the largest possible 2 digit number that can be made from
    a sequence of single digit numbers (preserving order of input)
    """
    print(f"Processing {filename}...")
    total = 0
    with open(filename) as f:
        for line in f:
            largest_vals = [0, 0]
            nums = [int(num) for num in line.strip()]
            num_nums = len(nums)
            for i, num in enumerate(nums):
                if num > largest_vals[0]:
                    # Providing it isn't the last number in the list,
                    # the largest 2 digit number will always start with the largest digit
                    if i != (num_nums - 1):
                        largest_vals = [num, 0]
                    elif num > largest_vals[1]:
                        largest_vals[1] = num
                elif num > largest_vals[1]:
                    largest_vals[1] = num
            total += int(f"{largest_vals[0]}{largest_vals[1]}")

    print(total)


def day_3b_lobby(filename: str, num_batteries: int = 12) -> None:
    """
    Finds the largest possible 12 digit number that can be made from
    a sequence of single digit numbers (preserving order of input):
    """
    print(f"Processing {filename}...")
    total = 0
    with open(filename) as f:
        for line in f:
            nums = [int(num) for num in line.strip()]
            num_digit_to_remove = len(nums) - num_batteries
            largest_vals = []

            for digit in nums:
                while num_digit_to_remove > 0 and largest_vals and largest_vals[-1] < digit:
                    largest_vals.pop()
                    num_digit_to_remove -= 1
                largest_vals.append(digit)

            largest_number = ""
            for val in largest_vals[:num_batteries]:
                largest_number += str(val)
            total += int(largest_number)

    print(total)


if __name__ == "__main__":
    print("Part 1:")
    day_3a_lobby("test_input.txt")
    day_3a_lobby("input.txt")
    print("Part 2:")
    day_3b_lobby("test_input.txt")
    day_3b_lobby("input.txt")
