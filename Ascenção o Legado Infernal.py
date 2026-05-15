import time
import random
print ("Olá, Bem Vindo ao Ascenção Legado Infernal")
print (input("Insira um nome para iniciar: "))
idade = int(input("Insira sua idade: "))
if idade >= 14:
    print ("Idade aceita!")
    if idade >= 60:
        print("Olá vôvozinho, você está bem moderno eu acho!")
else:
    print ("Idade recusada!")
print()
print ("Esse mundo sugiu através da poeira cósmica de uma nebulosa orion...")
time.sleep(5)
print ("Com isso surgiram o Elementais, Smoke, Earth, Mizu e Mac")
time.sleep(5)
print ("Mas não foram somente os elementais que surgiram...")
time.sleep(4)
print ("Maxwell o ser omniversal mais forte de tudo e todos")
time.sleep(5)
print ("E Ercahaya uma ser de luz poderosa")
time.sleep(5)
print ("Nesse jogo você poderá selecionar um personagem dentre os indicados!")
time.sleep(5)
vida_maxwell = 7500
vida_mizu = 6000
vida_smoke = 6000
vida_earth = 6000
vida_mac = 6000
vida_ercahaya = 5000
print (f"Maxwell - {vida_maxwell} pontos de vida(HP)")
print (f"Mizu - {vida_mizu} pontos de vida(HP)")
print (f"Smoke - {vida_earth} pontos de vida(HP)")
print (f"Earth - {vida_smoke} pontos de vida(HP)")
print (f"Mac - {vida_mac} pontos de vida(HP)")
print (f"Ercahaya - {vida_ercahaya} pontos de vida(HP)")
time.sleep(5)
print ("Com seu personagem selecionado, a luta começa!!!")
time.sleep(5)
print ("Ercahaya against Mizu!")
time.sleep(1)
print ("3")
time.sleep(1)
print ("2")
time.sleep(1)
print ("1")
time.sleep(1)
print ("Fight")
time.sleep(1)
print ("Mizu ataca primeiro")
time.sleep(3)
num_round = 0
while vida_maxwell > 0 and vida_mizu > 0 and vida_ercahaya > 0 and vida_mac > 0 and vida_earth > 0 and vida_smoke > 0:
    num_round += 1
    print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ROUND {num_round} ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Escolha o ataque de Mizu: 1 - Soco, 2 - Chute, 3 - whirlpool, 4 - Hell Water")
    ataque = input()
    if ataque == "1":
        dano = 250
        print("Você deu um soco no adversário!")
    elif ataque == "2":
        dano = 300
        print("Você deu um chute no adversário!")
    elif ataque == "3":
        soma = 0
        for hit in range (1,5):
           dano = 350
           print (f"HIT {hit} - {dano}HP...")
           soma = soma + dano
        print(f"Você acertou o {soma} com magia!")
    elif ataque == "4":
        rounds_sangramento = 4
        dano = 500
        print("Você acertou o adversário com magia!")
    else:
        print("Ataque Inválido!")
    vida_ercahaya = vida_ercahaya - dano
    time.sleep(2)
    print (f"O ataque removeu {dano} HPs do adversário!")
    print(f"O personagem está com {vida_ercahaya}")
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    dano_ercahaya = random.randint(250,500)
    time.sleep(2)
    print("O adversário lhe atacou!")
    vida_mizu = vida_mizu - dano_ercahaya
    print (f"O ataque removeu {dano_ercahaya} HPs do adversário")
    if vida_mizu <= 0:
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        print("----Ercahaya winner----")
        print("~~~~~~~~~~~~~~~~~~~~~~~")
    elif vida_ercahaya <= 0:
        print("~~~~~~~~~~~~~~~~~~~")
        print("----Mizu winner----")
        print("~~~~~~~~~~~~~~~~~~~")