import string 

string_to_check_1 = string.ascii_lowercase
string_to_check_2 = "abcdefghijklmnopqrstuvwxyz"

def isAlphabet(string):
    for i in range(len(string) - 1):
        if string[i] > string[i + 1]:
            return False
    return True

result_1 = isAlphabet(string_to_check_1)
result_2 = isAlphabet(string_to_check_2)
print(result_1, result_2)
