from time import sleep
from random import randint
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def introducao():
    print('Hoje é um belo dia para passear, não acha?')
    sleep(2)
    print("...")
    sleep(3)
    print("Você pede um Uber até uma loja de alugueis de carro")
    sleep(2)
    print("...")
    sleep(3)
    print("O Uber chega")
    sleep(2)
    print("...")
    sleep(3)


def mostrar_opcoes_concessionaria(opcoes):
    print("Qual concessionária você pretende ir?")
    sleep(1)
    for numero, concessionaria in opcoes.items():
        print(f"{numero}- {concessionaria}")


def escolher_concessionaria(opcoes_concessionarias):
    while True:
        esc = input('Escolha uma concessionária digitando seu respectivo número: ')
        if esc in opcoes_concessionarias:
            print(f"Você escolheu {opcoes_concessionarias[esc]}")
            return opcoes_concessionarias[esc]
        else:
            print("Opção inválida, insira um número válido para continuar")
            sleep(2)


def chegou_concessionaria(concessionarias_escolhidas):
    print(f'Você chegou na {concessionarias_escolhidas}')
    sleep(3)
    print("...")
    sleep(3)
    print('Um funcionário chega para te atender')
    sleep(4)


def mostrar_opcoes_carro(opcoes, page):
    clear_screen()
    print(f'Página {page}: Opções de carros para alugar')
    print('-----------------------------------------')
    sleep(2)
    start_index = (page - 1) * 50
    end_index = min(page * 50, len(opcoes))
    for numero, carro in opcoes.items():
        if start_index < int(numero) <= end_index:
            print(f"{numero}- {carro}")
    print('-----------------------------------------')


def escolher_carro(opcoes):
    while True:
        esc = input('Escolha um carro digitando seu respectivo número: ')
        if esc in opcoes:
            return opcoes[esc]
        else:
            print("Opção inválida. Por favor, escolha um número válido.")


def corrida(carro):
    print(f'Você escolheu o {carro}, um ótimo carro')
    sleep(2)
    print(f'Você vai para uma rodovia testar essa belezinha de carro {carro}')
    sleep(2)
    print('Um carro cola ao seu lado buzinando para começar um racha!')
    sleep(2)
    print('Você todo empolgado começa a acelerar')
    velocidade = randint(200, 520)
    if velocidade <= 280:
        print('Vocês correm por vários quilômetros...')
        sleep(2)
        print('Você, na emoção do momento, acaba não percebendo um radar de velocidade logo à frente, mas, '
              'para sua sorte, você estava dentro da velocidade permitida')
        sleep(2)
        print('Infelizmente o outro carro foi mais rápido que você e você acaba perdendo o racha')
    else:
        print('Vocês correm por vários quilômetros...')
        sleep(2)
        print('Você, no calor do momento, acaba nem percebendo o radar de velocidade logo à frente...')
        sleep(2)
        print("E acaba passando do limite de velocidade permitido na rodovia")
        multa = (velocidade - 90) * 5
        sleep(2)
        print(f'No dia seguinte você recebe uma carta com uma multa de velocidade de R${multa} por passar no radar de '
              f'velocidade com {velocidade} Km/h')
        sleep(2)
        print('Pelo menos você acaba ganhando o racha')


def continuar():
    return input("Deseja fazer outra corrida? (s/n): ").strip().lower() == 's'

