def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(1)
print_params('строка', True)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ('stoka', True, 26)
values_dict = {'a': 'Urban', 'b': [1, 2, 3], 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ([2, 6, 8], 'vlada')
print_params(*values_list_2, 42)

