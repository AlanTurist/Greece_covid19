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
D6 = reg1['TEST']
D7 = reg1['NEW_CASES']
D8 = reg1['NEW_DEATHS']

print('\t~ Ανάλυση δεδομένων για τον SARS-CoV2 στην Ελλάδα~')
print('\n\t@Author: Γεώργιος Κολιού, georgios.koliou@gmail.com')
print('\n****************************************************************************************')
print("\n\tΣήμερα έχουμε",data1)
print('\n****************************************************************************************')

print("\n\t1. Ο συνολικός αριθμός κρουσμάτων είναι:",D1)
a = (100*D1)/10742599
print('\n\t\t1.1. Μολύνθηκε το','{0:.3f}'.format(a),'% της χώρας.')
     
print("\n\t2. Ο αριθμός των νέων κρουσμάτων είναι:",D7)
b = (D1 - D7)
c = (100*D7)/b
print('\n\t\t2.1 Σε σχέση με χθες, ο αριθμός των κρουσμάτων αυξήθηκε κατά','{0:.2f}'.format(c),'%')
    
print('\n\t3. Ο συνολικός αριθμός θανάτων είναι:',D4)
d = (D4 - D8)
e = (100*D8)/d
print('\n\t\t3.1 Σε σχέση με χθες, ο αριθμός των θανάτων αυξήθηκε κατά','{0:.2f}'.format(e),'%')
f = (100*D4)/D1
print("\n\t\t3.2 Η θνητότητα είναι:",'{0:.2f}'.format(f),'%')
    
print('\n\t4. Ο αριθμός όσων ανάρρωσαν είναι:',D3)
g = (100*D3)/D1
print('\n\t\t4.1 Ανάρρωσε το','{0:.2f}'.format(g),'%')
    
print('\n\t5. Ο αριθμός των σοβαρών περιστατικών είναι:',D5)
h = (100*D5)/D1
print('\n\t\t5.1 Σοβαρά είναι το','{0:.2f}'.format(h),'%')
    
print('\n\t6. Ο αριθμός των ενεργών κρουσμάτων είναι:',D2)
k = (100*D2)/D1
print('\n\t\t6.1 Τα ενεργά κρούσματα είναι','{0:.1f}'.format(k),'%')
    
i = ((10000*a)/100)
print("\n\t7. Τα κρούσματα ανά 10 χιλιάδες πληθυσμού είναι:",'{0:.1f}'.format(i))
    
j = ((1000000*a)/100)
print("\n\t8. Τα κρούσματα ανά 1 εκατομμύριο πληθυσμού είναι:",'{0:.1f}'.format(j))
          
l = (100*D5)/247
print("\n\t6. Είναι κατηλλημένο το",'{0:.2f}'.format(l),"% των ΜΕΘ")

import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(24, 12), subplot_kw=dict(aspect="equal"))

recipe = ["ΕΝΕΡΓΟΙ", "ΑΝΝΑΡΩΣΑΝ", "ΘΑΝΑΤΟΙ", "ΚΡΙΣΙΜΑ"]

data = [D2, D3, D4, D5]

wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, **kw)

ax.set_title("SARS-CoV2 ΕΛΛΑΔΑ")

plt.show()