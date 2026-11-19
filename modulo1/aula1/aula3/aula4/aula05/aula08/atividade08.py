##diferença entre copy e armazenamento

import random
import aula08_listas

from aula08_listas import *
from aula08_listas import origem_produtos

import pandas as pand

insetos1 ={
"mosca","louva-deus","barata","cachorro do mato"
}

insetos2 = insetos
insetos3 = insetos.copy()

insetos.clear()

print(insetos)
print(insetos2)
print(insetos3)