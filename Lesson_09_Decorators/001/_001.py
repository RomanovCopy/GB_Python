from shlex import join


def func01(str1):
    array=[]
    print(str1)
    def func02(str2):
        array.append(str2)
        return str1+', '+ ', '.join(array)
    return func02


a = func01('Sergey')
print(a('Romanov'))
print(a('Mihailovich'))
print(func01('Romanov')('Sergey'))
