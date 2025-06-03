from datetime import datetime

def data(data_nascimento): 
    nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
    data_hoje =  datetime.today().date() 
    idade = data_hoje.year - nascimento.year
    if (data_hoje.month, data_hoje.day) < (nascimento.month, nascimento.day):
        idade -= 1
    return idade
