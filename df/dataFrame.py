
import pandas as pd

data = {
        'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']
        }

df = pd.DataFrame(data)

print(df[['Name', 'Address','Qualification']],"\n")

qty = len(df)

print(qty)


for i in range(qty):
    if df.Name == 'Jai':
            print(df.Name) 