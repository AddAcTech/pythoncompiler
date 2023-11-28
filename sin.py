import re

def analizador_sintactico(tokens):
    reglas_sintacticas = {
        'DECLARACION': r'TYPE\s+ID(?:\s+ASIG\s+(NUM|FLOAT))?(?:\s*COMA\s*ID(?:\s+ASIG\s+(NUM|FLOAT))?)*\s+ENDL',
        'ASIGNACION': r'ID ASIG (NUM|FLOAT) ENDL',
        'IGUALDAD': r'ID REL (NUM|FLOAT) ENDL',
        'LIBRARY': r'ID REL ID REL',
        'FUNCTION': r'TYPE\s+ID\s+PA\s+PC\s+LA',
        'EMPY': r'|LA|LC',
        'DO': r'ID DO|ID DO LA',
        'DO': r'(\s)*ID DO|DO LA',
        'FOR': r'FOR\s+PA\s+(TYPE\s+ID\s+ASIG\s+NUM\s+ENDL|ID\s+ASIG\s+NUM\s+ENDL)\s+ID\s+REL\s+ID\s+ENDL\s+ID\s+(ARIT\s+ARIT\s+PC|ARIT\s+ARIT\s+PC\s+LA)',
        'FOR': r'FOR\s+PA\s+(TYPE\s+ID\s+ASIG\s+NUM\s+ENDL|ID\s+ASIG\s+NUM\s+ENDL)\s+ID\s+REL\s+ID\s+ENDL\s+ID\s+(ARIT\s+ARIT\s+PC|ARIT\s+ARIT\s+PC\s)',
        'FOR': r'FOR\s+PA\s+(TYPE\s+ID\s+ASIG\s+NUM\s+ENDL|ID\s+ASIG\s+NUM\s+ENDL)\s+ID\s+REL\s+ID\s+ENDL\s+(ARIT\s+ARIT\s+ID\s+PC|ARIT\s+ARIT\s+ID\s+PC\s+LA)',
        'RETURN': r'RET (ID|TRUE|FALSE|NUM)\s*ENDL',
        'COUTCIN': r'IO REL REL (COMILLAS (ID|(ID )*) COMILLAS|ID) ENDL',
        'IF': r'IF PA ID REL (ASIG ASIG (NUM|ID)|ASIG (NUM|ID)) PC LA',
        'IF2': r'IF PA ID REL (ASIG ASIG (NUM|ID)|ASIG (NUM|ID)) PC',
        'WHILE': r'LC WHILE PA ID REL ID PC ENDL',
        'WHILE2': r'WHILE PA ID REL ID PC ENDL',
    }

    num=1
    for tokens_linea in tokens:
        linea = ' '.join(tokens_linea)
        for regla, patron in reglas_sintacticas.items():
            if re.fullmatch(patron, linea):
                print(f"{num} +++  Valida  +++")
                break
        else:
            print(f'{num} --- Invalida ---')
        num=num +1

if __name__ == "__main__":
    archivo_entrada = 'tokens.txt'

    with open(archivo_entrada, 'r') as archivo:
        lineas = archivo.readlines()

    tokens_por_linea = [linea.split() for linea in lineas]

    analizador_sintactico(tokens_por_linea)
