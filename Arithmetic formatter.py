#Arithmetic formatter project
def arithmetic_arranger(problems, display_answers=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize strings to store each line of the arranged problems
    first_line = ""
    second_line = ""
    dashes = ""
    answers = ""

    # Loop through each problem in the list
    for problem in problems:
        parts = problem.split()  # Split the problem into its components
        if parts[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        if not (parts[0].isdigit() and parts[2].isdigit()):
            return "Error: Numbers must only contain digits."
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        operand1 = parts[0]  # First number
        operator = parts[1]  # Operator (+ or -)
        operand2 = parts[2]  # Second number

        # Calculate the result based on the operator
        if operator == "+":
            result = str(int(operand1) + int(operand2))
        else:
            result = str(int(operand1) - int(operand2))

        # Determine the width of the problem for formatting
        width = max(len(operand1), len(operand2)) + 2
        first_line += operand1.rjust(width) + "    "
        second_line += operator + operand2.rjust(width - 1) + "    "
        dashes += "-" * width + "    "
        answers += result.rjust(width) + "    "

    # Combine the lines into the final arranged problems string
    arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + dashes.rstrip()
    if display_answers:
        arranged_problems += "\n" + answers.rstrip()

    return arranged_problems

# Example usage:
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
