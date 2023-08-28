
def validar_email(email):
    return "@" in email and "." in email

def validar_senha(senha):
    return len(senha) >= 6

def validar_cpf(cpf):
    return len(cpf) == 11 and cpf.isdigit()
