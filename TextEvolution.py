result = list ("HELLO WORLD")
z=0
y=0
words = list (input ('Введите 11 символов: '))
if len (words) == 11:
    while words != result and z!=11:
        words [y] = result [y]
        y +=1
        z +=1
        f = ''.join (words)
        print ('Изменение %r: ' %z, f)
else:
    exit 
