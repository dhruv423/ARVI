import random
import string







def randomPassGenerator(min_string,max_string):

        # A string of letters (uppercase and lowercase), special characters and digits
        all_Chars = string.ascii_letters + string.digits + "-|@.,?/!~#%^&*(){}[]\=*"
        password = ""
        for x in range(random.randint(min_string, max_string)):
            password += ''.join(random.choice(all_Chars))
        return password



print(randomPassGenerator(10,24))