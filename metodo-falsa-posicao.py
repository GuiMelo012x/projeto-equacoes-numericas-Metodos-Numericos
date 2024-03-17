def metodo_fp(func, a, b, erro_aceitavel):
    def f(x):
        f = eval(func)  # Lê a string dada pelo usuário e transforma em uma função matemática
        return f

    i = 0  # O i será o contador de iterações.
    c_anterior = 0  # valor de c da iteração anterior.
    c = (a * f(b) - b * f(a)) / (f(b) - f(a))  # Calcula o primeiro valor de c.
    erro = abs(c-c_anterior)  # Calcula o erro entre c e o c_anterior.

   # Loop que irá girar até bater o número de iterações máximas.
    while erro > erro_aceitavel:
        c_prox = (a * f(b) - b * f(a)) / (f(b) - f(a))  # Calcula o próximo valor de c

        # Verifica se há raiz dentro do intervalo
        if f(a) * f(b) >= 0:
            print("Não há raiz.")
            quit()

        # Atualiza o intervalo baseado no f(c_prox)
        elif f(c_prox) * f(a) < 0:
            erro = abs(c_prox - b)  # Atualiza o erro
            b = c_prox  # Atualiza o limite superior do intervalo
            i = i + 1

        elif f(c_prox) * f(b) < 0:
            erro = abs(c_prox - a)  # Atualiza o erro
            a = c_prox  # Atualiza o limite inferior do intervalo
            i = i + 1


    print(f'O erro restante é {erro:.2f}, após {i} iterações')
    print(f'A raiz pode ser encontrada aproximadamente em {c_prox:.2f}')
    print(f'O limite inferior do intervalo "a" é {a:.2f} e o limite superior do intervalo "b" é {b:.2f}')

# Insira a sua função aqui:
metodo_fp("(x**3 - (3*x)**2 - (4*x) + 12)",0,2,0.001)

# f(x)= x³ - 3x² − 4x+12


'''

func = função dada pelo usuário como uma String, é convertida em uma função matemática na linha 3 com o "eval". 
a e b --> limites dos intervalos entre a raíz procurada.
erro_aceitavel --> critério de parada do método. Seria a precisão desejada para a solução.
c --> ponto intermediário calculado em cada iteração.
c_anterior --> inicializa a variável que armazena o valor de c da iteração anterior.
c_prox --> calcula o próximo valor de 'c'.
erro --> calcula o erro entre o c e o c_anterior. O erro é a diferença entre a estimativa atual da raiz e a estimativa anterior da raiz. Quando a diferença entre duas estimativas consecutivas da raiz for menor ou igual a erro_aceitavel, 
significa que encontramos uma boa aproximação para a raiz.

'''


