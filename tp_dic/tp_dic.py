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

print("test print direct addition fruits avec patates")
mesLegumes = OrganizedDico(patates=70)
print (mesLegumes+mesFruits)
print ("mes legumes pour check, que patates")
print (mesLegumes)

#print ("print dico result test")
#dicoResult= mesLegumes + mesFruits
#print (dicoResult)

#print ("mon panier")
#print(monPanier)

monPanier = OrganizedDico(cerises=77)
print("test addition legumes avec += cerises")
mesLegumes += monPanier
print (mesLegumes)
print("test addition legumes avec += fruits")
mesLegumes += mesFruits
print (mesLegumes)
