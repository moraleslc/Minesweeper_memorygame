import random, os, time

# LIMPIAR TERMINAL (AMBAS FUNCIONES)

def limpia():
    if os.name=='nt': #Windows
        os.system('cls')
    else:
        os.system('clear') #Mac/Linux
        
#BUSCAMINAS

#DESTAPA COORDENADAS
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

#COLOCA MINAS Y NÚMEROS
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

#DESPLIEGA TABLERO (BUSCAMINAS)
    
def despliega_cuadro(tablero):
    for renglon in tablero:
        print("-------------------------------------")
        print("|", end="")
        for elemento in renglon:
            print(f'{elemento}'.center(5), end="")
            print("|", end="")
        print("\n-------------------------------------")

#COMPRUEBA BANDERITAS CON MINAS
def banderita_mina(banderita, real):
    contadorb=0
    for col in range(6):
        for ren in range(6):
            if banderita[col][ren]=='#' and real[col][ren]=='*':
                contadorb+=1
    if contadorb==6:
        return('Ganador')
    else:
        return('Perdiste')
    
#CREAR MATRIZ ESCONDIDA
def crear_matriz_escondida():
    matriz_esc=[]
    for col in range(6):
        lista=[]
        for ren in range(6):
            lista.append('x')
        matriz_esc.append(lista)
    return(matriz_esc)
    
#MEMORAMA
    
#CREAR MATRIZ
def crear_matriz():
    matriz_simbolos=[]
    matriz_nueva=[]
    simbolos=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z']
    for num in range (18):
        sim=random.choice(simbolos)
        for nam in range(2):
            matriz_simbolos.append(sim)
        simbolos.remove(sim)
    matriz_nueva=[]
    for ha in range(6):
        listax=[]
        for hu in range(6):
            valor=random.choice(matriz_simbolos)
            listax.append(valor)
            matriz_simbolos.remove(valor)
        matriz_nueva.append(listax)
    return(matriz_nueva)

#IMPRESIÓN DE MATRIZ (MEMORAMA)
def despliega_memorama(tablero):
    for renglon in tablero:
        print("-------------------------------------------------------------------")
        print("|", end="")
        for elemento in renglon:
            print(f'{elemento}'.center(10), end="")
            print("|", end="")
        print("\n-------------------------------------------------------------------")

##PROGRAMA PRINCIPAL

opcion=0

