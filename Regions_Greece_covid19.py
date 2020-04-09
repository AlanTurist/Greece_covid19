#!/usr/bin/env python
# coding: utf-8

import datetime
data = datetime.datetime.now()
data1 = data.strftime("%d-%m-%Y %H:%M:%S")
import pandas as pd
url = 'https://raw.githubusercontent.com/AlanTurist/Greece_covid19/master/region_greece.csv'
df = pd.read_csv(url,index_col=0, sep=",")

reg = str(input("\nΕισάγετε περιφέρεια: "))

def regione(reg, x, y):
    reg1 = df.iloc[x]
    D1 = reg1['CASES']
    
    print('\n\t~ Ανάλυση δεδομένων του SARS-CoV2 - ',reg,'~')
    print('\n\t@Author: Γεώργιος Κολιού, georgios.koliou@gmail.com')
    print('\n****************************************************************************************')
    print("\n\tΣήμερα έχουμε",data1)
    print('\n****************************************************************************************')
    
    print("\n\t1. Το σύνολο κρουσμάτων",reg,"είναι:",D1)
    a = (100*D1)/y
    print('\n\t\t1.1. Μολύνθηκε το','{0:.3f}'.format(a),'% της περιφέρειας.')
    
    b = ((10000*a)/100)
    print("\n\t2. Τα κρούσματα ανά 10 χιλιάδες πληθυσμού είναι:",'{0:.3f}'.format(b))
    
    print('\n****************************************************************************************\n\n')

if reg == "ΑΤΤΙΚΗ":
    regione(reg,0,3742000)
    
elif reg == "ΔΥΤΙΚΗ ΕΛΛΑΔΑ":
    regione(reg,1,655189)

elif reg == "ΚΕΝΤΡΙΚΗ ΕΛΛΑΔΑ":
    regione(reg,2,547390)
    
elif reg == "ΔΥΤΙΚΗ ΜΑΚΕΔΟΝΙΑ":
    regione(reg,3,283689)
    
elif reg == 'ΚΕΝΤΡΙΚΗ ΜΑΚΕΔΟΝΙΑ':
    regione(reg,4,1882000)

elif reg == 'ΒΟΡΕΙΟ ΑΙΓΑΙΟ':
    regione(reg,5,221098)

elif reg == "ΑΝΑΤΟΛΙΚΗ ΜΑΚΕΔΟΝΙΑ/ΘΡΑΚΗ":
    regione(reg,6,608182)

elif reg == "ΘΕΣΣΑΛΙΑ":
    regione(reg,7,732762)

elif reg == "ΠΕΛΟΠΟΝΝΗΣΟΣ":
    regione(reg,8,1155000)

elif reg == "ΕΠΤΑΝΗΣΑ":
    regione(reg,9,207855)

elif reg == "ΚΡΗΤΗ":
    regione(reg,10,623025)

elif reg == "ΗΠΕΙΡΟΣ":
    regione(reg,11,336856)

elif reg == "ΝΟΤΙΟ ΑΙΓΑΙΟ":
    regione(reg,12,309015)

elif reg == "ΑΓΝΩΣΤΗ ΤΟΠΟΘΕΣΙΑ":
    regione(reg,13,1)
    
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