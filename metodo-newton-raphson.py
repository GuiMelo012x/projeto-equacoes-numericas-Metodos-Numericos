def newton_raphson(func, funcderiv, x, n):
    """
    Implementa o método de Newton-Raphson para encontrar as raízes de uma função.

    Parâmetros:
    - func: string representando a função.
    - funcderiv: string representando a derivada da função.
    - x: valor inicial para começar a iteração.
    - n: número máximo de iterações.

    Retorna:
    Nenhum. A função imprime a raiz encontrada e o número de iterações realizadas.
    """
    
    # Função interna para avaliar a função fornecida
    def f(x):
        f = eval(func)  # Avalia a função fornecida em um ponto x.
        return f
    
    # Função interna para avaliar a derivada da função fornecida
    def df(x):
        df = eval(funcderiv)  # Avalia a derivada da função fornecida em um ponto x.
        return df
    
    # Loop para realizar as iterações do método de Newton-Raphson
    for itercept in range(1, n):
        # Atualiza o valor de x usando a fórmula do método de Newton-Raphson
        i = x - (f(x) / df(x))
        x = i
    
    # Após o término do loop, imprime a raiz encontrada e o número de iterações realizadas
    print(f"A raiz foi encontrada em {x:.2f}, depois de {n} iterações")

# Testando a função
newton_raphson("x**2 - 2", "2*x", 2, 10)  # Encontra a raiz da função x^2 - 2, começando em x = 2, com no máximo 10 iterações.
newton_raphson("x**2 - 2", "2*x", -10, 10)  # Encontra a raiz da função x^2 - 2, começando em x = -10, com no máximo 10 iterações.
