ficha = []
import random
print("=" * 30)
print("{:^30}".format(" SORTEIO "))
print("=" * 30)
while True:
    nome = str(input("Digite um participante: ")).upper()
    ficha.append(nome)
    resp = str(input("Quer continuar? [S/N]: "))
    while resp not in "SsNn":
        resp = str(input("\033[0;31mTente novamente. Quer continuar? [S/N]: \033[m"))
    if resp in "Nn":
        break
print("=" * 30)
print("{:^30}".format("LISTAGEM DE PARTICIPANTES"))
print("=" * 30)
print(f'{"ID"} {"JOGADOR":>20}')
for i, a in enumerate(ficha):
    print("-" * 30)
    print(f"{i+1}º {a:>20}")
    print("-" * 30)
aa = random.choice(ficha)
print(f"O GANHADOR FOI {aa}")
