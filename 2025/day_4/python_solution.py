import numpy as np


def find_accessible(grid):
    height = len(grid)
    width = len(grid[0])
    accessible = []

    num_accessible = 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] != "@":
                print(".", end="")
                if j == width-1:
                    print("")
                continue

            number_adjacent = 0

            # Top Cases
            if i > 0:
                # Directly Above
                if grid[i-1][j] == "@":
                    number_adjacent += 1

                # Top Left
                if j > 0:
                    if grid[i-1][j-1] == "@":
                        number_adjacent += 1

                # Top Right
                if j < width - 1:
                    if grid[i-1][j+1] == "@":
                        number_adjacent += 1

            # Bottom cases
            if i < height - 1:
                # Dirrectly Below:
                if grid[i+1][j] == "@":
                    number_adjacent += 1
                if j < width - 1:
                    # Bottom Right:
                    if grid[i+1][j+1] == "@":
                        number_adjacent += 1
                if j > 0:
                    # Bottom Left:
                    if grid[i+1][j-1] == "@":
                        number_adjacent += 1
            # Left
            if (j > 0) and (grid[i][j-1] == "@"):
                number_adjacent += 1

            # Right
            if (j < width - 1) and (grid[i][j+1] == "@"):
                number_adjacent += 1

            if number_adjacent < 4:
                print("x", end="")
                num_accessible += 1
                accessible.append((i, j))
            else:
                print("@", end="")

            if j == width - 1:
                print("")

    print(f"{num_accessible} removed")
    return accessible, num_accessible


def read_grid_from_file(filename: str) -> list[list[str]]:
    with open(filename) as f:
        grid = []
        for line in f:
            grid.append(list(line.strip()))
    return np.array(grid, dtype=str)


def day_4a(filename: str) -> list[tuple[int]]:
    print(f"Processing {filename}...")
    grid = read_grid_from_file(filename)
    return find_accessible(grid)


def day_4b(filename: str) -> None:
    print(f"Processing {filename}...")
    grid = read_grid_from_file(filename)
    total_accessible = []
    num_accessible = None
    while num_accessible != 0:
        accessible, num_accessible = find_accessible(grid)
        if num_accessible > 0:
            total_accessible.extend(accessible)
            for index in accessible:
                grid[index] = "."
    print(len(total_accessible))


if __name__ == "__main__":
    print("Part 1")
    day_4a("test_input.txt")
    day_4a("input.txt")
    print("Part 2")
    day_4b("test_input.txt")
    day_4b("input.txt")
