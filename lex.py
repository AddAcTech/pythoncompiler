import re

# Arreglo para almacenar los nombres de las funciones
nombre_de_funciones = []

def analizador_lexico(linea):
    global nombre_de_funciones
    
    # Definir expresiones regulares para diferentes tokens
    patrones = [
        (r'\b(?:int|float|char|double|void)\s+(\w+)\s*\(([^)]*)\)\s*{', 'FUNCT'),  # Funcion
        (r'//[^\n]*', 'COMENT'),  # Comentarios
        (r'\b(int|float|char|double|void)\b', 'TYPE'),  # Tipos de datos
        (r'\b(#include)\b', 'LIB'),  # Palabras reservadas
        (r'\b(return)\b', 'RET'),  # Palabras reservadas
        (r'\b(if|IF)\b', 'IF'),  # Palabras reservadas
        (r'\b(for|FOR)\b', 'FOR'),  # Palabras reservadas
        (r'\b(while|WHILE)\b', 'WHILE'),  # Palabras reservadas
        (r'\b(else|ELSE)\b', 'ELSE'),  # Palabras reservadas
        (r'\b(true|false)\b', 'TF'),  # Valores booleanos
        (r'\b(cin|cout)\b', 'IO'),  # Entrada y salida estándar
        (r'\b[0-9]+\b', 'NUM'),  # Números enteros
        (r'[0-9]+\.[0-9]+', 'FLOAT'),  # Números de punto flotante
        (r'"', 'COMILLAS'),  # Cadenas
        (r'\'(\\\'|[^\'])\'', 'CHAR'),  # Caracteres
        (r'\b(?!int|float|char|double|void|if|else|while|for|return|true|false|cin|cout)\b[a-zA-Z_][a-zA-Z0-9_]*\b', 'ID'), # Identificadores
        (r'==|!=|<|>|<=|>=', 'REL'),  # Operadores relacionales
        (r'[\+\-\*/%]', 'ARIT'),  # Operadores aritméticos
        (r'=|\+=|-=|\*=|/=|%=', 'ASIG'),  # Operadores de asignación
        (r';', 'ENDL'),  # Punto y coma
        (r'(\s)*do(\s)*', 'DO'),  # Punto y coma
        (r',', 'COMA'),  # Coma
        (r'\(', 'PA'),   # Paréntesis abre
        (r'\)', 'PC'),   # Paréntesis cierra
        (r'{', 'LA'),    # Llave abre
        (r'}', 'LC'),    # Llave cierra
        (r'\b(\w+)\s*\(([^)]*)\)\s*;', 'FUNCCALL'),  # Llamada a función
    ]

    tokens = []
    for patron, tipo in patrones:
        regex = re.compile(patron)
        coincidencias = regex.finditer(linea)

        for coincidencia in coincidencias:
            if tipo == 'FUNCT':
                # Almacenar el nombre de la función
                nombre_funcion = coincidencia.group(1)
                nombre_de_funciones.append(nombre_funcion)
                
            elif tipo == 'FUNCCALL':
                # Verificar si la función llamada existe en el arreglo
                nombre_llamada = coincidencia.group(1)
                if nombre_llamada not in nombre_de_funciones:
                    tokens.append(('NODECL', 'NODECL', coincidencia.start()))

            tokens.append((coincidencia.group(), tipo, coincidencia.start()))

    # Ordenar los tokens por su posición de inicio en la línea original
    tokens = sorted(tokens, key=lambda x: x[2])

    return tokens

def analizar_archivo(archivo_entrada, archivo_salida):
    global nombre_de_funciones
    
    with open(archivo_entrada, 'r') as archivo_entrada:
        with open(archivo_salida, 'w') as archivo_salida:
            for linea in archivo_entrada:
                tokens = analizador_lexico(linea.strip())
                for token, tipo, _ in tokens:
                    archivo_salida.write(f'{tipo} ')
                archivo_salida.write('\n')

if __name__ == "__main__":
    archivo_entrada = 'codigo.cpp'
    archivo_salida = 'tokens.txt'
    analizar_archivo(archivo_entrada, archivo_salida)
