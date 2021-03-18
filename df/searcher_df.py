
import pandas as pd

tipo_form = input("Ingresa Tipo: ")
ubicacion_form =input("Ingresa Ubicación: ")
edo_form =input("Ingresa nuevo/usado(n/u): ")

raw_data = {'cod': ['123', '321', '234', '432', '765','555'],
                'tipo': ['casa', 'casa', 'casa', 'galpon', 'galpon','galpon'],
                'ubi': ['barrio', 'centro', 'centro', 'centro', 'barrio','barrio'],
                'edo': ['n', 'u', 'u', 'u', 'n','u'],
                'precio': [1000, 1500, 1200, 3000, 2300,1200]}

df = pd.DataFrame(raw_data, columns = ['cod', 'tipo', 'ubi', 'edo','precio'])
print(df,"\n")



if (tipo_form != '') and (ubicacion_form != '') and (edo_form != ''): 
    newdf = df.loc[((df.tipo == tipo_form) & (df.ubi == ubicacion_form) & (df.edo == edo_form))]
    print(newdf)

elif (tipo_form != '') and (ubicacion_form != '') and (edo_form == ''): 
    newdf = df.loc[((df.tipo == tipo_form) & (df.ubi == ubicacion_form))]
    print(newdf)

elif (tipo_form != '') and (ubicacion_form == '') and (edo_form == ''): 
    newdf = df.loc[df.tipo == tipo_form]
    print(newdf)

elif (tipo_form == '') and (ubicacion_form != '') and (edo_form == ''): 
    newdf = df.loc[df.ubi == ubicacion_form]
    print(newdf)

elif (tipo_form == '') and (ubicacion_form != '') and (edo_form != ''):
    newdf = df.loc[((df.ubi == ubicacion_form) & (df.edo == edo_form))]
    print(newdf)

elif (tipo_form != '') and (ubicacion_form == '') and (edo_form != ''): 
    newdf = df.loc[((df.tipo == tipo_form) & (df.edo == edo_form))]
    print(newdf)

elif (tipo_form == '') and (ubicacion_form == '') and (edo_form != ''): 
    newdf = df.loc[df.edo == edo_form]
    print(newdf)




#Vas a necesitar esto en Django
#df= pd.DataFrame(list(Post.objects.all().values()))
