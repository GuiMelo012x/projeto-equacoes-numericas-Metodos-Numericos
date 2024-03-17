
def metodo_bisseccao(func, a, b, erro_aceitavel):  
    """
    Implementa o método da bisseção para encontrar as raízes de uma função no intervalo [a, b]
    com uma margem de erro aceitável.

    Parâmetros:
    - func: string representando a função a ser avaliada.
    - a, b: limites do intervalo onde procuramos a raiz.
    - erro_aceitavel: margem de erro desejada para a raiz.

    Retorna:
    Nenhum. A função imprime as raízes, o erro final e o número total de iterações necessárias.
    """
    
    # Função interna para avaliar a função fornecida
    def f(x):
        f = eval(func)  # Usa a função eval para avaliar a expressão de string da função fornecida.
        return f  # Retorna o valor da função para um dado ponto x.
    
    error = abs(b - a)  # Calcula o erro inicial como a diferença absoluta entre os limites do intervalo.
    iteracoes = 0  # Inicializa o contador de iterações
    
    while error > erro_aceitavel:
        iteracoes += 1  # Incrementa o contador de iterações a cada iteração
        c = (b + a) / 2  # Calcula o ponto médio do intervalo.
        
        if f(a) * f(b) >= 0:  # Verifica se a função tem o mesmo sinal nos pontos extremos do intervalo.
            print("Sem raiz ou múltiplas raízes presentes. O método da bissecação não irá funcionar!")
            quit()
            
        elif f(c) * f(a) < 0:  # Verifica se a função muda de sinal entre 'a' e 'c'.
            b = c  # Atualiza o limite superior do intervalo para o ponto médio.
            error = abs(b - a)  # Atualiza o erro.
            
        elif f(c) * f(b) < 0:  # Verifica se a função muda de sinal entre 'c' e 'b'.
            a = c  # Atualiza o limite inferior do intervalo para o ponto médio.
            error = abs(b - a)  # Atualiza o erro.
        
        else:  # Se nenhuma das condições acima for atendida, algo de errado ocorreu.
            print("Algo de errado foi feito!")
            quit()
            
        # Imprime informações sobre a iteração atual
        print(f"Iteração {iteracoes}: Intervalo [{a:.2f}, {b:.2f}], Erro: {error:.2f}")
    
    # Após a convergência, imprime o erro final, as raízes inferior e superior do intervalo e o número total de iterações
    print(f"\nApós {iteracoes} iterações:") 
    print(f"O erro é {error:.2f}")
    print(f"A raiz inferior é {a:.2f}.\nA raiz superior é {b:.2f}")
    
    
# Testando a função
metodo_bisseccao("x**3 - 3*x**2 - 4*x + 12", -10, 10, 0.05)
print("==========================================//============================================")
metodo_bisseccao("x**3 - 3*x**2 - 4*x + 12", -5, 5, 0.05)