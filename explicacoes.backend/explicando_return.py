# RETURN EXEMPLO

def latir():
    print("au au")

def latir_retorno():
    return "au au", "meow"


discurso_cachorro = latir_retorno()[0]

print(discurso_cachorro)
