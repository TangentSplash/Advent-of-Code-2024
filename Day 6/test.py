# String constant defined earlier in the file
STRING_CONSTANT = "example_string"

# Function to demonstrate the match-case structure
def check_string(s):
    match s:
        case value if value == STRING_CONSTANT:
            return "Matched the string constant"
        case _:
            return "Did not match the string constant"

# Example usage
result = check_string("example_string")
print(result)  # Output: Matched the string constant
result = check_string("exahkbmple_string")
print(result)  # Output: Matched the string constant
