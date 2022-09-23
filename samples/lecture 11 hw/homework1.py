#1 write a motto
import os
filename = 'motto.txt'

try:
    path = os.path.dirname(os.path.abspath(__file__))
    filehandle = open(path+'/'+filename, 'w+')
    filehandle.write('Fiat Lux!')
    filehandle.seek(0)
    print(filehandle.readline())
except IOError:
    print('IO Error! Please check valid file names and paths')
    exit
finally:
    filehandle.close()

try:
    filehandle = open(path+'/'+filename, 'a')
    filehandle.write('\nLet there be light!')
except IOError:
    print('IO Error! Please check valid file names and paths')
    exit
finally:
    filehandle.close()   
    