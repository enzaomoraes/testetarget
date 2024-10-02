def sequencia_fibonacci(n):
    
    def quadrado_perfeito(x):
        q = int(x**0.5)
        return q * q == x
    
    

    def numero_fibonacci(n):
        return quadrado_perfeito(5*n*n + 4) or quadrado_perfeito(5*n*n - 4)
    
    if numero_fibonacci(n):
        return f"o numero {n} pertence a sequencia de Fibonacci"
    else:
        return f"o numero {n} nao pertence a sequencia de Fibonacci"
    
    
    
numero = int(input("Digite um valor: "))
resultado = sequencia_fibonacci(numero)
print(resultado)