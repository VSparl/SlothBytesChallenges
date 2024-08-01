def sort_function(arr):
    if not arr:
        # Empty array
        return arr

    new_arr = []
    for string in arr:
        for symbol in string:
            if symbol.isalpha():  # Ignore numbers
                # Insert string into list based on the ASCII value of the char
                # Subtract 61 to instert the letter a at index 0
                # We only have lowercase letters anyway
                new_arr.insert(ord(symbol) - 61, string)

    return new_arr


def sort_by_letter(arr):
    return sorted(arr, key=sort_function)


print("\n".join(sort_by_letter(["932c", "832u32", "2344b"]),
                sort_by_letter(["99a", "78b", "c2345", "11d"]),
                sort_by_letter(["572z", "5y5", "304q2"]),
                sort_by_letter([])
                ))
