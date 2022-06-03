import random, os, time

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

def despliega_memorama(tablero):
    for renglon in tablero:
        print("-------------------------------------------------------------------")
        print("|", end="")
        for elemento in renglon:
            print(f'{elemento}'.center(10), end="")
            print("|", end="")
        print("\n-------------------------------------------------------------------")
        
def limpia():
    if os.name=='nt': #Windows
        os.system('cls')
    else:
        os.system('clear') #Mac/Linux
            
def crear_matriz_escondida():
    matriz_esc=[]
    for col in range(6):
        lista=[]
        for ren in range(6):
            lista.append('x')
        matriz_esc.append(lista)
    return(matriz_esc)


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