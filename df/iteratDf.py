import pandas as pd

#df = pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 110, 120]})

data = {
        'Estado': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],  
        'AÃ±o': [2000, 2001, 2002, 2001, 2002, 2003],  
        'Pob': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
        }
 
df = pd.DataFrame(data,  columns=['Estado','AÃ±o','Pob'])
 
print('Cuadro Completo:\n' ,df)

print('\n')
print('Con PoblaciÃ³n Mayor a 2 millones:\n')
for index, row in df.iterrows():
    if row['Pob'] > 2:
    	print(row['Estado'], row['AÃ±o'])
