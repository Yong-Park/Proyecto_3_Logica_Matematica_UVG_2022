from postfix import * 
from grafo import *
#r = "(0=>(ros))"
#r = '~~~q'
#r = '~(p^q)'
#r = '(p<=>~p)'
#r = '(~(p^(qor))os)'
#r = '((p=>q)^p)'
#r = 'p'
r = '(p^q)'

postfix_transformtacion = Postfix(r)

Grafo(postfix_transformtacion)



