##listats:
#indices    0   1   2   3   4
compras= ["arroz","sabão","pão","açucar","feijão"]

compras2= ["amaciante","papel toalha","farinha","maçã","pão de forma"]
  
print(compras2[0:4:2])

compras_final = compras + compras2
print(compras_final)

compras3=[
    "laranja",
    "maçã",
    "hambuguer",
    "sal"
]

compras_final += compras3
#print(compras_final)

#compras_final += ["café"]
#compras_final.append("café")
compras_final.insert(2,"café")
#print(compras_final)

compras_final.pop(3)
compras_final.remove("maçã")
compras_final.pop()
compras_dezembro=compras_final.copy()
print(compras_dezembro)

compras_final.count("maçã")
compras_final.clear()

print(compras_final)
print(compras_dezembro)

## tuplas:

tupla_compras = tuple(compras_dezembro)
print(tupla_compras)
#tupla_compras.append("saleiro")
#add_tupla=("leite")

#final_tupla = tupla_compra + add_tupla
#print(tupla_compras)

filmes_final_semana = {
    "o menino e a garça",
    "as branquelas",
    "premonição",
    "avengers",
    "diarios de uma paixão"
    }

print(filmes_final_semana)

#for i in filmes_final_semana
# print(i)

#dicionários:

filmes = {
    "titanic":[1977,"drama/roomance"],
"como se treinar o dragão":2010,
"shrek": 2001,
"star wars IV": 1984
}

#print(filmes["titanic","shrek"]
ano_lancamento_filmes = [1997,2007]
genero_filmes=["drama/romance","comédia/animação"]
indicacoes_oscar=["sim","sim"]

titanic_info = ["titanic",1997,"drama/romance","sim"]




