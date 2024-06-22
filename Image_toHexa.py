from PIL import Image
import cv2
from colorsys import hsv_to_rgb


def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Pasar a Hexadecimal Ampliado', accion1),
        '2': ('Pasar a Hexadecimal Simplificado', accion2),
        '3': ('Pasar al nombre del color del pixel', accion3),
        '4': ('Pasar al nibble del hexadecimal del pixel', accion4),
        '5': ('Pasar de Codigo simplificado a Imagen', accion5),
        '6': ('Pasar de Codigo amplificado a Imagen', accion6),
        '7':('Salir', salir)
    }

    generar_menu(opciones, '7')

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def fhex_to_whex(str):
    if str == "#000000": #black
        return "0"
    if str == "#0000aa": #dark_blue
        return "1"
    if str == "#00aa00": #dark_green
        return "2"
    if str == "#00aaaa": #dark_cyan
        return "3"
    if str == "#aa0000": #dark_red
        return "4"
    if str == "#aa00aa": #dark_magenta
        return "5"
    if str == "#aa5500": #brown
        return "6"
    if str == "#aaaaaa": #light_gray
        return "7"
    if str == "#555555": #dark_gray
        return "8"
    if str == "#5555ff": #light_blue
        return "9"
    if str == "#55ff55": #light_green
        return "A"
    if str == "#55ffff": #light_cyan
        return "B"
    if str == "#ff5555": #light_red
        return "C"
    if str == "#ff55ff": #light_magenta
        return "D"
    if str == "#ffff55": #yellow
        return "E"
    if str == "#ffffff": #white
        return "F"

        
def hex_to_ncolor(str):
    if str == "#000000": #black
        return "Negro"
    if str == "#0000aa": #dark_blue
        return "Azul oscuro"
    if str == "#00aa00": #dark_green
        return "Verde oscuro"
    if str == "#00aaaa": #dark_cyan
        return "Cyan oscuro"
    if str == "#aa0000": #dark_red
        return "Rojo"
    if str == "#aa00aa": #dark_magenta
        return "Magenta"
    if str == "#aa5500": #brown
        return "Cafe"
    if str == "#aaaaaa": #light_gray
        return "Gris claro"
    if str == "#555555": #dark_gray
        return "Gris oscuro"
    if str == "#5555ff": #light_blue
        return "Azul claro"
    if str == "#55ff55": #light_green
        return "Verde claro"
    if str == "#55ffff": #light_cyan
        return "Cyan claro"
    if str == "#ff5555": #light_red
        return "Rosa"
    if str == "#ff55ff": #light_magenta
        return "Magenta claro"
    if str == "#ffff55": #yellow
        return "Amarillo"
    if str == "#ffffff": #white
        return "Blanco"

def hex_to_nibble(str):
    if str == "#000000": #black
        return "0000"
    if str == "#0000aa": #dark_blue
        return "0001"
    if str == "#00aa00": #dark_green
        return "0010"
    if str == "#00aaaa": #dark_cyan
        return "0011"
    if str == "#aa0000": #dark_red
        return "0100"
    if str == "#aa00aa": #dark_magenta
        return "0101"
    if str == "#aa5500": #brown
        return "0110"
    if str == "#aaaaaa": #light_gray
        return "0111"
    if str == "#555555": #dark_gray
        return "1000"
    if str == "#5555ff": #light_blue
        return "1001"
    if str == "#55ff55": #light_green
        return "1010"
    if str == "#55ffff": #light_cyan
        return "1011"
    if str == "#ff5555": #light_red
        return "1100"
    if str == "#ff55ff": #light_magenta
        return "1101"
    if str == "#ffff55": #yellow
        return "1110"
    if str == "#ffffff": #white
        return "1111"

def shex_to_lhex(str):    
    if str == "0": #black
        return "000000"
    if str == "1": #dark_blue
        return "0000aa"
    if str == "2": #dark_green
        return "00aa00"
    if str == "3": #dark_cyan
        return "00aaaa"
    if str == "4": #dark_red
        return "aa0000"
    if str == "5": #dark_magenta
        return "aa00aa"
    if str == "6": #brown
        return "aa5500"
    if str == "7": #light_gray
        return "aaaaaa"
    if str == "8": #dark_gray
        return "555555"
    if str == "9": #light_blue
        return "5555ff"
    if str == "A": #light_green
        return "55ff55"
    if str == "B": #light_cyan
        return "55ffff"
    if str == "C": #light_red
        return "ff5555"
    if str == "D": #light_magenta
        return "ff55ff"
    if str == "E": #yellow
        return "ffff55"
    if str == "F": #white
        return "ffffff"
    
