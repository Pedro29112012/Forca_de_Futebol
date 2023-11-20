import random
import os

x = True

    

def lprint(cor, texto, end="\n"):
    cor = int(cor)
    print(f"\033[38;5;{cor}m{texto}\033[38;5;255m", end=f"{end}")



os.system("cls")


def RodarJogo():
    df = []


    players = ['PELE', 'ZIDANE', 'RONALDO',
            'CRUYFF', 'RONALDINHO', 'CHARLTON', 'MALDINI', 'BECKENBAUER','BAGGIO', 'ZICO', 'VAN BASTEN', 'BARESI', 'EUSEBIO', 'CAFU', 'HENRY',
            'MOORE', 'DEL PIERO', 'MATTHAUS', 'ROBERTO CARLOS','BERGKAMP', 'PIRLO', 'RAUL', 'GULLIT', 'XAVI', 'BEST', 'CASSILAS', 'FIGO', "ETO'O",
            'NESTA', 'SCHEIMECHEL', 'PUYOL', 'CANNAVARO','STOICHKOV', 'LAHM', 'CANTONA', 'DROGBA', 'ZANETTI', 'NEDVED', 'VAN DER SAR', 'SCHOLES',
            'GERRARD', 'KLOSE', 'VAN PERSIE', 'BLANC','BECKHAM', 'CECH', 'ROONEY', 'KOEMAN', 'SHEVCHENKO', 'RIQUELME', 'LAUDRUP', "RIBERY",
            "XABI ALONSO", 'RIJKAARD', 'PETIT', 'VIDIC', 'PIRES', 'LAMPARD', 'BALLACK', 'ESSIEN','SNEIJDER', 'TEVEZ','KOMPANY', 'LITMANEN',
            'RUI COSTA', 'BERBATOV','LUCIO','ABEDI PELE','VOLLER','KOHLER','GINOLA','PAPIN','MORIENTES', 'FORLAN', 'MASCHERANO','MILITO',
            'GOMEZ', 'DI NATALE', 'MARQUEZ', 'OKOCHA', 'RICARDO CARVALHO', 'KEWELL', 'NAKATA', 'MARCHISIO', 'TOURE', 'BROLIN', 'JOE COLE',
            'CORDOBA', 'JI SUNG PARK', 'AL-JABER', 'DUDEK', 'CAPDEVILA', 'SMOLAREK', 'MOSTOVOI', 'DONOVAN', 'LJUNBERG', 'SOLSKJAER', 'KEANE',
            'CAHILL', 'AL OWAIRAN', 'CROUCH', "ROBBEN", 'JOHN TERRY', 'MANDZUKIC', 'RYAN GIGGS', 'BUFFON', 'TOTTI', 'IBRAHIMOVIC', 
            'MESSI', 'HAALAND', 'DE BRUYNE', 'VINICIUS JUNIOR', 'MBAPPE', 'RODRI', 'ALVAREZ', 'OSIMHEN','BERNARDO SILVA', 'MODRIC', 'SALAH',
            'LEWANDOWSKI', 'BOUNOU', 'GUNDOGAN', 'EMILIANO MARTINEZ', 'KVARATSKHELIA', 'BELLINGHAM', 'KANE', 'LAUTARO', 'GRIEZMANN',
            'KIM MIN JAE', 'ONANA','SAKA', 'GVARDIOL', 'MUSIALA', 'BARELLA', 'ODEGAARD', 'KOLO MUANI', 'RUBEN DIAS', 'CASEMIRO','ALISSON',
            'TER STEGEN','VAN DIJK', 'OBLAK', 'VALVERDE', 'BRUNO FERNANDES', 'KIMMICH','EDERSON', 'MARQUINHOS', 'KOBEL', 'MAIGNAN',
            'DONNARUMA', 'NEUER', 'DE JONG', 'HEUNG MIN SON', 'VERRATI','SZCZESNY', 'DEMBELE', 'PEDRI', 'ARAUJO', 'KROOS',
            'DYBALA', 'RAFAEL LEAO', 'DE LIGT', 'CANCELO', 'MILITAO', 'ROBERTSON', 'ALEXANDER ARNOLD', 'TONALI', 'NKUNKU', 'THOMAS PARTEY',
            'DI LORENZO', 'THEO HERNANDEZ', 'CALHANOGLU', 'VARANE', 'BERARDI', 'BASTONI', 'NAVAS', 'COMAN', 'LAPORTE','RUDIGER', 'KOUNDE', 'STONES',
            'TRIPPIER', 'DIOGO JOTA', 'WIRTZ', 'GORETZKA', 'RODRYGO', 'ALABA', 'RASHFORD', 'DECLAN RICE','GREALISH', 'FODEN', 'MARTINELLI',
            'BRUNO GUIMARAES', 'GABRIEL JESUS', 'LUIS DIAZ', 'RAPHINA', 'LUKAKU', 'TOMORI', 'SOMMER','SKRINIAR', 'ALCANTARA', 'LUCAS HERNANDEZ',
            'HAKIMI', 'DE PAUL', 'SANE', 'TCHOUAMENI', 'DEPAY', "ROMARIO", 'THOMAS MULLER', 'MADDISON','DIABY', 'REECE JAMES', 'CHIESA', 'SALIBA', 'GAVI',
            'GAKPO', 'ERIKSEN', 'DI MARIA', 'REUS', 'ALPHONSO DAVIES', 'STERLING', 'ENZO FERNANDEZ','UPAMECANO', 'MAC ALLISTER', 'ROGERIO CENI', 'LOCO ABREU', 'CESC FABREGAS']



    rp = random.choice(players)
    print("\033[38;5;255m  ")



    letras_usuario = []
    if len(rp) <= 5:
        chances = 6
    elif len(rp) <= 10 and len(rp) > 5:
        chances = 8
    elif len(rp) > 10:
        chances = 9

    ganhou = False
    h = 0
    if " " in rp:
        letras_usuario.append(" ")
        h = rp.count(" ")
    if "'" in rp:
        letras_usuario.append("'")
        h = rp.count("'")
    if "-" in rp:
        letras_usuario.append("-")
        h = rp.count("-")
    
    k = len(rp) - h

    while True:
        os.system("cls")
        lprint(202, (f"O jogador tem {k} letras"), "")
        print(" ")
        for letra in rp:
            if letra == " ":
                print(" ", end=" ")
                s = True
            elif letra == "'":
                lprint(33, "'", end=" ")
                g = True
            elif letra == "-":
                lprint(33, "-", end=" ")
                j = True
            elif letra.upper() in letras_usuario:
                lprint(33, f"{letra}", " ")
            else:
                lprint(160, "_", end=" ")

        print(f"   Você tem {chances} chances")

        print(f"Letras usadas: \033[38;5;28m{df}\033[38;5;255m", "")
        tentativa = input("Escolha uma letra para adivinhar: ")
        letras_usuario.append(tentativa.upper())
        if tentativa.upper() not in rp:
            df.append(tentativa.upper())

        if tentativa.upper() not in rp.upper():
            chances -= 1
        print("")

        ganhou = True
        for letra in rp:
            if letra.upper() not in letras_usuario:
                ganhou = False

        if chances == 0 or ganhou:
            if ganhou:
                    print(f"Parabéns, você ganhou. O jogador era: \033[38;5;46m{rp}\033[38;5;255m")
                        
            else:
                print(f"Você perdeu! O jogador era: \033[38;5;196m{rp}\033[38;5;255m")
            break
        print(" ")
        
       
        


RodarJogo()

while x == True:
    print()
    jogarDeNovo = input("Jogar de novo(S ou N)? ")
    print()
    if jogarDeNovo.upper() == "N":
        lprint(120, "Obrigado por jogar")
        x = False
        while True:
            break

        

    elif jogarDeNovo.upper() == "S":
        x = True
        RodarJogo()

    else:
        print("Resposta inválida")

