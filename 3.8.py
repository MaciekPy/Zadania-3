# Dla dwóch sekwencji znaleźć: (a) listę elementów występujących 
# jednocześnie w obu sekwencjach (bez powtórzeń), 
# (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).

L = {1,3,6,9,12}
K = {2,3,5,8,12}

print("Sekwencje : \n" + str(L) + "\n" + str(K))

inter = L.intersection(K)
union = L.union(K)

print("Elementy występujące w obydwoch sekwencjach : " + str(inter))
print("Wszystkie elementy z obydwoch sekwencji : " + str(union))