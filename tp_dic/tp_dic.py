from dic import *

mesFruits = OrganizedDico(raisin=50,poires=10,orange=20, pommes=30)
print (mesFruits)

mesFruits.reverse()
print (mesFruits)

mesFruits.sort()
print (mesFruits)

print(mesFruits.len())

a = mesFruits['raisin']
print (a)

a = mesFruits['fraises']
print (a)

del mesFruits['fraises']

mesFruits['fraises']=31
print (mesFruits)

mesFruits['fraises']=41
print (mesFruits)

mesFruits.reverse()
print (mesFruits)

del mesFruits['fraises']
print (mesFruits)

a = 'raisin' in mesFruits
print (a)

a = 'patates' in mesFruits
print (a)

mesLegumes = OrganizedDico(patates=70)

print(mesFruits + mesLegumes)

#mesFruits = mesFruits + mesLegumes
#print (mesFruits)