from datetime import datetime, timedelta

data = [
    "18/04/2026", 
    "19/04/2026", 
    "21/04/2026", 
    "25/04/2026",     
    "26/04/2026"]

def obter_dias_nao_trabalhados():    
    return data.copy()

def definir_periodo_pesquisa(numero_dias_uteis):    
    data_atual = datetime.now()
    data_atual_str = data_atual.strftime("%d/%m/%Y")
    data_inicial = datetime.now()
    contagem = 0
    while contagem < numero_dias_uteis:
        data_inicial -= timedelta(days=1)
        data_inicial_str = data_inicial.strftime("%d/%m/%Y")    
        if data_inicial_str not in obter_dias_nao_trabalhados():
           contagem += 1
    return data_inicial_str, data_atual_str