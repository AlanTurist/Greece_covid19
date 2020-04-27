#!/usr/bin/env python
# coding: utf-8
import perif

reg = str(input("\nΕισάγετε περιφέρεια: "))

if reg == "ΑΤΤΙΚΗ":
    perif.regione(reg,0,3742000)
    
elif reg == "ΔΥΤΙΚΗ ΕΛΛΑΔΑ":
    perif.regione(reg,1,655189)

elif reg == "ΚΕΝΤΡΙΚΗ ΕΛΛΑΔΑ":
    perif.regione(reg,2,547390)
    
elif reg == "ΔΥΤΙΚΗ ΜΑΚΕΔΟΝΙΑ":
    perif.regione(reg,3,283689)
    
elif reg == 'ΚΕΝΤΡΙΚΗ ΜΑΚΕΔΟΝΙΑ':
    perif.regione(reg,4,1882000)

elif reg == 'ΒΟΡΕΙΟ ΑΙΓΑΙΟ':
    perif.regione(reg,5,221098)

elif reg == "ΑΝΑΤΟΛΙΚΗ ΜΑΚΕΔΟΝΙΑ/ΘΡΑΚΗ":
    perif.regione(reg,6,608182)

elif reg == "ΘΕΣΣΑΛΙΑ":
    perif.regione(reg,7,732762)

elif reg == "ΠΕΛΟΠΟΝΝΗΣΟΣ":
    perif.regione(reg,8,1155000)

elif reg == "ΕΠΤΑΝΗΣΑ":
    perif.regione(reg,9,207855)

elif reg == "ΚΡΗΤΗ":
    perif.regione(reg,10,623025)

elif reg == "ΗΠΕΙΡΟΣ":
    perif.regione(reg,11,336856)

elif reg == "ΝΟΤΙΟ ΑΙΓΑΙΟ":
    perif.regione(reg,12,309015)

elif reg == "ΑΓΝΩΣΤΗ ΤΟΠΟΘΕΣΙΑ":
    perif.regione(reg,13,1)

elif reg == "ΑΓΙΟ ΟΡΟΣ":
    perif.regione(reg,14,2416)
    
else:
    print('Η περιφέρεια που εισάγατε δεν υπάρχει..')

import os
import sys

restart = input("\n\nΑν Θέλετε να ξαναδοκιμάσετε πατήστε το 'Ν' και enter: ")

if restart == "Ν":
    os.execl(sys.executable, sys.executable, * sys.argv) 
else:
    print("\nΤο πρόγραμμα κλείνει..")
    sys.exit(0)