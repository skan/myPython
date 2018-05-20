from dic import *

mesFruits = OrganizedDico(raisin=50,poires=10,orange=20, pommes=30)
print (mesFruits)

print ("test reverse ")
mesFruits.reverse()
print (mesFruits)

print ("test sort ")
mesFruits.sort()
print (mesFruits)

print ("test len ")
print(mesFruits.len())

print ("test set item ")
a = mesFruits['raisin']
print (a)

a = mesFruits['fraises']
print (a)

print ("test del fraises")
del mesFruits['fraises']

print ("test fraises = 31")
mesFruits['fraises']=31
print (mesFruits)

print ("test fraises = 31")
mesFruits['fraises']=41
print (mesFruits)

print ("test reverse")
mesFruits.reverse()
print (mesFruits)

print ("test del")
del mesFruits['fraises']
print (mesFruits)

print("test in")
a = 'raisin' in mesFruits
print (a)

a = 'patates' in mesFruits
print (a)
print("test addition")
#mesLegumes = OrganizedDico(patates=70)
#print (mesLegumes)

print ("mon panier")
monPanier = OrganizedDico(cerises=77)
print(monPanier)

#mesFruits = mesFruits + mesLegumes
#print (mesFruits)