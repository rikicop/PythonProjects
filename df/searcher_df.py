
import pandas as pd

a=input("Ingresa Tipo: ")
b=input("Ingresa Ubicación: ")
c=input("Ingresa nuevo/usado(n/u): ")

raw_data = {'cod': ['123', '321', '234', '432', '765','555'],
                'tipo': ['casa', 'casa', 'casa', 'galpon', 'galpon','galpon'],
                'ubi': ['barrio', 'centro', 'centro', 'centro', 'barrio','barrio'],
                'edo': ['n', 'u', 'u', 'u', 'n','u'],
                'precio': [1000, 1500, 1200, 3000, 2300,1200]}

df = pd.DataFrame(raw_data, columns = ['cod', 'tipo', 'ubi', 'edo','precio'])
print(df,"\n")
#print(df['Comedy_Score'].where(df['Rating_Score'] < 50))

#En el if estan todas las posibilidades
""" if (a != '') and (b != ''):
	#EL QUE Es Diferente ahora va a ser igual
    newdf = df.loc[((df.tipo == a) & (df.ubi == b))]
    print(newdf)

elif (a != '') and (b == ''):
	#EL QUE Es igual ahora desaparece
    newdf = df.loc[df.tipo == a]
    print(newdf)

elif (a == '') and (b != ''):
    newdf = df.loc[df.ubi == b]
    print(newdf) """


if (a != '') and (b != '') and (c != ''): 
    newdf = df.loc[((df.tipo == a) & (df.ubi == b) & (df.edo == c))]
    print(newdf)

elif (a != '') and (b != '') and (c == ''): 
    newdf = df.loc[((df.tipo == a) & (df.ubi == b))]
    print(newdf)

elif (a != '') and (b == '') and (c == ''): 
    newdf = df.loc[df.tipo == a]
    print(newdf)

elif (a == '') and (b != '') and (c == ''): 
    newdf = df.loc[df.ubi == b]
    print(newdf)

elif (a == '') and (b != '') and (c != ''):
    newdf = df.loc[((df.ubi == b) & (df.edo == c))]
    print(newdf)

elif (a != '') and (b == '') and (c != ''): 
    newdf = df.loc[((df.tipo == a) & (df.edo == c))]
    print(newdf)

elif (a == '') and (b == '') and (c != ''): 
    newdf = df.loc[df.edo == c]
    print(newdf)




#Vas a necesitar esto en Django
#df= pd.DataFrame(list(Post.objects.all().values()))