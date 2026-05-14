import time
print ("Olá, Bem Vindo ao Ascenção Legado Infernal")
print (input("Insira um nome para iniciar: "))
idade = int(input("Insira sua idade: "))
if idade >= 14:
    print ("Idade aceita!")
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
while vida_maxwell > 0 and vida_mizu > 0 and vida_ercahaya > 0 and vida_mac > 0 and vida_earth > 0 and vida_smoke > 0:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Escolha o ataque de Mizu: 1 - Soco, 2 - Chute, 3 - whirlpool, 4 - Hell Water")
    ataque = input()
    if ataque == "1":
        dano = 200
        print("Você deu um soco no adversário!")
    elif ataque == "2":
        dano = 300
        print("Você deu um chute no adversário!")
    elif ataque == "3":
        dano = 450
        print("Você acertou o adversário com magia!")
    elif ataque == "4":
        dano = 500
        print("Você acertou o adversário com magia!")
    else:
        print("Ataque Inválido!")
    time.sleep(2)
    vida_ercahaya = vida_ercahaya - dano
    print (f"O ataque removeu {dano} HPs do adversário!")
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Escolha o ataque de Ercahaya: 1 - Soco, 2 - Chute, 3 - Blindness, 4 - Manipulation :")
ataque= input()
if ataque == "1":
    dano = 250
    print("Você deu um soco no adversário!")
elif ataque == "2":
        dano = 300
        print("Você deu um chute no adversário!")
elif ataque == "3":
        dano = 450
        print("Você acertou o adversário com magia!")
elif ataque == "4":
        dano = 500
        print("Você acertou o adversário com magia!")
else:
        print("Ataque Inválido!")
        time.sleep(2)
        vida_mizu = vida_mizu - dano
        print (f"O ataque removeu {dano} HPs do adversário!")
if vida_mizu <= 0:
     print("~~~~~~~~~~~~~~~~~~~")
     print("----Mizu winner----")
     print("~~~~~~~~~~~~~~~~~~~")
elif vida_ercahaya <= 0:
     print("~~~~~~~~~~~~~~~~~~~~~~~")
     print("----Ercahaya winner----")
     print("~~~~~~~~~~~~~~~~~~~~~~~")