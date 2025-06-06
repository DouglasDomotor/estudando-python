from datetime import datetime, date

def calcular_idade(data_nascimento): 
    nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
    data_hoje =  date.today() 
    idade = data_hoje.year - nascimento.year
    if (data_hoje.month, data_hoje.day) < (nascimento.month, nascimento.day):
        idade -= 1
    return idade
#$env:PYTHONPATH="src"; pytest
