N=4


def perm_caoticas_backtrack(perm_corrente, lista):
    if len(perm_corrente) == N:
        lista += [perm_corrente]
    else:
        for x in range(1, N+1):
            if x != len(perm_corrente) + 1 and x not in perm_corrente:
                nova_perm = perm_corrente + [x]
                perm_caoticas_backtrack(nova_perm, lista)
   

lista = []
perm_caoticas_backtrack([], lista)
print("\n".join([str(perm) for perm in lista]))

print("Total =", len(lista))
