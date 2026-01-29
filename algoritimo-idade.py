'''

dona maria precisa de um algoritimo que faça as seguintes decisões

1: se um criança com idade < que 12 deve mostra a mensagem criança
2: se a idade for < que 18 mostrar a mensagem adolecente
3: se a idade for < que 60 mostrar a mensagem aduto
4: se não for não se encaixar nas decima mostra a mensagem idoso
'''

# entrada de informação

idade = 1000

if idade < 12:
    print("criança")
elif idade < 18:
    print("adolecente")
elif idade < 60:
    print("adulto")
else:
    print("idoso")