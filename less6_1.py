# try:
#     print('start code')
#     print(name)
#     print('No error')
# except:
#     print('We have a problem (error)')
try:
    print('start code.')
    print(2 / 0)
    print(name)
    print('no errors.')
# except(NameError, ZeroDivisionError):
#     print('We have an Error')

except(NameError, ZeroDivisionError) as error:
    print(error)

print('code after capsule.')


try:
    try:
        print('start code.')
        print(error)
        print('no errors.')
    except SyntaxError:
        print('Wrong Syntax')
except: NameError as error:
    print(error)