def accion1():
    
    hexData = ' '
    
    print('Ingrese la ruta de la imagen a transformar')
    route = input()
    my_route = route
    
    img = cv2.imread(my_route)
    
    print('Mostrando el codigo completo hexadecimal')

    for x in range(16):
        for y in range(16):
            print("Fila ", + x, " Columna ", + y, " Color en Hex: ", rgb_to_hex((img[x,y][2]), (img[x,y][1]), (img[x,y][0])))
            hexData += rgb_to_hex((img[x,y][2]), (img[x,y][1]), (img[x,y][0]))

    hexData=hexData.strip()
    hexData=hexData.replace(' ', '')
    hexData=hexData.replace('#', '')        
    print("-----------------------------------")
    print(hexData)
    

def accion2():
    
    print('Ingrese la ruta de la imagen a transformar')
    route = input()
    my_route = route
    img = cv2.imread(my_route)
    
    print('Mostrando la forma simplificada el codigo hexadecimal: ')

    for x in range(16):      # this row
        for y in range(16):   # and this row was exchanged
            print("Fila ", + x, " Columna ", + y, " Color en Hex: ", fhex_to_whex(rgb_to_hex((img[x,y][2]), (img[x,y][1]), (img[x,y][0]))))
    
    simpleHexdata = ""
        
    for x in range(16):      # this row
        for y in range(16):   # and this row was exchanged
            simpleHexdata += fhex_to_whex(rgb_to_hex((img[x,y][2]), (img[x,y][1]), (img[x,y][0])))

    print("-----------------------------------")
    print(simpleHexdata)

def accion3():
    
    print('Ingrese la ruta de la imagen a transformar')
    route = input()
    my_route = route
    img = cv2.imread(my_route)
    
    print('Mostrando el nombre del color')
    
    for x in range(16):      # this row
        for y in range(16):   # and this row was exchanged
            print("Fila ", + x, " Columna ", + y, " Color en Hex: ", hex_to_ncolor(rgb_to_hex((img[x,y][2]), (img[x,y][1]), (img[x,y][0]))))

def accion4():
    
    print('Ingrese la ruta de la imagen a transformar')
    route = input()
    my_route = route
    img = cv2.imread(my_route)
    
    print('Mostrando los nibbles')
    
    for x in range(16):      # this row
        for y in range(16):   # and this row was exchanged
            print("Fila ", + x, " Columna ", + y, " Color en Hex: ", hex_to_nibble(rgb_to_hex((img[x,y][2]), (img[x,y][1]), (img[x,y][0]))))

def accion5():
    
    print('Ingresa el codigo simlificado a transformar a imagen')
    code = input()
    hexData = code.replace("0", "000000").replace("1", "0000aa").replace("2", "00aa00").replace("3", "00aaaa").replace("4", "aa0000").replace("5", "aa00aa").replace("6", "aa5500").replace("7", "aaaaaa").replace("8", "555555").replace("9", "5555ff").replace("A", "55ff55").replace("B", "55ffff").replace("C", "ff5555").replace("D", "ff55ff").replace("E", "ffff55").replace("F", "ffffff")
        
        
    # Convert hexadecimal string to list of integers
    input_bytes = bytes.fromhex(hexData)
    input_data = list(input_bytes)

    # Make some RGB values. 
    # Cycle through hue vertically & saturation horizontally

    for hue in range(360):
        for sat in range(100):
            # Convert color from HSV to RGB
            rgb = hsv_to_rgb(hue/360, sat/100, 1)
            rgb = [int(0.5 + 255*u) for u in rgb]
            input_data.extend(rgb)

    # Convert list to bytes
    colors = bytes(input_data)
    img = Image.frombytes('RGB', (16, 16), colors)
    img.save('new_image.png')
    
    print("Se ha creado la imagen :3, revisa la carpeta donde se encuentra el proyecto el nombre: new_image.png")
    
def accion6():
    
    print('Ingresa el codigo amplificado a transformar a imagen')
    
    hexData = input()
        
    # Convert hexadecimal string to list of integers
    input_bytes = bytes.fromhex(hexData)
    input_data = list(input_bytes)

    # Make some RGB values. 
    # Cycle through hue vertically & saturation horizontally

    for hue in range(360):
        for sat in range(100):
            # Convert color from HSV to RGB
            rgb = hsv_to_rgb(hue/360, sat/100, 1)
            rgb = [int(0.5 + 255*u) for u in rgb]
            input_data.extend(rgb)

    # Convert list to bytes
    colors = bytes(input_data)
    img = Image.frombytes('RGB', (16, 16), colors)
    img.save('new_image.png')
    
    print("Se ha creado la imagen :3, revisa la carpeta donde se encuentra el proyecto el nombre: new_image.png")    
    
def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()