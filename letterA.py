def letter_a(texto):
    count_a = texto.lower().count('a')

    if count_a > 0:
        return f"A letra 'a' aparece {count_a} vezes na string."
    else:
        return "A letra 'a' não foi encontrada na string."

entrada = input("Informe uma frase: ")
resultado = letter_a(entrada)
print(resultado)
