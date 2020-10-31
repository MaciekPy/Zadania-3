# Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim
# (z literami I, V, X, L, C, D, M) na liczby arabskie
# (podać kilka sposobów tworzenia takiego słownika).
# Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].

S = {"I": 1 , "V": 5, "X": 10, "L" : 50, "C": 100, "D": 500, "M": 1000}

R = "MXMIX"

print("Rzymska liczba : " + R)

length = len(R)

arab = 0

for i in range(length):
	if i == length-1:
		arab = arab + S[R[i]]
		break
		
	if S[R[i]] > S[R[i+1]]:
		arab = arab + S[R[i]]
	else:
		arab = arab - S[R[i]]
		
print("Arabska liczba : " + str(arab))