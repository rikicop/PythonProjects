# -*- coding: utf-8 -*-
import  re 
#import urllib.request as urllib
#opener = urllib.FancyURLopener({})
url = "https://mobile.twitter.com/dolartoday"
#f = opener.open(url)
#content = f.read()
#print(content)
#x  =  ' ysyw "From" Using  the  : character' 
x='<span class="css-901oao css-16my406 r-1qd0xha  /img d9z0x r-bcqeeo r-qvutc0">Noticias de Venezuela Viernes Ago 2, 2019 el $ cotiza a Bs. 13016,84 y el € a Bs. 14354,84 entra sin bloqueos -► </span>'
#el resultado es una lista
y  =  re.findall('cotiza a Bs.(.+?),',  x)
#convierte la lista en toda una cadena 
#de caracteres
str1 = ''.join(str(e) for e in y)
t=float(str1)+7

print(str1)
#print  (t)

#diferente patron
#quieres remplazar img/ por
# {%   %}

z = re.findall('class(.+?)"' , x)
str2 = ''.join(str(e) for e in z)

print(str2 )