def main():
    # Inicializa o total da compra
    total_compra = 0.0
    
    while True:
        # Solicita a quantidade do produto ao usuário
        quantidade = input("Digite a quantidade do produto (ou 'fim' para encerrar): ")
        
        # Verifica se o usuário deseja encerrar
        if quantidade.lower() == "fim":
            break  # Sai do loop se o usuário digitar 'fim'

        # Solicita o valor unitário do produto
        valor_unitario = input("Digite o valor unitário do produto: ")
        
        # Converte a quantidade e o valor unitário para float
        quantidade = float(quantidade)
        valor_unitario = float(valor_unitario)       
        
        # Calcula o custo total do produto
        custo_total = quantidade * valor_unitario   
        
        # Acumula o custo total na compra
        total_compra += custo_total

    # Exibe o valor total da compra ao final
    print(f"O valor total da compra é: R${total_compra:.2f}")

# Chama a função principal para executar o programa
main()

