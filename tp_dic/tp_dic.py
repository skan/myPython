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

mesFruits['fraises']=31
print (mesFruits)

mesFruits['fraises']=41
print (mesFruits)

mesFruits.reverse()
print (mesFruits)