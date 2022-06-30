A = (0, 0)
B = (2, 0)
C = (2.6, 1.9)
D = (1, 3.1)
E = (-0.6, 1.9)
lista_t = [A, B, C, D, E]
lista_l = []
for t in lista_t:
  lista_l.append(t[1])
lista_l.sort()
print(lista_l)