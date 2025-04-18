def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    first_line = []
    second_line = []
    dashes = []
    answers = []

    for problem in problems:
        num1, operator, num2 = problem.split()

        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        if not (num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.'
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'  

        num1_int = int(num1)
        num2_int = int(num2)    

        answer = num1_int + num2_int if operator == '+' else num1_int - num2_int

        width = max(len(str(num1)), len(str(num2))) + 2 
        first_line.append(f"{num1:>{width}}")
        second_line.append(f"{operator} {num2:>{width - 2}}")
        dashes.append('-' * width)
        answers.append(f"{answer:>{width}}")
    arranged_problems = '    '.join(first_line) + '\n' + \
                        '    '.join(second_line) + '\n' + \
                        '    '.join(dashes)         
    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)


    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')