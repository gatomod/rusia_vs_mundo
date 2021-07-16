###################################
###  RUSIA VS. MUNDO (MIT Lic.) ###
###################################
# No garantizo que el ingles este bien ni que esto funcione xd
# Puede que lo suba a GitHub
# Rusia vs. Mundo

# TODO poder elegir país

# Lib
from os import name, system
from time import sleep


# Funciones
def clear():        # Limpiar consola
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def countryPower( n1, n2, n3, n4 ):     # Determinar potencial de un país
    t = n1 + n2 + n3 + n4
    if t < 100:
        return ['Bajo', 0]
    elif t >= 100 and t < 300:
        return ['Medio', 1]
    else:
        return ['Alto', 2]

def ok():           # Literalmente una función basura
    return True


# Variables iniciales
infPower = 15
flightPower = 15
marinePower = 10
nuclearPower = 5
power = countryPower(infPower, flightPower, marinePower, nuclearPower)

# Como no se como hacer objetos como los de JS usare un array
# Indices:
# 0: nombre     
# 1: codigo     
# 2: potencia infanteria      
# 3: pot. fuerza aerea    
# 4: pot. marina      
# 5: pot. nuclear
# 6: emoji
ussr = [
    'URSS',
    'ussr',
    infPower,
    flightPower,
    marinePower,
    nuclearPower
]
uk = [ 'Reino Unido', 'uk', 85, 70, 75, 5, '🍵' ]
dl = [ 'Alemania', 'dl', 60, 30, 38, 2, '🍺' ]
usa = [ 'Estados Unidos', 'usa', 90, 80, 85, 95, '🍔' ]
es = [ 'España', 'es', 40, 20, 25, 0, '🆙' ]
fr = [ 'Francia', 'fr', 50, 70, 40, 10, '🥖' ]
jp = [ 'Japón', 'jp', 80, 40, 70, 40, '🍣' ]
sl = [ 'Suiza', 'sl', 30, 0, 40, 0, '🏔 ' ]
br = [ 'Brasil', 'br', 50, 40, 60, 5, '⚽' ]
bg = [ 'Casa de Bill Gates', 'bg', 0, 0, 0, 0, '🏡' ]
ch = [ 'China', 'ch', 99, 95, 87, 90, '🍚' ]
god = [ 'Dios', 'god', 100, 100, 100, 99, '🙏' ]
tk = [ 'Turquía', 'tk', 70, 50, 60, 10, '🥙' ]
sa = [ 'Sudáfrica', 'sa', 50, 35, 40, 0, '🏆' ]
ve = [ 'Venezuela', 've', 40, 20, 15, 0, '🛢 ' ]
nk = [ 'Corea del Norte', 'nk', 90, 85, 80, 70, '🚀' ]
an = [ 'Andorra', 'an', 10, 0, 15, 2, '📺' ]
ar = [ 'Argentina', 'ar', 30, 10, 25, 0, '🥩' ]
fp = [ 'Filipinas', 'fp', 10, 5, 5, 0, '🏖 ' ]
nv = [ 'NVIDIA GeForce RTX 3080 Ti', 'nv', 0, 0, 0, 1, '⛏ ' ]

allCountries = [uk, dl, usa, es, fr, jp, sl, br, bg, ch, god, tk, sa, ve, nk, an, ar, fp, nv]


# CLI

# Introducción
clear()
print('  _____           _                       __  __                 _       ')
print(' |  __ \         (_)                     |  \/  |               | |      ')
print(' | |__) |   _ ___ _  __ _  __   _____    | \  / |_   _ _ __   __| | ___  ')
print(' |  _  / | | / __| |/ _` | \ \ / / __|   | |\/| | | | | \'_ \ / _` |/ _ \ ')
print(' | | \ \ |_| \__ \ | (_| |  \ V /\__ \_  | |  | | |_| | | | | (_| | (_) |')
print(' |_|  \_\__,_|___/_|\__,_|   \_/ |___(_) |_|  |_|\__,_|_| |_|\__,_|\___/ ')
print('\nBienvenid@ a "Rusia vs. Mundo", un juego en linea de comando para conquistar todo el mundo. A continuación le diré alguna información')
input('Pulse enter para continuar...')
print('\nUsted poseerá el control de la URSS. Su labor es administrar el ejército para conquistar todo el mundo')
print('Cualquier ejército tiene un poder de hasta 400 puntos repartidos en 4 apartados (infantería, fuerza aérea, marina y poder nuclear)')
print('Tiene la opción de atacar a un país y saber su potencia militar. Si ve que no posee el poder suficiente para ganar puede elegir otro país')
print('Dicho esto, empecemos!!!')
input('Pulse enter para continuar... ')


