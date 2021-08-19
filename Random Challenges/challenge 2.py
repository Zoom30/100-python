# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
# Examples

# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true

# Constraints

# 0 <= input.length <= 100

# Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).


def valid_parentheses(string):
    num_open_par = string.count("(")
    num_close_par = string.count(")")
    is_complete = []
    if num_open_par != num_close_par:
        return False
    else:
        is_open_counter = 0
        is_closed_counter = 0
        for alpha in string:
            if alpha == "(":
                is_open_counter += 1
            elif alpha == ")":
                is_closed_counter += 1
                if is_closed_counter > is_open_counter:
                    return False
            if is_closed_counter == is_open_counter:
                is_complete.append("complete")
        if all(item == "complete" for item in is_complete) == True:
            return True


print(valid_parentheses("hi())("))
