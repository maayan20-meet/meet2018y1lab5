speed = 50
is_birthday = True

if (is_birthday = False and speed < 31) or (is_birthday = True and speed < 36):
    print('no ticket')

if (is_birthday = False and speed > 31 and speed < 51) or (is_birthday = True and speed < 36 and speed < 56):
    print('small ticket')

if (is_birthday = False and speed < 50) or (is_birthday = True and speed < 56):
    print('big ticket!')
