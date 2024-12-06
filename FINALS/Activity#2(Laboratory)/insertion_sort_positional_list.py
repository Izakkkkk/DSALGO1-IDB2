from PositionalList import PositionalList
from LinkedStack import LinkedStack

def evaluate_postfix(expression):
    stack = []
    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)
            else:
                raise ValueError(f"Unknown operator: {token}")
    return stack[0]

def insertion_sort(arr, ascending=True):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and ((arr[j] > key) if ascending else (arr[j] < key)):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    print("Enter a postfix expression (e.g., '5 2 + 8 3 - * 4 /'):")
    postfix_expr = input("> ").strip()
    try:
        result = evaluate_postfix(postfix_expr)
        print("Result of postfix evaluation:", result)
    except ValueError as e:
        print("Error:", e)

    print("\nEnter numbers separated by spaces for sorting (e.g., '5 2 9 1 3'):")
    user_input = input("> ").strip()
    try:
        numbers = list(map(int, user_input.split()))
        sorted_asc = insertion_sort(numbers.copy(), ascending=True)
        sorted_desc = insertion_sort(numbers.copy(), ascending=False)
        print("Sorted in Ascending Order:", sorted_asc)
        print("Sorted in Descending Order:", sorted_desc)
    except ValueError:
        print("Error: Please enter valid numbers.")
