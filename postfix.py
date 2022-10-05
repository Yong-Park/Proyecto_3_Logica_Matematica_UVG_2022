
cadena_post = []
pila = []

caracter = []
nueva_cadena = []
negaciones = []
variables = ['p','q','r','s','t','u','v','w','x','y','z']
indices = []
chain = []

def Postfix(cadena):
    existe_variable = False
    #conectarlo correctamente
    for i in range(len(cadena)):
        # print('_______')
        # print(cadena)
        # print(cadena[i])
        # print("indices: ",indices)
        nueva_cadena.append(cadena[i])
        if existe_variable:
            nueva_cadena.append(negaciones[len(negaciones)-1])
            negaciones.pop(len(negaciones)-1)
            existe_variable = False
        # print("cadena armandose: ", nueva_cadena)
        if cadena[i] == '>':
            nueva_cadena.reverse()
            caracter.append(nueva_cadena[0])
            nueva_cadena.pop(0)
            caracter.append(nueva_cadena[0])
            nueva_cadena.pop(0)
            if nueva_cadena[0] == '<':
                caracter.append(nueva_cadena[0])
                nueva_cadena.pop(0)
            nueva_cadena.reverse()
            caracter.reverse()
            unido = ''.join(caracter)
            nueva_cadena.append(unido)
            caracter.clear()
        elif cadena[i] == '~':
            if cadena[i+1] == '(':
                negaciones.append(cadena[i])
                nueva_cadena.pop(len(nueva_cadena)-1)
            elif cadena[i+1] == '~':
                negaciones.append(cadena[i])
                nueva_cadena.pop(len(nueva_cadena)-1)
            elif cadena[i+1] in variables:
                negaciones.append(cadena[i])
                nueva_cadena.pop(len(nueva_cadena)-1)
                existe_variable = True
        elif cadena[i] == ')':
            if cadena[indices[len(indices)-1]-1] == '~':
                 nueva_cadena.append(negaciones[len(negaciones)-1])
                 negaciones.pop(len(negaciones)-1)
            indices.pop(len(indices)-1)
        elif cadena[i] == '(':
            indices.append(i)
    if negaciones:
        nueva_cadena.extend(negaciones)
                
    print("nueva cadena: ", nueva_cadena)
    #transformacion a postfix
    for i in nueva_cadena:
        # print("pila: ", pila)
        # print("postfix: ", cadena_post)
        # print("________________")
        if i == '<=>' or i =='=>'or i =='('or i ==')'or i =='o'or i =='~'or i =='^':
            pila.append(i)
            if i == ')':
                pila.reverse()
                # print(pila)
                contador = 1
                for x in pila:
                    if x != ')':
                        if x == '(':
                            contador +=1
                            break
                        else:
                            cadena_post.append(x)
                            contador += 1
                # print(contador)
                for x in range(contador):
                    pila.pop(0)
                pila.reverse()
            elif i == '=>':
                pass
        else:
            cadena_post.append(i)
        # print('pila: ',pila)

    if pila:
        cadena_post.extend(pila)
    print('cadena:' , cadena_post)
    print('________')
    return cadena_post