#!/usr/bin/env python
# coding: utf-8

import datetime
data = datetime.datetime.now()
data1 = data.strftime("%d-%m-%Y %H:%M:%S")
import pandas as pd
url = 'https://raw.githubusercontent.com/AlanTurist/Greece_covid19/master/total_greece.csv'
df = pd.read_csv(url,index_col=0, sep=",")

reg1 = df.iloc[0]
D1 = reg1['TOTAL_CASES']
D2 = reg1['ACTIVE_CASES']
D3 = reg1['RECOVERED']
D4 = reg1['DEATHS']
D5 = reg1['CRITICAL']

print('\t~ Ανάλυση δεδομένωνγια τον SARS-CoV2 στην Ελλάδα~')
print('\n\t@Author: Γεώργιος Κολιού, georgios.koliou@gmail.com')
print('\n****************************************************************************************')
print("\n\tΣήμερα έχουμε",data1)
print('\n****************************************************************************************')

print("\n\t1. Το σύνολο κρουσμάτων είναι:",D1)
a = (100*D1)/10742599
print("\n\t\t1.1 Έχει μολυνθεί το",'{0:.3f}'.format(a),"% της χώρας. ")

print("\n\t2. Τα ενεργά κρούσαματα είναι:",D2)
b = (100*D2)/D1
print('\n\t\t2.1. Τα ενεργά κρούσματα είναι το','{0:.2f}'.format(b),'% του συνόλου.')

c = (100*D4)/D1
print("\n\t3. Έχουν αναρρώσει:",D4)
print("\n\t\t3.1. Έχει αναρρώσει το",'{0:.2f}'.format(c),"% του συνόλου.")

d = (100*D4)/D1
print("\n\t4. Ο αριθμός θανάτων είναι:",D4)
print("\n\t\t4.1 Η θνησιμότητα είναι στο",'{0:.2f}'.format(d),"% του συνόλου.")

e = (100*D5)/D1
print("\n\t5. Σε κρίσιμη κατάσταση είναι:",D5)
print("\n\t\t5.1 Σε κρίσιμη κατάσταση είναι το",'{0:.2f}'.format(e),"% του συνόλου.")
      
f = (100*D5)/247
print("\n\t6. Είναι κατηλλημένο το",'{0:.2f}'.format(f),"% των ΜΕΘ")

input("\n\nΠατήστε enter για έξοδο από το πρόγραμμα..")