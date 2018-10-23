import os

if os.path.exists('aula'):
    print 'removendo arquivo...'
    os.remove('aula')
else:
    print 'nao existe'
