"""
Перевод со строки в спиок и обратно
"""
line_str = input()
#line_list = line_str.split() # из строки в список
line_list = list(line_str)
line_str_x = ''.join(line_list) # из списка в строку
print(len(line_list))
print(line_list)
print(line_str)
print(line_str_x)