# Mamy daną listę sekwencji (listy lub krotki)
# różnej długości zawierających liczby.
# Znaleźć listę zawierającą sumy liczb z tych sekwencji.
# Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)],
# spodziewany wynik [0,4,3,7,18].

L = [[],[4],(1,2),[3,4],(5,6,7)]
length = len(L)
K = []

print("Początkowa lista sekwencji : " + str(Ls))

for i in range(length):
	len2 = len(L[i])
	sum = 0 
	for j in range(len2):
		sum = sum + L[i][j]
	K.append(sum)

print("Wynik : " + str(K))