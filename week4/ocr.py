def convert(input_grid):
    DIGITS = {
        (" _ ",
        "| |",
        "|_|",
        "   "): " 0",
        ("   ",
        "  |",
        "  |",
        "   "): "1",
        (" _ ", 
        " _|", 
        "|_ ", 
        "   "): "2",
        (" _ ", 
        " _|", 
        " _|", 
        "   "): "3",
        ("   ", 
        "|_|", 
        "  |", 
        "   "): "4",
        (" _ ", 
        "|_ ", 
        " _|", 
        "   "): "5",
        (" _ ", 
        "|_ ", 
        "|_|", 
        "   "): "6",
        (" _ ", 
        "  |", 
        "  |", 
        "   "): "7",
        (" _ ", 
        "|_|", 
        "|_|", 
        "   "): "8",
        (" _ ", 
        "|_|", 
        " _|", 
        "   "): "9"
    }

    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if any(len(row) % 3 != 0 for row in input_grid):
        raise ValueError("Number of input columns is not a multiple of three") 

    result_lines = []
    for row_index in range(0, len(input_grid),4):
        lines = ""
        print(row_index)
        for column_index in range(0, len(input_grid[row_index]), 3):
            digit_block = tuple(input_grid[row_index + i][column_index:column_index + 3] for i in range(4))
            lines += DIGITS.get(digit_block, "?")
            print(column_index)

        result_lines.append(lines)
    return ",".join(result_lines)

print(convert([
                    "    _  _ ",
                    "  | _| _|",
                    "  ||_  _|",
                    "         ",
                    "    _  _ ",
                    "|_||_ |_ ",
                    "  | _||_|",
                    "         ",
                    " _  _  _ ",
                    "  ||_||_|",
                    "  ||_| _|",
                    "         ",
                ]))