import random 

nums = [1,2,3,4,5,6,7,8,9,10]
pares= [nums for nums in nums if nums % 2 == 0]
quadrados = [nums*nums for nums in nums]
palavras = ["pão","leite","queijo","manteiga"]
maiorquecinco = [nums >5 for nums in nums]
maisculas = [palavra.upper() for palavra in palavras]
print (pares, quadrados, palavras, maiorquecinco)