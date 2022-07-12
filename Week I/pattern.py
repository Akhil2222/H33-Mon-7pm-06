x=10
for i in range(x):
    str = ''
    spac = ''
    for j in range(i):
        str = str + '*'
    for j in range(x-i):
        spac = spac + ' '
    print(spac + str + ' ' + str)