while opcion!=5:
    limpia()
    print('''
------------------BUSCAMINAS Y MEMORAMA------------------

    MENÚ
    
    1- JUGAR BUSCAMINAS
    2- JUGAR MEMORAMA
    3- INSTRUCCIONES Y REGLAS DE LOS JUEGOS
    4- CRÉDITOS
    5- SALIR
    
---------------------------------------------------------''')

    opcion=int(input())
    
    # BUSCAMINAS
    if opcion==1:
        cuadricula=crear_matriz_escondida()
        limpia()
        despliega_cuadro(cuadricula)
        minas=cuadro_minas()   #Minas ya colocadas en matriz
        over=False
        banderita=0
        while not over:
            
            print('''
    1-. Destapar coordenadas
    2-. Colocar una banderita
    3-. Quitar una banderita
            ''')
            opcm=int(input())
            
            if opcm==1:
                print('Escribe las coordenadas que quieras destapar')
                renglon=int(input('Renglón: '))
                columna=int(input('Columna: '))
                if 0<renglon<7 and 0<columna<7:
                    renglon-=1
                    columna-=1
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
            elif opcm==2:
                limpia()
                despliega_cuadro(minas_usuario)
                print('''
Cuentas con 6 banderitas a colocar. Te quedan ''' + str(6-banderita) + '''.
Escribe las coordenadas donde quieras colocar tu banderita:
        ''')
                renban=int(input('Renglón: '))
                colban=int(input('Columna: '))
                if 0<renban<7 and 0<colban<7:
                    limpia()
                    minas_usuario[renban-1][colban-1]='#'
                    banderita+=1
                    despliega_cuadro(minas_usuario)
                    
                    if banderita>=6:
                        resultado=banderita_mina(minas_usuario, minas)
                        over=True
                    else:
                        continue
                else:
                    print('')
                    print('Ingresaste un valor inválido, intenta de nuevo')
            elif opcm==3:
                print('')
                print('Ingresa las coordenadas de la banderita que quieras quitar.')
                renquit=int(input('Renglón: '))
                colquit=int(input('Columna: '))
                if 0<renquit<7 and 0<colquit<7:
                    minas_usuario[renquit-1][colquit-1]='x'
                    banderita-=1
                    limpia()
                    despliega_cuadro(minas_usuario)
                else:
                    print('')
                    print('Ingresaste valores inválidos')
                    continue
            else:
                print('Ingresaste un valor inválido, intenta de nuevo.')
                print('')
        if resultado=='Ganador':
            print('''
        ¡GANASTE!
''')
            menu=input('Da enter para regresar al menú')
            continue
        else:
            limpia()
            despliega_cuadro(minas)
            print('''
        ¡PERDISTE!
        
''')
            menu=input('Da enter para regresar al menú')
            limpia()
            continue
        
    #MEMORAMA
    elif opcion==2:
        limpia()
        matriz_escondida=crear_matriz_escondida()
        matriz_muestra=crear_matriz_escondida()
        matriz=(crear_matriz())
        # Despliega la matriz con valores pares
        despliega_memorama(matriz)
        enter=input('''
Recuerda la ubicación de las letras ya que se esconderá el tablero y tendrás que descubrir los pares

Da enter cuando quieras comenzar''')
        limpia()
        errores=0
        puntos=0
        columna1=1
        columna2=1
        renglon1=1
        renglon2=1
        intentos=3


        while errores<3:
            despliega_memorama(matriz_escondida)
            print('''
Escribe las coordenadas de tus pares
Primer par''')
            columna1=int(input('Columna='))
            renglon1=int(input('Renglón='))
            
            limpia()
            if 0<columna1<7 and 0<renglon1<7:
                #Despliega la primera coordenada
                matriz_muestra[renglon1-1][columna1-1]=matriz[renglon1-1][columna1-1]
                despliega_memorama(matriz_muestra)
                
                print('''
Segundo par''')
                columna2=int(input('Columna='))
                renglon2=int(input('Renglón='))
                
                limpia()
                if 0<columna2<7 and 0<renglon2<7:
                    #Despliega la segunda coordenada
                    matriz_muestra[renglon2-1][columna2-1]=matriz[renglon2-1][columna2-1]
                    despliega_memorama(matriz_muestra)
                    time.sleep(5)
                    
                    
                    if matriz[renglon1-1][columna1-1]==matriz[renglon2-1][columna2-1]:
                        matriz_escondida[renglon1-1][columna1-1]=matriz[renglon1-1][columna1-1]
                        matriz_escondida[renglon2-1][columna2-1]=matriz[renglon2-1][columna2-1]
                        puntos+=1
                        limpia()
                        print('''
Correcto
                                           ''')
                    else:
                        errores+=1
                        matriz_muestra[renglon1-1][columna1-1]='x'
                        matriz_muestra[renglon2-1][columna2-1]='x'
                        limpia()
                        print('''
Oportunidades restantes: ''' + str(intentos-errores) + '''
''')
                    if puntos==18:
                        print('''
¡FELICIDADES! ¡GANASTE!
Cantidad de errores obtenidos: ''' + str(errores) + '''.
''')
                    elif 3<=errores:
                        print('''
Perdiste!
Obtuviste ''' + str(puntos) + ''' puntos. Intenta de nuevo.

            ''')
                        enter=input('Da enter para regresar al menú')
                        break
                    else:
                        continue
                else:
                    limpia()
                    print('''

                    Ingresaste valores inválidos, intenta de nuevo
                            
                            ''')
            else:
                limpia()
                print('''

                    Ingresaste valores inválidos, intenta de nuevo
                        
                        ''')


#INSTRUCCIONES
    elif opcion==3:
        limpia()
        print('''
-----------------------------------------------------INSTRUCCIONES-----------------------------------------------------
                
BUSCAMINAS

Al desplegarse el tabalero, ingresa el número de las columnas que deseas destapar, ya que no puedes colocar banderitas
sin conocer valores. Se destapará un número. Si es un 0, eso significa que tanto en sus lados superiores, inferiores,
izquierdo, derecho, o diagonales, no hay minas. En el caso de ser 1, se encuentra cerca de 1 mina. Si se despliega
un 2, estará cerca de 2 minas, y 3 si está cerca de 3. Para ganar, tienes que colocar banderitas (indicado con #) sobre
la posición de las bombas, ingresando el número de columna y renglón donde sea desea ingresar la banderita. En el caso
que hayas colocado mal una banderita, podrás quitarla con la tercera opción, igualmente ingresando la columna y posición
donde se encuentra.

MEMORAMA

Dentro de un tablero se asignarán pares de letras del abecedario de manera aleatoria, con el fin de que encuentres la
posición de los pares al esconderse las letras. Ingresa el número de renglón y columna que deseas destapar para los
pares. Tendrás 5 segundos donde se revelarán las letras y dependiendo si son pares, se sumará puntos, mientras en el
caso que no sean pares, se te quitará una oportunidad de las tres que tienes. Ganarás si revelas todas las casillas
pares y perderás si no logras identificar las casillas pares en tres intentos.

''')
        enter=input('Da enter para regresar al menú')
    #CREDITOS
    elif opcion==4:
        limpia()
        print('''

                          PROYECTO INTEGRADOR:
                Juegos Cognitivos - Buscaminas y memorama
        
        Este programa fue creado por Carla Morales y Andrea Borjas
        Pensamiento Computacional para Ingeniería
        Fabiola Uribe Plata
        Grupo 17
        9:00-10:50

''')
        proyecto=input('Da enter para regresar al menú ')
        continue
    elif opcion==5:
        limpia()
        print('''
                        ¡Gracias por jugar!
''')
        break
    else:
        print('')
        print('Ingresaste un valor inválido. Intenta de nuevo.')
        time.sleep(1)