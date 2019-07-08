import os

def makedir(i):
    try:
        os.mkdir('./dir' + i)
    except FileExistsError:
        print('dir{} - папка уже существует'.format(i))

def removedir(i):
    try:
        os.removedirs('./dir' + i)
    except FileNotFoundError:
        print('dir{} - папки не существует'.format(i))

for r in range(10):
    makedir(str(r+1))
print(os.listdir())

for r in range(10):
    removedir(str(r+1))