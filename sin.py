import re

def analizador_sintactico(tokens):
    reglas_sintacticas = {
        'DECLARACION': r'FUNCT\s+TYPE\s+ID(?:\s+ASIG\s+(NUM|FLOAT))?(?:\s*COMA\s*ID(?:\s+ASIG\s+(NUM|FLOAT))?)*\s+(ENDL|LA)',
        'DECLARACION': r'TYPE\s+ID(?:\s+ASIG\s+(NUM|FLOAT))?(?:\s*COMA\s*ID(?:\s+ASIG\s+(NUM|FLOAT))?)*\s+ENDL',
        'DECLARACION': r'FUNCT TYPE ID PA TYPE ID COMA TYPE ID PC LA',
        'DECLARACION': r'TYPE ID ASIG ID FUNCCALL PA NUM COMA NUM PC ENDL',
        'ASIGNACION': r'ID ASIG (NUM|FLOAT) ENDL',
        'IGUALDAD': r'ID REL (NUM|FLOAT) ENDL',
        'LIBRARY': r'ID REL ID REL',
        'FUNCTION': r'FUNCT\s+TYPE\s+ID\s+PA\s+PC\s+LA',
        'FUNCTION2': r'FUNCT TYPE ID PA PC LA',
        'FUNCTION3': r'FUNCT TYPE ID PA TYPE ID COMA TYPE ID PC LA',
        'FUNCTION4': r'ID FUNCCALL PA NUM COMA NUM PC ENDL',
        'FUNCTION5': r'FUNCT TYPE ID PA ((TYPE ID)*|(COMA TYPE ID)*) PC LA',
        'FUNCTION6': r'FUNCT TYPE ID PA TYPE ID COMA TYPE ID COMA TYPE ID PC LA',
        'EMPY': r'|LA|LC',
        'ELSE': r'ELSE LA',
        'ELSE2': r'ELSE',
        'DO': r'ID DO|ID DO LA',
        'DO2': r'(\s)*ID DO|DO LA',
        'FOR': r'FOR\s+PA\s+(TYPE\s+ID\s+ASIG\s+NUM\s+ENDL|ID\s+ASIG\s+NUM\s+ENDL)\s+ID\s+REL\s+ID\s+ENDL\s+ID\s+(ARIT\s+ARIT\s+PC|ARIT\s+ARIT\s+PC\s+LA)',
        'FOR2': r'FOR\s+PA\s+(TYPE\s+ID\s+ASIG\s+NUM\s+ENDL|ID\s+ASIG\s+NUM\s+ENDL)\s+ID\s+REL\s+ID\s+ENDL\s+ID\s+(ARIT\s+ARIT\s+PC|ARIT\s+ARIT\s+PC\s)',
        'FOR3': r'FOR\s+PA\s+(TYPE\s+ID\s+ASIG\s+NUM\s+ENDL|ID\s+ASIG\s+NUM\s+ENDL)\s+ID\s+REL\s+ID\s+ENDL\s+(ARIT\s+ARIT\s+ID\s+PC|ARIT\s+ARIT\s+ID\s+PC\s+LA)',
        'RETURN': r'RET (ID|TRUE|FALSE|NUM)\s*ENDL',
        'RETURN2': r'RET ID ENDL',
        'RETURN3': r'RET (NUM|ID|CHAR) ENDL',
        'COUTCIN': r'IO REL REL (COMILLAS (ID|(ID )*) COMILLAS|ID) ENDL',
        'IF': r'IF PA ID REL (ASIG ASIG (NUM|ID)|ASIG (NUM|ID)) PC LA',
        'IF2': r'IF PA ID REL (ASIG ASIG (NUM|ID)|ASIG (NUM|ID)) PC',
        'IF3': r'IF PA ID REL ID PC LA',
        'WHILE': r'LC WHILE NODECL FUNCCALL PA ID REL ID PC ENDL',
        'WHILE2': r'WHILE NODECL FUNCCALL PA ID REL ID PC ENDL',
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
