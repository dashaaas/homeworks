def check_palindrom(string):
    if string == string[::-1]:
        return True
    return False


my_string = 'лепсспел'
print(check_palindrom(my_string))