import urllib.request
import re 
import sys 

information = open("infos.txt",'w')
l = sys.argv[1]
lettre1 = l[0]
car = l[1]
lettre2 = l[2]

if((lettre1 > lettre2)or(car != '-') or (lettre1 < 'A') or (lettre2 > 'Z')):
   print("ERREUR ! , ce cas n'est pas consideré")
   information.write("Fichier Vide !")
   information.close()
   exit()
else:
   fich = open("ess.txt",'w')
   dic = open("subst.dic",'w',encoding='UTF-16')
   dic.write("\ufeff")
   liste = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
   information.write("\n\n--------------------------------------------------------------------------------------------------------------------\n\n")
   information.write("Le nombre d'entités médicales par substence active :\n\n\n")
   for i in liste:  #extraire les codes html et les mettre dans un fichier intermidiare ess.txt
    if(((i >= lettre1)&(i <= lettre2))or((i >= lettre1.upper())&(i <= lettre2.upper()))):
     f = urllib.request.urlopen("https://www.vidal.fr/Sommaires/Substances-"+str(i)+".htm")
     var = f.read().decode('UTF-8')
     fich.write(var)
   fich.close()
   
   fich = open("ess.txt",'r')
   x = fich.readlines()
   fich = open("ess.txt",'w')
   for i in x: #utiliser le fichier ess.txt pour extraire les substences
    p = re.findall("Substance/(.+)-[0-9]",i) # p est une liste qui contient les substences actives
    for v in p:  # v est une chaine des substence
     # print(v)
     if((v[0:1] < 'a') or (v[0:1] > 'z')):
       v=v[1:] # pour les medicaments qui ont un carctère bizarre au debut
       print(i)
     fich.write(v+"\n")
   fich.close()
   
   
   # on va utiliser le fichier ess pour compter le nombre des entités 
   # on utilise un dictionnaire 
   di = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
   fich = open("ess.txt",'r')
   var = fich.readlines()
   # print(var)

   for indice in di:
    for v in var:
      if(v[0:1] == indice):
       di[indice]=di[indice]+1
   
   # print(di)
   compteur=0
   for indice in sorted(di):
    information.write("\t*\tPour la lettre \" "+str(indice.upper())+" \" le nombre est\t\t:"+str(di.get(indice))+"\n")
    compteur = compteur + di.get(indice)
   information.write("\n\t*\tle nombre total d'entités médicales par substance active du dictionnaire est \" "+str(compteur)+" \"\n")
   information.write("\n\n--------------------------------------------------------------------------------------------------------------------\n\n")
   information.close()  
   
   fich = open("ess.txt",'r') # prendre les resultats de fichier ess et on rajoute ,.N+subst dans le dictionnaire subst.dic
   x = fich.readlines()
   dic.write("\n")
   for i in x:
    i = (i.rstrip())
    dic.write(i+",.N+subst\n")
   fich.close()
