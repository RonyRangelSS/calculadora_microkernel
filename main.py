from core.calculadora import Calculadora

# Inicialmente é uma calculadora de terminal com apenas soma e subtração. Por meio da utilização de plugins, novas funcionalidades são adicionadas dinamicamente.
# Cada plugin é um módulo Python que implementa uma operação específica (multiplicação, divisão, potência, etc.) e é carregado em tempo de execução.
def main():
    calc = Calculadora()

    plugins_para_carregar = ["multiplicacao", "divisao", "potencia", "media"]

    calc.load_plugins(plugins_para_carregar)

    print("\nCalculadora ")
    print("Operações disponíveis:")
    print(", ".join(calc.operations.keys()))

    while True:
        op = input("\nDigite a operação (ou 'sair'): ").strip().lower()
        if op == "sair":
            print("Encerrando...")
            break

        try:
            a = float(input("Primeiro número: "))
            b = float(input("Segundo número: "))
            resultado = calc.calculate(op, a, b)
            print(f"Resultado: {resultado}")
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()

