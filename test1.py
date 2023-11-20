year = int(input())
match year % 12:
 case 0:
    res = 'год обезьяны'
 case 1:
    res = 'год петуха'
 case 2:
    res = 'год собаки'
 case 3:
    res = 'год свиньи'
 case 4:
    res = 'год мыши'
 case 5:
    res = 'год быка'
 case 6:
    res = 'год тигра'
 case 7:
    res = 'год кролика'
 case 8:
    res = 'год дракона'
 case 9:
    res = 'год змеи'
 case 10:
    res = 'год лошади'
 case 11:
    res = 'год овцы'
print(res)