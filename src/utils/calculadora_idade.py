from datetime import datetime, date

class CalculadoraIdade:
    def __init__(self):
        pass

    @staticmethod
    def calcular_idade(data_nascimento): 
        nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
        data_hoje =  date.today() 

        if nascimento > data_hoje:
            raise ValueError("Data de nascimento não pode ser no futuro")

        idade = data_hoje.year - nascimento.year
        if (data_hoje.month, data_hoje.day) < (nascimento.month, nascimento.day):
            idade -= 1
        return idade
