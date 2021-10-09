import os

os.system("rd /s corpus-medical_snt")
os.mkdir("corpus-medical_snt")

os.system("C:/Unitex-GramLab/App/exToolLogger Normalize corpus-medical.txt -r C:/Users/Public/Documents/Unitex-GramLab/Unitex/French/Norm.txt")
os.system("C:/Unitex-GramLab/App/UnitexToolLogger Tokenize corpus-medical.snt -a C:/Users/Public/Documents/Unitex-GramLab/Unitex/French/Alphabet.txt")
os.system("C:/Unitex-GramLab/App/UnitexToolLogger Compress subst.dic")
os.system("C:/Unitex-GramLab/App/UnitexToolLogger Dico -t corpus-medical.snt -a C:/Users/Public/Documents/Unitex-GramLab/Unitex/French/Alphabet.txt subst.bin C:/Users/Public/Documents/Unitex-GramLab/Unitex/French/Dela/delaf.bin")
os.system("C:/Unitex-GramLab/App/UnitexToolLogger Grf2Fst2 posologie.grf")
os.system("C:/Unitex-GramLab/App/UnitexToolLogger Locate -t corpus-medical.snt posologie.fst2 -a C:/Users/Public/Documents/Unitex-GramLab/Unitex/French/Alphabet.txt -L -I --all")
os.system("C:/Unitex-GramLab/App/UnitexToolLogger concord corpus-medical_snt/concord.ind -f \"Courrier New\" -s 12 -l 40 -r 55")
