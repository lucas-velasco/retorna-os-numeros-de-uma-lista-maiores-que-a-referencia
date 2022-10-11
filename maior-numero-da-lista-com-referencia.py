'''Faça uma função chamada maiores que dada uma lista de números inteiros e um número inteiro n, retorna outra lista,
que contenha todos os números da lista original maiores que n, ordenados em ordem crescente.'''


def maiores(n_inteiro,n):
''' A função retorna outra lista, que contenha todos os números da lista original maiores que n, ordenados em ordem crescente.'''
def maiores(n_inteiro,n):
    if n not in n_inteiro:
        n_inteiro.append(n)
    n_inteiro.sort()
    indice= list.index(n_inteiro, n)
    return n_inteiro[indice+1:]
        
