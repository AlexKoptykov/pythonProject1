t = input()
if t[0:6] == 'qwerty':
    print('ОЧЕНЬ ПЛОХО')
else:
    if "qwerty" in t:
        print('ПЛОХО')
    else:
        print('ХОРОШО')