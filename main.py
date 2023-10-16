import random

# Lista de palavras para o jogo
palavras = ['jesus', 'maria', 'jose', 'pedro', 'paulo']

def escolher_palavra():
    return random.choice(palavras)

def desenhar_forca(tentativas):
    forca = [
        "   ____\n  |    |\n       |\n       |\n       |\n       |\n=========",
        "   ____\n  |    |\n  O    |\n       |\n       |\n       |\n=========",
        "   ____\n  |    |\n  O    |\n  |    |\n       |\n       |\n=========",
        "   ____\n  |    |\n  O    |\n /|    |\n       |\n       |\n=========",
        "   ____\n  |    |\n  O    |\n /|\\   |\n       |\n       |\n=========",
        "   ____\n  |    |\n  O    |\n /|\\   |\n / \\   |\n       |\n========="
    ]
    return forca[5 - tentativas]

def jogar_forca():
    palavra = escolher_palavra()
    letras_adivinhadas = []
    tentativas = 5

    print("Bem-vindo ao Jogo da Forca!")

    while True:
        palavra_mascarada = ""
        for letra in palavra:
            if letra in letras_adivinhadas:
                palavra_mascarada += letra
            else:
                palavra_mascarada += "_"

        print("Palavra: " + palavra_mascarada)
        print("Letras adivinhadas: " + ", ".join(letras_adivinhadas))
        print("Tentativas restantes: " + str(tentativas))
        print(desenhar_forca(tentativas))

        if palavra_mascarada == palavra:
            print("IHUU! ACERTOOOOU! A PALAVRA ERA: " + palavra)
            break

        if tentativas == 0:
            print("QUE PENA! NÃO FOI DESSA VEZ. A PALAVRA ERA: " + palavra)
            break

        tentativa = input("Digite uma letra: ").lower()

        if tentativa in letras_adivinhadas:
            print("Você já tentou esta letra.")
        else:
            letras_adivinhadas.append(tentativa)
            if tentativa not in palavra:
                tentativas -= 1
                print("Letra errada. Tente novamente.")

if __name__ == "__main__":
    jogar_forca()
