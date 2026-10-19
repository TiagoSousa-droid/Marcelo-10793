import random 

tarefas = ["T1", "T2", "T3"]
# Inserir uma tarefa
tarefas.append("T4")
print("Lista depois do append: ", tarefas)
# Inserir vários
tarefas.extend(["T5", "T6"])
print("Lista depois do extend: ", tarefas)
#Inserir um em uma posição específica
tarefas.insert(2,"T7")
print("Lista depois do insert: ", tarefas)
# Remover o último 
tarefas.pop()
print("Lista depois do pop: ", tarefas)
# Remover um em uma posição específica
tarefas.pop(4)
print("Lista depois do pop(4): ", tarefas)
#ELIMINAR TODAS
tarefas.clear()
print("Lista depois do clear: ", tarefas)
#jogadores.count("J5")
tarefas.count("T5")
print("Nº de ocorrências do T5: ", tarefas.count("T5"))
# Devolver o índice de um element
tarefas.index("T3")
print("Índice do T3: ", tarefas.index("T3"))

# Inverter a lista
tarefas.reverse()
print("Lista depois do reverse: ", tarefas)
# Copiar uma lista
tarefas = [1,2,3]
tarefas2 = tarefas # As listas ficam ligadas
print("Lista 1: ", tarefas, "Lista 2: ", tarefas2)
