with open('hello-world.docx', 'w+') as file:
    file.write('Olá, mundo!')
    file.seek(0)
    content = file.read()  
    print(content)  


    