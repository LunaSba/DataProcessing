import re,sys

# 1ere etape extraire les substance active de corpus_medc
fichier = open("medical.txt",'w')
var=open(sys.argv[1],'r',encoding="utf-8\ufeff").readlines()  # pour lire corpus-medical
for i in var: 
 x=re.search("^-? ?(\w+) :? ?(\d+|,)+ (mg|ml)", i,re.I) 
 fichier.write(x.group(1).lower()+"\n") if x else ' '  # on met le resultat de l'extraction dans un fichier nommé medical
fichier.close()

# recuper l'intervel
info = open("subst.dic",'r',encoding="UTF-16-le")
info = info.readlines()
car1 = info[1]
car1 = car1[0:1]
car2 = info[-1]
car2 = car2[0:1]


# extraction des substances et les mettre dans un fichier subst_enri.dic
caractere = input("\n\t* Si vous voulez enrichir votre dictionnaire tapez ' oui ' sinon n'import quel caractère : ")
if(caractere == "oui") :
  # garder la trace 
  fichier = open("medical.txt",'r') # prendre les resultats de fichier medical et on rajoute ,.N+subst dans le dictionnaire subst_enri.dic
  x = fichier.readlines()
  # print(x)
  liste = []
  for i in x:
   if((i[0:1] < 'a') or (i[0:1] > 'z')):
      i=i[1:] # pour les medicaments qui ont un carctère bizarre au debut
      # print(i)
   if(((i[0:1] >= car1)&(i[0:1] <= car2))or((i[0:1] >= car1.upper())&(i[0:1] <= car2.upper()))):
    if((i!="puis\n")and(i != "crp\n")):  # pour eliminer puis et crp )
     i = (i.rstrip())
     i = i+",.N+subst\n"
     liste.append(i)
  # on utilise un dictionnaire 
  substance_corpus ={} 
  for l in liste: 
   if l in substance_corpus: 
    substance_corpus[l] = substance_corpus[l] + 1  
   else: 
    substance_corpus[l] = 1 
  # substance_corpus contient les nouveaux med 
  # affichage des medicaments + le tri et l insertion en subst_enri.dic
  print("\n\t* L'affichage des médicaments rajoutes :")
  print("\t---------------------------------------\n")
  compteur = 0
  dic = open("subst_enri.dic",'w',encoding="UTF-16-le")
  dic.write("\ufeff")
  for i in sorted(substance_corpus):
   dic.write(i)
   compteur+=1
   print(str(compteur)+" -> le medicament : "+i[0:-10]+".")
  # print(dic)
  dic.close()
  
  f = open("subst.dic",'r',encoding="UTF-16-le")
  su = f.readlines()
  substance = {}
  for l in su: 
   if l in substance: 
    substance[l] = substance[l] + 1  
   else: 
    substance[l] = 1
	
  # print(substance)
  # print(substance_corpus)
  for i in sorted(substance_corpus):
   if i in sorted(substance):
     substance[i] = substance[i]+1
   else:
     substance[i] = 1   
  # print(sorted(substance))
  
  s = open("subst.dic",'w',encoding="UTF-16-le")
  s.write("\ufeff")  
  for i in sorted(substance):
   s.write(i)
  s.close()
else :
  exit()