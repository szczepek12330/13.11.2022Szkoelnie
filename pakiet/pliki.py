with open('test.log', 'w',encoding= 'utf-8') as f:
    f.write('powitanie\n')
    f.write('jeszcze jedno\n')
    f.write('Łukasz...')

with open('test.log', 'a',encoding= 'utf-8') as f:
    f.write('\nComarch')

with open('test.log', 'r',encoding= 'utf-8') as f:
    lines = f.read()
    print(lines)
