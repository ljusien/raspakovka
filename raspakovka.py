def print_params(a=3, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])
values_list = [9.8, 'const', True]
values_dict = {'b': 2, 'b': False, 'c': 0}
print_params(*values_list)
print_params(**values_dict)
print()
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)





