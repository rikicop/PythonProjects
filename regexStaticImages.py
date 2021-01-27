import re

#tienes src="images/hola.jpg"
#quieres src="{% static 'website/images/hola.jpg' %}"

#Agregar esto al principio {% static 'website/images
# y esto al fina %} 

x='<span class="css-901oao css-16my406 r-1qd0xha  src="images/hola.jpg" d9z0x r-bcqeeo r-qvutc0">Noticiaes Ago 2, 2019 el $ cotiza a Bs. 13016,84 y el € a Bs. 14354,84 entra sin bloqueos -► src="images/hola.jpg"  </span>'

#Remplazar Principio
tagstart = re.sub(r"images/", "{% static 'website/images/", x)
print(tagstart)
#Out: <span class="css-901oao css-16my406 r-1qd0xha
#src=" {% static 'website/images/hola.jpg"
#d9z0x r-bcqeeo r-qvutc0">Noticiaes 
#Ago 2, 2019 el $ cotiza a Bs. 13016,84 y el € a Bs. 14354,84 entra
#sin bloqueos -► src=" {% static 'website/images/hola.jpg"  </span>

#Reemplazar Final .jpg"
tagend = re.sub(r".jpg", ".jpg' %}", tagstart)
print(tagend)

#<span class="css-901oao css-16my406 r-1qd0xha  
#src="{% static 'website/images/hola.jpg' %}" d9z0x
#r-bcqeeo r-qvutc0">Noticiaes Ago 2, 2019 el $ cotiza a Bs. 13016,84 y
#el € a Bs. 14354,84 entra sin bloqueos -►
#src="{% static 'website/images/hola.jpg' %}"  </span>



#tienes src="images/hola.jpg"
#quieres src="{% static 'website/images/hola.jpg' %}"
