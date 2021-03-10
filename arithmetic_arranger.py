def arithmetic_arranger(problems, check = False):
    ### Function to receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side.
    ### Function accept 2 parameters, first the list of problems, second is a boolean to show result or not

    # initialize lines data list
    line1 = []
    line2 = []
    line3 = []
    line4 = []
    line5 = []


    # check number of problems if greater than 5
    if len(problems) > 5 :
        return('Error: Too many problems.')

    # Iterate in problems
    for problem in problems :

        # check if operator is addition
        if '+' in problem :
            operator = '+'
            operands = problem.split('+')
        # check if operator is subtraction
        elif '-' in problem :
            operator = '-'
            operands = problem.split('-')
        # otherwise raise Error: Operator must be '+' or '-'
        else :
            return("Error: Operator must be '+' or '-'.")

        # convert the all operands to integers
        # and handle non integer operand exception
        try:
            operands = list(map(int, operands))
        except:
            return('Error: Numbers must only contain digits.')

        # initiate variable for largest number of digits
        numlen = None
        
        for operand in operands:

            # check if operand is greater than 4 digits
            if operand > 9999:
                return('Error: Numbers cannot be more than four digits.')

            # save largest number of digits
            if numlen is None:
                numlen = len(str(operand))
            elif numlen < len(str(operand)):
                numlen = len(str(operand))

        # Add space for operator and next white space
        numlen = numlen + 2
        
        # Calculate problem result
        result = eval(str(operands[0]) + operator + str(operands[1]))
        
        # update lines lists with each problem data
        line1.append(str(operands[0]).rjust(numlen))                            # 1st operand
        line2.append(operator + ' ' + str(operands[1]).rjust(numlen - 2))       # operator + white_space + 2nd operand
        line3.append(''.rjust(numlen, '-'))                                     # dashes separator
        line4.append(str(result).rjust(numlen))                                 # result

    # prepare lines lists for print and separate each problem by 4 white spaces
    line1 = '    '.join(line1)
    line2 = '    '.join(line2)
    line3 = '    '.join(line3)
    line4 = '    '.join(line4)

    # Arrange arranged_problems
    arranged_problems = line1 + '\n' + line2 + '\n' + line3

    # Add result line if requested / check is True
    if check:
        arranged_problems = arranged_problems + '\n' + line4
        
    return arranged_problems
