import re
import time

#tienes src="images/hola.jpg"
#quieres src="{% static 'website/images/hola.jpg' %}"

#Agregar esto al principio {% static 'website/images
# y esto al fina %} 

with open('index.html', 'r') as file:
    x = file.read()

tagstartImg = re.sub(r"images/", "{% static 'website/images/", x)

#Reemplazar Final .jpg"
tagendImgJpg = re.sub(r"\.jpg", ".jpg' %}", tagstartImg)
#Reemplazar Final .png"
tagendImgPng = re.sub(r"\.png", ".png' %}", tagendImgJpg)
#Reemplazar Final .svg"
tagendImgSvg = re.sub(r"\.svg", ".svg' %}", tagendImgPng)

time.sleep(2)
#Css Principio
tagstartCss = re.sub(r"css/", "{% static 'website/css/", tagendImgSvg)
#Css Final
tagendCss = re.sub(r"\.css", ".css' %}", tagstartCss)

time.sleep(2)

#Js Princ
tagstartJs = re.sub(r"js/", "{% static 'website/js/", tagendCss)
#Css Final
tagendJs = re.sub(r"\.js", ".js' %}", tagstartJs)
print(tagendJs)

filename = 'new-index.html'

# Open the file in write mode and store the content in file_object
with open(filename, 'w') as file_object:
    file_object.write(tagendJs)