if __name__ == "__main__":
    introducao()

    opcoes_concessionaria = {
        "1": "Veiculos do Niro",
        "2": "Padaria Motors",
        "3": "Kléber Carros",
        "4": "Carrinhos Carandiru",
        "5": "Posto dos Picosos",
        "6": "Carros do Zé",
        "7": "Legendary Motors",
        "8": "Classic Cars",
        "9": "Furacão de Preços",
        "10": "Veiculos da Peste"
    }
    mostrar_opcoes_concessionaria(opcoes_concessionaria)
    concessionaria_escolhida = escolher_concessionaria(opcoes_concessionaria)
    chegou_concessionaria(concessionaria_escolhida)

    opcoes_carro = {
        "1": "Toyota Supra MK4",
        "2": "Porsche GT3 RS",
        "3": "Ford/Shelby Mustang",
        "4": "Nissan GTR Skyline R34",
        "5": "Lamborghini Aventador",
        "6": "Ferrari F8 Spider",
        "7": "Mercedes-Benz CLA 35 AMG",
        "8": "McLaren Artura",
        "9": "Mitsubishi Lancer Evolution",
        "10": "BMW M3 Competition",
        "11": "Mazda RX7",
        "12": "Dodge Charger (1996)",
        "13": "Chevrolet Camaro ",
        "14": "Acura NSX (2018)",
        "15": "Audi R8 Sport Edition",
        "16": "Alfa Romeo Giulia",
        "17": "Bugatti Chiron",
        "18": "Koenigsegg Agera RS",
        "19": "Jaguar F-Type",
        "20": "Subaru WRX STI Launch Edition",
        "21": "Mitsubishi Eclipse GST",
        "22": "McLaren P1",
        "23": "BMW i8",
        "24": "Willys Interlagos",
        "25": "Puma GTE",
        "26": "Chevrolet Opala SS",
        "27": "Dodge Charger R/T",
        "28": "Ford Maverick GT",
        "29": "Fiat Uno Turbo i.e",
        "30": "Lamborghini Hurancán",
        "31": "Volkswagen Golf GTI",
        "32": "Aston Martin DB5",
        "33": "Aston Martin DBS Superleggera",
        "34": "Ariel Atom 500",
        "35": "Audi R8 V10 Plus",
        "36": "BMW M1",
        "37": "BMW M2 Competition",
        "38": "BMW M3 E46",
        "39": "BMW M3 GTS Coupe E92",
        "40": "Bugatti Veyron",
        "41": "Cadillac CTS-V",
        "42": "Chevrolet Camaro SS 1969",
        "43": "Chevrolet Camaro Z/28 (2014)",
        "44": "Chevrolet Corvette C6 ZR1",
        "45": "Chevrolet Corvette Stingray 1966-1967",
        "46": "Datsun 240Z",
        "47": "DeTomaso Pantera",
        "48": "Dodge Challenger Demon",
        "49": "Dodge Viper",
        "50": "Ferrari 246 GT Dino",
        "51": "Ferrari 250 GTO",
        "52": "Ferrari F40",
        "53": "Ferrari 458 Speciale",
        "54": "Ferrari La Ferrari",
        "55": "Ford GT (primeira geração)",
        "56": "Ford Mustang Shelby GT350R",
        "57": "Ford RS200",
        "58": "Hennessey Venom F5",
        "59": "Honda Integra Type R",
        "60": "Honda NSX (primeira geração)",
        "61": "Jaguar E-Type",
        "62": "Jaguar F-Type",
        "63": "Jaguar XE SV Project 8",
        "64": "Koenigsegg Jesko",
        "65": "Lamborghini Aventador LP770-4 SVJ",
        "66": "Lamborghini Gallardo LP570-4 Superleggera",
        "67": "Lamborghini Huracan Performante",
        "68": "Lamborghini Miura",
        "69": "Lamborghini Murciélago LP670-4 SuperVeloce",
        "70": "Lancia Stratos",
        "71": "Lexus LFA",
        "72": "Lotus Elise",
        "73": "Lotus Esprit V8",
        "74": "Mazda MX-5",
        "75": "McLaren P1 GTR",
        "76": "McLaren F1",
        "77": "McLaren Senna",
        "78": "Mercedes-Benz 300SL 1954",
        "79": "Mercedes-Benz AMG GT-R Pro",
        "80": "Mercedes-Benz SLS AMG Black Series",
        "81": "Nissan 300ZX",
        "82": "Nissan 370Z",
        "83": "Nissan Skyline R32",
        "84": "Pagani Huayra R",
        "85": "Porsche 911",
        "86": "Porsche 918 Spyder",
        "87": "Porsche 956",
        "88": "Porsche Carrera GT",
        "89": "Shelby 289 Cobra",
        "90": "Shelby 427 Cobra",
        "91": "Toyota 2000 GT",
        "92": "Drako GTE",
        "93": "De Tomaso P72",
        "94": "McLaren Elva",
        "95": "Czinger 21C",
        "96": "Ferrari Monza",
        "97": "Gordon Murray T.33",
        "98": "Koenigsegg Gemera",
        "99": "Zenvo TSR-S",
        "100": "W Motors Lykan Hypersport",
        "101": "Nissan 350z",
        "102": "Honda Civic Type R",
        "103": "Acura RSX-S (2004)",
        "105": "Beck Kustoms F132",
        "106": "Chevrolet Camaro Z28",
        "107": "Chevrolet Corvette Z06",
        "108": "Dodge Challenger SRT8",
        "109": "Dodge Viper SRT",
        "110": "Ferrari 458 Italia",
        "111": "1932 Ford",
        "112": "Ford Focus RS",
        "113": "Ford Mustang (1965)",
        "114": "Ford Mustang Boss 302 (1969)",
        "115": "Ford Mustang Foxbody (1990)",
        "116": "Honda NSX Type-R",
        "117": "Honda S2000",
        "118": "Lamborghini Diablo SV",
        "119": "Lamborghini Murcielago LP 670-4 SV",
        "120": "Lotus Exige S",
        "121": "Nissan 180sx Type-x",
        "122": "Nissan Fairlady 240ZG",
        "123": "Nissan Silvia Spec-R",
        "124": "Nissan Skyline GT-R KPGC10",
        "125": "Porsche 911 Carrera RSR 2.8",
        "126": "Scion FR-S",
        "127": "Subaro Impreza WRX STI",
        "128": "Toyota GT86",
        "129": "Toyota Sprinter GT APEX",
        "130": "Toyota Supra SZ-R",
        "131": "Volvo 242 (1975)",
        "132": "BMW M3 E46 Deluxe",
        "133": "Ken´s Hoonicorn Ford Mustang (1965)",
        "134": "Morohoshi´s Lamborghini Diablo SV (1999)",
        "135": "Eddie´s Nissan Skyline GT-R V-Spec (1999)",
        "136": "Aston Martin Vulcan",
        "137": "Aston Martin DB11",
        "138": "Audi S5 Sportback",
        "139": "BMW M3 Evolution II E30",
        "140": "BMW M4 GTS",
        "141": "BMW M5",
        "142": "BMW X6 M",
        "143": "Chevrolet Bel Air",
        "144": "Chevrolet C10 Sidestep Pickup",
        "145": "Ford Crown Victoria",
        "146": "Ford F-150 Raptor",
        "147": "Ford GT",
        "148": "Infiniti Q60 S",
        "149": "Land Rover Defender 110",
        "150": "Land Rover Range Rover Sport SVR",
        "151": "McLaren 570S Coupé",
        "152": "Mercedes-AMG A 45",
        "153": "Mercedes-AMG G 63",
        "154": "Mercedes-AMG GT",
        "155": "Mercury Cougar",
        "156": "Mini JCW Countryman",
        "157": "Plymouth Barracuda",
        "158": "Pontiac Firebird",
        "159": "Volkswagen Beetle",
        "160": "Volkswagen Golf GTI Clubsport",
        "161": "Volvo 242DL",
        "162": "Volvo Amazon P130",
        "163": "Abarth 124 Spider",
        "164": "Abarth 595 esseesse",
        "165": "Abarth 695 Biposto",
        "166": "Abarth Fiat 131",
        "167": "Alfa Romeo 155 Q4",
        "168": "Alfa Romeo 4C",
        "169": "Alfa Romeo 8C Competizione",
        "170": "Alfa Romeo 8C Competizione F.E.",
        "171": "Alfa Romeo 33 Stradale",
        "172": "Alfa Romeo Giulia Sprint GTA Stradale",
        "173": "Alfa Romeo Giulia TZ2",
        "174": "Alfa Romeo Giulia Quadrifoglio",
        "175": "Alfa Romeo Giulia Quadrifoglio F.E.",
        "176": "Alfa Romeo P3",
        "177": "Alfa Romeo Stelvio Quadrifoglio",
        "178": "Alpine A110",
        "179": "Alumi Craft Class 10 Race Car",
        "180": "Alumi Craft Class 10 Race Car F.E.",
        "181": "AMC Gremlin X",
        "182": "AMC Javelin AMX",
        "183": "AMC Rebel 'The Machine'",
        "184": "Apollo Intensa Emozione",
        "185": "Ascari KZ1R",
        "186": "Chevrolet Chevette Pais Tropical",
        "187": "Chevrolet Celta Piquet",
        "188": "Fiat Stilo Blackmotion 2.4",
        "189": "Fiat Oggi CSS",
        "190": "Volkswagen TL personalizado",
        "191": "Volkswagen Fusca 1300 GL",
        "192": "Chrysler Esplanada GTX",
        "193": "Ford Corcel II Van",
        "194": "Willys Itamaraty Executivo",
        "195": "Chevrolet Monza Hi Tech",
        "196": "Ford Escort XR3 75 Special Edition",
        "197": "Chevrolet Diplomata Collector",
        "198": "Ford Escort XR3 Fórmula",
        "199": "Fiat Brava HGT 2.4",
        "200": "Volkswagen Karmann Ghia Conversível"
    }

    page = 1
    pages = len(opcoes_carro) // 50 + 1
    for page in range(1, pages + 1):
        while True:
            mostrar_opcoes_carro(opcoes_carro, page)
            carro_escolhido = escolher_carro(opcoes_carro)
            corrida(carro_escolhido)
            if not continuar():
                break
