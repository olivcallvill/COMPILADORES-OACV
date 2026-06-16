def lexico(codigo):
    codigo = codigo + ""
    n = len(codigo)
    i = 0
    tokens = []
    estado = 0
    lexema = ""
    while i < n:
        c = codigo[i]
        if estado == 0:
            if codigo[i:i+8] == 'declarar':
                estado = -1
                i = i + 8
                continue
            elif codigo[i:i+6] == 'entero':
                estado = -2
                i = i + 6
                continue
            elif codigo[i:i+4] == 'real':
                estado = -3
                i = i + 4
                continue
            elif codigo[i:i+6] == 'cadena':
                estado = -4
                i = i + 6
                continue
            elif codigo[i:i+8] == 'booleano':
                estado = -5
                i = i + 8
                continue
            elif codigo[i:i+4] == 'leer':
                estado = -6
                i = i + 4
                continue
            elif codigo[i:i+7] == 'escribir':
                estado = -7
                i = i + 7
                continue
            elif codigo[i:i+2] == 'si' and (i+2 >= n or not codigo[i+2].isalpha()):
                estado = -8
                i = i + 2
                continue
            elif codigo[i:i+7] == 'entonces':
                estado = -9
                i = i + 7
                continue
            elif codigo[i:i+4] == 'sino':
                estado = -10
                i = i + 4
                continue
            elif codigo[i:i+5] == 'fin si':
                estado = -11
                i = i + 5
                continue
            elif codigo[i:i+8] == 'mientras':
                estado = -12
                i += i + 8
                continue
            elif codigo[i:i+11] == 'fin mientras':
                estado = -13
                i = i + 11
                continue
            elif codigo[i:i+7] == 'funcion':
                estado = -14
                i = i + 7
                continue
            elif codigo[i:i+11] == 'fin funcion':
                estado = -15
                i = i + 11
                continue
            elif codigo[i:i+8] == 'retornar':
                estado = -16
                i = i + 8
                continue
            elif codigo[i:i+1] == 'y' and (i+1 >= n or not codigo[i+1].isalpha()):
                estado = -17
                i = i + 1
                continue
            elif codigo[i:i+1] == 'o' and (i+1 >= n or not codigo[i+1].isalpha()):
                estado = -18
                i = i + 1
                continue
            elif codigo[i:i+2] == 'no' and (i+2 >= n or not codigo[i+2].isalpha()):
                estado = -19
                i = i + 2
                continue
            elif codigo[i:i+9] == 'verdadero':
                estado = -20
                i = i + 9
                continue
            elif codigo[i:i+5] == 'falso':
                estado = -21
                i = i + 5
                continue
            elif codigo[i:i+2] == '>=':
                estado = -40
                i = i + 2
                continue
            elif codigo[i:i+2] == '<=':
                estado = -41
                i = i + 2
                continue
            elif codigo[i:i+2] == '==':
                estado = -42
                i = i + 2
                continue
            elif codigo[i:i+2] == '!=':
                estado = -43
                i = i + 2
                continue
            elif c == '+':
                estado = -44
                i = i + 1
                continue
            elif c == '-':
                estado = -45
                i = i + 1
                continue
            elif c == '*':
                estado = -46
                i = i + 1
                continue
            elif c == '/':
                estado = -47
                i = i + 1
                continue
            elif c == '%':
                estado = -48
                i = i + 1
                continue
            elif c == '>':
                estado = -49
                i = i + 1
                continue
            elif c == '<':
                estado = -50
                i = i + 1
                continue
            elif c == '=':
                estado = -51
                i = i + 1
                continue
            elif c == ',':
                estado = -52
                i = i + 1
                continue
            elif c == ':':
                estado = -53
                i = i + 1
                continue
            elif c == ';':
                estado = -54
                i = i + 1
                continue
            elif c == '(':
                estado = -55
                i = i + 1
                continue
            elif c == ')':
                estado = -56
                i = i + 1
                continue
            elif c == '"':
                i = i + 1
                estado = 7
                continue
            elif c.isdigit():
                i = i + 1
                estado = 3
                continue
            elif c.isalpha():
                i = i + 1
                estado = 4
                continue
            elif c.isspace():
                i = i + 1
            else:
                return f'ERROR LEXICO: Caracter "{c}" no valido'
        elif estado == 3:
            if c.isdigit():
                i = i + 1
                estado = 3
            elif c == '.':
                i = i + 1
                estado = 5
            else:
                tokens.append(700)
                estado = 0  
        elif estado == 4:
            if c.isalpha() or c.isdigit() or c == '_':
                i = i + 1
                estado = 4
            else:
                tokens.append(1000)
                estado = 0
        elif estado == 5:
            if c.isdigit():
                i = i + 1
                estado = 6
            else:
                return 'ERROR LEXICO: Se esperaba digito despues del punto'  
        elif estado == 6:
            if c.isdigit():
                i = i + 1
                estado = 6
            else:
                tokens.append(701)
                estado = 0 
        elif estado == 7:
            if c == '"':
                tokens.append(702)
                estado = 0
                i = i + 1
            else:
                i = i + 1
                estado = 7
        elif estado == -1:
            tokens.append(201)
            estado = 0
        elif estado == -2:
            tokens.append(202)
            estado = 0
        elif estado == -3:
            tokens.append(203)
            estado = 0
        elif estado == -4:
            tokens.append(204)
            estado = 0
        elif estado == -5:
            tokens.append(205)
            estado = 0
        elif estado == -6:
            tokens.append(206)
            estado = 0
        elif estado == -7:
            tokens.append(207)
            estado = 0
        elif estado == -8:
            tokens.append(208)
            estado = 0
        elif estado == -9:
            tokens.append(209)
            estado = 0
        elif estado == -10:
            tokens.append(210)
            estado = 0
        elif estado == -11:
            tokens.append(211)
            estado = 0
        elif estado == -12:
            tokens.append(212)
            estado = 0
        elif estado == -13:
            tokens.append(213)
            estado = 0
        elif estado == -14:
            tokens.append(214)
            estado = 0
        elif estado == -15:
            tokens.append(215)
            estado = 0
        elif estado == -16:
            tokens.append(216)
            estado = 0
        elif estado == -17:
            tokens.append(217)
            estado = 0
        elif estado == -18:
            tokens.append(218)
            estado = 0
        elif estado == -19:
            tokens.append(219)
            estado = 0
        elif estado == -20:
            tokens.append(703)
            estado = 0
        elif estado == -21:
            tokens.append(704)
            estado = 0
        elif estado == -40:
            tokens.append(307)
            estado = 0
        elif estado == -41:
            tokens.append(308)
            estado = 0
        elif estado == -42:
            tokens.append(309)
            estado = 0
        elif estado == -43:
            tokens.append(310)
            estado = 0
        elif estado == -44:
            tokens.append(300)
            estado = 0
        elif estado == -45:
            tokens.append(301)
            estado = 0
        elif estado == -46:
            tokens.append(302)
            estado = 0
        elif estado == -47:
            tokens.append(303)
            estado = 0
        elif estado == -48:
            tokens.append(304)
            estado = 0
        elif estado == -49:
            tokens.append(305)
            estado = 0
        elif estado == -50:
            tokens.append(306)
            estado = 0
        elif estado == -51:
            tokens.append(403)
            estado = 0
        elif estado == -52:
            tokens.append(400)
            estado = 0
        elif estado == -53:
            tokens.append(401)
            estado = 0
        elif estado == -54:
            tokens.append(402)
            estado = 0
        elif estado == -55:
            tokens.append(404)
            estado = 0
        elif estado == -56:
            tokens.append(405)
            estado = 0
    return tokens
codigo = '''
            funcion esPar(n: entero): entero
                si n % 2 = 0 entonces
                    retornar 1
                sino
                    retornar 0
                fin si
            fin funcion
    
            declarar numero: entero
            declarar texto: cadena
            texto = "Ingrese un numero: "
            escribir texto
            leer numero
            si esPar(numero) = 1 entonces
                escribir "El numero ", numero, " es par"
            sino
                escribir "El numero ", numero, " es impar"
            fin si
    '''
print(lexico(codigo))
