print(f'NameError - {type(NameError)} -')
'''print(maxim)
print("hello")'''
try:
    print('start code')
    print(illia)
    print('no error')
except:
    print("We have an error")
print('кінець!')

print('$$$$$$$$$$$$$$$$$$$$$$$$$$')
try:
    print('start code')
    print(10/0)
    print('no error')
except NameError:
    print("We have an error NameError")
except ZeroDivisionError:
    print("We have an error ZeroDivisionError ")
print('кінець!')

print('$$$$$$$$$$$$$$$$$$$$$$$$$$')

try:
    print('start code')
    print(5/0)
    print('no error')
except (NameError, ZeroDivisionError) as error:
    print(error)
print('$$$$$$$$$$$$$$$$$$$$$$$$$$')
try:
    try:
        print('start code')
        print(5/0)
        print('no error')
    except SyntaxError:
     print("Wrong Syntax")
except NameError as error:
    print(error)

