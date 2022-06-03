import random, os

# LIMPIAR TERMINAL

def limpia():
    if os.name=='nt': #Windows
        os.system('cls')
    else:
        os.system('clear') #Mac/Linux
        
#BUSCAMINAS

#Destapa las coordenadas dadas por el usuario
def destapar(ren, col, mini, man):
    if mini[ren][col]==0:
        man[ren][col]=mini[ren][col]
        for a in [1, 0, -1]:
            for o in [1, 0, -1]:
                try:
                    if mini[ren+a][col+o]==0:
                        if (ren+a>-1 and col+o>-1):
                            man[ren+a][col+o]=mini[ren+a][col+o]
                except:
                    pass
    else:
        man[ren][col]=mini[ren][col]
    return(man)

#Coloca minas al azar
def cuadro_minas():
    mi=[['x', 'x', 'x', 'x', 'x', 'x'],
                ['x', 'x', 'x', 'x', 'x', 'x'],
                ['x', 'x', 'x', 'x', 'x', 'x'],
                ['x', 'x', 'x', 'x', 'x', 'x'],
                ['x', 'x', 'x', 'x', 'x', 'x'],
                ['x', 'x', 'x', 'x', 'x', 'x']]
    for i in range(6):
        ren=random.randint(0, 5)
        col=random.randint(0, 5)
        mi[ren][col]='*'
    for ren in range(6):
        for col in range(6):
            if mi[ren][col]!='*':
                count=0
                for a in [1, 0, -1]:
                    for o in [1, 0, -1]:
                        try:
                            if mi[ren+a][col+o]=='*':
                                if (ren+a>-1 and col+o>-1):
                                    count+=1
                        except:
                            pass
                mi[ren][col]=count

    return(mi)

#DESPLIEGA TABLERO (AMBAS FUNCIONES)
    
def despliega_cuadro(tablero):
    for renglon in tablero:
        print("---------------------------------------------------------------------")
        print("|", end="")
        for elemento in renglon:
            print(f'{elemento}'.center(10), end="")
            print("|", end="")
        print("\n-------------------------------------------------------------------")



##PROGRAMA PRINCIPAL


print('''
------------------BUSCAMINAS Y MEMORAMA------------------

    MENÚ
    
    1- JUGAR BUSCAMINAS
    2- JUGAR MEMORAMA
    3- SALIR
    
---------------------------------------------------------''')

opcion=int(input())
while opcion!=3:
    if opcion==1:
        cuadricula=[['x', 'x', 'x', 'x', 'x', 'x'],
                ['x', 'x', 'x', 'x', 'x', 'x'],
                ['x', 'x', 'x', 'x', 'x', 'x'],
                ['x', 'x', 'x', 'x', 'x', 'x'],
                ['x', 'x', 'x', 'x', 'x', 'x'],
                ['x', 'x', 'x', 'x', 'x', 'x']]
        limpia()
        despliega_cuadro(cuadricula)
        minas=cuadro_minas()   #Minas ya colocadas en matriz
        over=False
        while not over:
            print(' ')
            print('Escribe las coordenadas que quieras destapar')
            renglon=int(input('Renglón: '))-1
            columna=int(input('Columna: '))-1
            if 0<=renglon<7 and 0<=columna<7: 
                limpia()
                if minas[renglon][columna]=='*':
                    resultado='Perdiste'
                    over=True
                else:
                    minas_usuario=destapar(renglon, columna, minas, cuadricula)
                    despliega_cuadro(minas_usuario)
            else:
                print('''
Valores inválidos, intenta de nuevo.''')
            
        if resultado=='Ganador':
            print('''
        GANASTE!
''')
            break
        else:
            despliega_cuadro(minas)
            print('''
        PEDRISTE!
''')
            break
    else:
        break