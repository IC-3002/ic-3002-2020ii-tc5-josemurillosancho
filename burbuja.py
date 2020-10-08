def burbuja(A):
    n = len(A)
    for i in range(1, n):
        for j in range(0, n - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)

def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def burbuja_optimizado(A):
    """Funcion para ordernar elementos de una lista
	E: Una lista
	S: Una lista o un error
	R: Ocupa ser una lista"""
	if type(A)!= list:
		return "Error01"
	else:
		i = 0
		n = len(A)
		ordenado = False
		while i < (n-1) and ordenado != True:
			i += 1
			ordenado = True
			for j in range(0, n-i):
				if A[j] > A[j+1]:
					swap(A, j, j+1)
					ordenado = False
	return A
