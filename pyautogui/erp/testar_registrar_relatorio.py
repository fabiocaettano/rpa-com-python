historico_execucao = []

def registrar_relatorio(nome, job, ref_erp):
    from datetime import datetime
    
    dados = {
        "nome": nome,
        "job": job,
        "referencia": ref_erp,
        "timestamp": datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    }
    historico_execucao.append(dados)

registrar_relatorio('Relatório A', 'R5542E002_EST72M0001', 'R5542E002_EST72M0001')
registrar_relatorio('Relatório B', 'R5542E002_EST72M0002', 'R5542E002_EST72M0002')

for relatorio in historico_execucao:
    print(f"Relatório: {relatorio['nome']}, Job: {relatorio['job']}, Referência: {relatorio['referencia']}, Timestamp: {relatorio['timestamp']}")

