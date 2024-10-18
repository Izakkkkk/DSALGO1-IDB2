from ArrayStack import ArrayStack as Stack

# Part 1: Balanced Expression Checker
def is_balanced(expression):
    stack = Stack()
    matching_pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in '([{':
            stack.push(char)  # Push opening bracket to the stack
        elif char in ')]}':
            if stack.is_empty() or stack.pop() != matching_pairs[char]:
                return False  # unbalanced if stack top is not a closing bracket

    return stack.is_empty()  # balanced if stack is empty at the end


def test_balanced_expressions():
    expressions = [
        "( )(( )){([( )])}",  # Correct
        "((( )(( )){([( )])}))",  # Correct
        ")(( )){([( )])}",  # Incorrect
        "({[])}",  # Incorrect
        "("  # Incorrect
    ]

    print("Balanced Expression Checker Results:")
    for exp in expressions:
        result = is_balanced(exp)
        print(f"Expression: {exp} - Balanced: {result}")
    print("\n")  # space for readability


# Part 2: Reversing Lines in a File
def reverse_lines_in_file(input_file, output_file):
    stack = Stack()

    # Try to open the input file
    try:
        with open(input_file, 'r') as file:
            for line in file:
                stack.push(line)

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
        return

    # Open the output file in write mode
    with open(output_file, 'w') as file:
        while not stack.is_empty():
            reversed_line = stack.pop()
            file.write(reversed_line)

    print("Reversed lines written to {output_file} \n")


def reverse_file_example():
    input_file = 'myfile.txt'
    output_file = 'reversed_output.txt'

    # Reverses the lines in the file
    reverse_lines_in_file(input_file, output_file)


# Run balanced checker and the file reverser
if __name__ == "__main__":
    print("Part 1: Balanced Expression Checker")
    test_balanced_expressions()

    print("Part 2: Reverse File Lines")
    reverse_file_example()
