def main():
    total_compra = 0.0
    valor_unitario = 0
    while True:
        quantidade = input("Digite a quantidade do produto (ou 'fim' para encerrar): ")
        
        if quantidade.lower() == "fim":
            break

        valor_unitario = input("Digite o valor unitário do produto: ")
        
        quantidade = float(quantidade)
        valor_unitario = float(valor_unitario)       
        custo_total = quantidade * valor_unitario   
        total_compra += custo_total
        
       
    
    print(f"O valor total da compra é: R${total_compra:.2f}")


main()
