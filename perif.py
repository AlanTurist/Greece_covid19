import datetime
data = datetime.datetime.now()
data1 = data.strftime("%d-%m-%Y %H:%M:%S")

import pandas as pd
url = 'https://raw.githubusercontent.com/AlanTurist/Greece_covid19/master/region_greece.csv'
df = pd.read_csv(url,index_col=0, sep=",")

def regione(reg, x, y):
    reg1 = df.iloc[x]
    D1 = reg1['CASES']
    
    print('\n\t~ Ανάλυση δεδομένων του SARS-CoV2 - ',reg,'~')
    print('\n\t@Author: Γεώργιος Κολιού, georgios.koliou@gmail.com\n')
    print("*"*50,reg,"*"*50)
    print("\n\n\tΣήμερα έχουμε",data1)
    print('\n')
    print("*"*50,reg,"*"*50)
    print("\n\n\t1. Το σύνολο κρουσμάτων είναι:",D1)
    a = (100*D1)/y
    print('\n\t\t1.1. Μολύνθηκε το','{0:.3f}'.format(a),'% της περιφέρειας.')
    
    b = ((10000*a)/100)
    print("\n\t2. Τα κρούσματα ανά 10 χιλιάδες πληθυσμού είναι:",'{0:.3f}'.format(b))
    print('\n')
    print('*'*110)