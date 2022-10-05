from turtle import pos
import graphviz

arbol = []
cadena = []
indices = []
cadena_indices = []
arbol_indice = []
postfix_respaldo = []

def Grafo(postfix):
    postfix_respaldo.extend(postfix)
    # print('postfix, ',postfix)
    #asigancion de indices
    counter = 0
    for x in postfix:
        indices.append(counter)
        counter +=1
    # print('indices,',indices)
    
    ignore = True
    restart = True
    while restart:
        restart = False
        for x in range(len(postfix)):
            print('postfix value: ', postfix[x])
            print('postif process', postfix)
            print('arbol process', arbol)
            print('arbol indice process', arbol_indice)
            print('____')
            # print(x)
            # print(postfix)
            # print('postfix: ',postfix[x])
            # print("arbol: ", arbol)
            cadena = []
            cadena_indices = []
            if postfix[x] == '<=>':
                if x-2 >= 0:
                    cadena.append(postfix[x-2])
                    cadena.append(postfix[x])
                    cadena.append(postfix[x-1]) 
                    arbol.append(cadena)
                    postfix[x-2:x+1] = [cadena[1]]
                    cadena_indices.append(indices[x-2])
                    cadena_indices.append(indices[x])
                    cadena_indices.append(indices[x-1])
                    arbol_indice.append(cadena_indices)
                    indices[x-2:x+1] = [cadena_indices[1]]
                    restart = True
                    break
            elif postfix[x] =='=>':
                if x-2 >= 0:
                    cadena.append(postfix[x-2])
                    cadena.append(postfix[x])
                    cadena.append(postfix[x-1]) 
                    arbol.append(cadena)
                    postfix[x-2:x+1] = [cadena[1]]
                    cadena_indices.append(indices[x-2])
                    cadena_indices.append(indices[x])
                    cadena_indices.append(indices[x-1])
                    arbol_indice.append(cadena_indices)
                    indices[x-2:x+1] = [cadena_indices[1]]
                    restart = True
                    break
            elif postfix[x] =='o':
                if x-2 >= 0:
                    cadena.append(postfix[x-2])
                    cadena.append(postfix[x])
                    cadena.append(postfix[x-1]) 
                    arbol.append(cadena)
                    postfix[x-2:x+1] = [cadena[1]]
                    cadena_indices.append(indices[x-2])
                    cadena_indices.append(indices[x])
                    cadena_indices.append(indices[x-1])
                    arbol_indice.append(cadena_indices)
                    indices[x-2:x+1] = [cadena_indices[1]]
                    restart = True
                    break
                
            elif postfix[x] =='~':
                if ignore:
                    cadena.append(postfix[x-1])
                    cadena.append(postfix[x])
                    arbol.append(cadena)
                    postfix[x-1:x+1] = [cadena[1]]
                    cadena_indices.append(indices[x-1])
                    cadena_indices.append(indices[x])
                    arbol_indice.append(cadena_indices)
                    indices[x-1:x+1] = [cadena_indices[1]]
                    ignore = False
                    restart = True
                    break
                else:
                    ignore = True
                
            elif postfix[x] =='^':
                if x-2 >= 0:
                    cadena.append(postfix[x-2])
                    cadena.append(postfix[x])
                    cadena.append(postfix[x-1]) 
                    arbol.append(cadena)
                    postfix[x-2:x+1] = cadena[1]
                    cadena_indices.append(indices[x-2])
                    cadena_indices.append(indices[x])
                    cadena_indices.append(indices[x-1])
                    arbol_indice.append(cadena_indices)
                    indices[x-2:x+1] = [cadena_indices[1]]
                    restart = True
                    break
            elif len(postfix) == 1:
                cadena.append(postfix[0])
                arbol.append(cadena)
                cadena_indices.append(indices[0])
                arbol_indice.append(cadena_indices)

    print('postfix respaldo,', postfix_respaldo)
    print('indices finales, ', arbol_indice)
    print('arbol final: ', arbol)
    #construccion de su grafo
    
    f = graphviz.Digraph(comment = "arbol")

    for x in range(counter):
        if str(postfix_respaldo[x]) == "<=>":
            f.node(str(x),label="↔",shape ="circle")
        else:
            f.node(str(x),label=str(postfix_respaldo[x]),shape ="circle")
    
    for l in range(len(arbol_indice)): #los nodos  
        if len(arbol_indice[l]) == 2:          
            f.edge(str(arbol_indice[l][1]),str(arbol_indice[l][0]))
        elif len(arbol_indice[l]) == 1:
            f.node(str(arbol_indice[l][0]))
        else:
            f.edge(str(arbol_indice[l][1]),str(arbol_indice[l][0]))
            f.edge(str(arbol_indice[l][1]),str(arbol_indice[l][2]))
    f.render("arbol", view = True)

            