exit = False
while exit == False:
    

    if len(allCountries) == 0:
        clear()
        print('😄🎉🎶 Felicidades mi camarada, ha conquistado TODO EL MUNDO!!!')
        print('\n··· EL MUNDO ES SUYO!!! ···\n')
        input('Pulse enter para salir del juego... ')
        exit = True
        # FIN DEL PROGRAMA

    elif infPower + flightPower + marinePower + nuclearPower <= 0:
        clear()
        print('😞 Lo sentimos pero no ha sido capaz de conquistar el mundo a causa de que su ejército está prácticamente agotado')
        print('\n··· FIN DEL JUEGO ···\n')
        input('Pulse enter para salir del juego... ')
        exit = True
        # FIN DEL PROGRAMA

    else:
        # Inicio
        clear()
        print('··· INICIO ···')
        print('| 🥃 🛠  Buenos dias camarada ruso. Le informo un poco')
        print('\n| 🌩  Poder:', power[0])
        print('| 🔫 Infantería: ', infPower,'/ 100')
        print('| 🛩  Fuerza aérea: ', flightPower,'/ 100')
        print('| 🛳  Marina: ', marinePower,'/ 100')
        print('| 💣 Poder nuclear: ', infPower,'/ 100')
        readyToAttack = input('\n❓ Listo para atacar? (S/n): ').lower()
        if readyToAttack == 'n':
            print('Hasta luego camarada ;D')
            exit = True
            # FIN DEL PROGRAMA

        else:
            # Menú de selección e info de países
            warMenu = False
            while warMenu == False:
                countryChooserLoop = False
                while countryChooserLoop == False:
                    # Selector de país
                    clear()
                    print('··· SELECTOR DE PAÍS ···')
                    print('🌍 A continuación le voy a mostrar un listado de países que puede atacar')
                    print('Ingrese el código del país, recibirá información y podrá decidir atacar o no')
                    input('Pulse enter para continuar... ')

                    for i in range(len(allCountries)):
                        print('|',allCountries[i][6], allCountries[i][0], '(', allCountries[i][1], ')')

                    # Verificador de país
                    endChoose = False
                    while endChoose == False:
                        choose = input('❓ Introduce el código del país: ').lower()
                        for i in range(len(allCountries)):
                            if choose == allCountries[i][1]:
                                endChoose = True
                                countryChooserLoop = True
                        print('Escriba un código de país válido')



                    

                    clear()
                    # Busqueda de país según el código
                    findChoose = False
                    while findChoose == False:
                        for i in range(len(allCountries)):
                            if allCountries[i][1] == choose:
                                enemyName = allCountries[i][0]
                                enemyCode = allCountries[i][1]
                                enemyInf = allCountries[i][2]
                                enemyFlight = allCountries[i][4]
                                enemyMarine = allCountries[i][3]
                                enemyNuclear = allCountries[i][5]
                                enemyEmoji = allCountries[i][6]
                                enemyPower = countryPower(enemyInf, enemyFlight, enemyMarine, enemyNuclear)
                                findChoose = True
                    print('Has elegido', enemyName)
                    print('\n··· INFO ···')
                    print('|', enemyEmoji ,'Nombre:', enemyName, '| Código:', enemyCode, '| Poder:', enemyPower[0])
                    print('| 🔫 Infantería:', enemyInf, '/ 100')
                    print('| 🛩  Fuerza aérea:', enemyFlight, '/ 100')
                    print('| 🛳  Marina:', enemyMarine, '/ 100')
                    print('| 💣 Poder nuclear:', enemyNuclear, '/ 100')
                    if enemyPower[1] <= power[1]:
                        print('| ✅ Posibilidades de ganar: Sí')
                    else:
                        print('| ❎ Posibilidades de ganar: No')
                    
                    preconfirm = input('\n❓ Desea atacar? (s/N): ').lower()
                    if preconfirm == 's':
                        confirm = input('❓ Está seguro? (s/N): ').lower()
                        if confirm == 's':
                            warMenu = True
                        
                            
                        

            # LUCHA
            # animación
            gun = [
                '                 ', '                 ', '  -              ',
                '    -            ', '      -          ', '        -        ',
                '          -      ', '            -    ', '              -  ',
                '                -', '               💣', '               ✨',
                '               🎆', '                 ', '                -',
                '              -  ', '            -    ', '          -      ',
                '        -        ', '      -          ', '    -            ',
                '  -              ', '-                ', '💣               ',
                '✨               ', '🎆               ',
            ]

            for i in range(0, 3):
                for i in range(0, 26):
                    clear()
                    print('Luchando...')
                    print('😐',gun[i],'😑')
                    sleep(0.15)

            # Algoritmo de lucha
            clear()
            enemy = enemyInf + enemyFlight + enemyMarine + enemyNuclear
            russian = infPower + flightPower + marinePower + nuclearPower

            # Derrota
            if enemy > russian:
                infPower -= (enemyInf - infPower)
                flightPower -= (enemyFlight - flightPower)
                marinePower -= (enemyMarine - marinePower)
                nuclearPower -= (enemyNuclear - nuclearPower)
                # Actualizar puntos
                power = countryPower(infPower, flightPower, marinePower, nuclearPower)
                print('··· RESULTADO DE LA GUERRA ···')
                print('| 🎖 Ganador: ', enemyName)
                print('| 😓 HA PERDIDO')
                print('\n··· Puntos')
                print('| 📉 Sus puntos han descendido a', infPower + flightPower + marinePower + nuclearPower, '/ 400 (', power[0], ')')

            # Empate (sube unos puntos de regalo)
            elif enemy == russian:
                if infPower < 100:
                    infPower += 5
                if flightPower < 100:
                    flightPower += 5
                if marinePower < 100:
                    marinePower += 5
                if nuclearPower < 100:
                    nuclearPower += 5
                # Actualizar puntos
                power = countryPower(infPower, flightPower, marinePower, nuclearPower)
                print('··· RESULTADO DE LA GUERRA ···')
                print('| 🎖 Ganador: Ambos')
                print('| 🤝 EMPATE')
                print('\n··· Puntos')
                print('| 📈 Sus puntos han aumentado ligeramente a', infPower + flightPower + marinePower + nuclearPower, '/ 400 (', power[0], ')')
            
            # Victoria
            else:
            	# Sumar puntos solo si tienen menos de 100 puntos
                if infPower < 100:
                    infPower = infPower + (enemyInf // 2) + 5
                if flightPower < 100:
                    flightPower = flightPower + (enemyFlight // 2) + 5
                if marinePower < 100:
                    marinePower = marinePower + (enemyMarine // 2) + 5
                if nuclearPower < 100:
                    nuclearPower = nuclearPower + (enemyNuclear // 2) + 5
                	
                
                # Actualizar puntos
                power = countryPower(infPower, flightPower, marinePower, nuclearPower)
                

                # Búsqueda del enemigo según el código para excluir de la lista de paises

                exclude = False
                i = 0
                while exclude == False:
                    if allCountries[i][1] == enemyCode:
                        allCountries.pop(allCountries.index(allCountries[i]))
                        exclude = True
                    i += 1

                            

                print('··· RESULTADO DE LA GUERRA ···')
                print('| 🎖 Ganador: URSS')
                print('| 🏆 HA GANADO!!!')
                print('\n··· Puntos')
                print('| 📈 Sus puntos han ascendido a', infPower + flightPower + marinePower + nuclearPower, '/ 400 (', power[0], ')')
            
            # Retorno al inicio
            input('\n\nPulse enter para volver al inicio... ')
            
# xd