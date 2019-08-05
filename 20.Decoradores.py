# -*- coding: utf-8 -*-
# v = 4.6

def protected(protected_func):
    def wrapper(password):
        if password == 'platzi':
            return protected_func()
        else:
            print('La contraseña es incorrecta')

    return wrapper

@protected 
def protected_func(): # es la funcion que queremos decorar -> unicamente se ejecuta la funcion si el password es correcto
    print('Tu contraseña es correcta.')

if __name__ == "__main__":
    password = str(input('Ingresa tu contraseña: '))

    protected_func(password)