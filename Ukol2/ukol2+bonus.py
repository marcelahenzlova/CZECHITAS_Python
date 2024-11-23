import requests

#Část 1:

ICO = input("Zadej ICO: ") #např. 22834958

response = requests.get('https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/' + ICO, verify=False)
subjekt_dle_ICO = response.json()
#print(subjekt_dle_ICO)

if 'kod' in subjekt_dle_ICO and subjekt_dle_ICO['kod'] == 'CHYBA_VSTUPU':
    print(subjekt_dle_ICO['popis']) #vypíše chybovou hlášku, pokud bude zadáno nesprávné IČO

else:
    print(subjekt_dle_ICO['obchodniJmeno'])
    print(subjekt_dle_ICO['sidlo']['textovaAdresa'])


#Část 2 + bonus:

headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

data = '{"obchodniJmeno": "moneta"}'
obchodniJmeno = input("Zadej obchodní jméno: ")
data = data.replace("moneta", obchodniJmeno)
data = data.encode("utf-8")
data2 = '{"kodCiselniku": "PravniForma", "zdrojCiselniku": "res"}'

res = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data, verify=False)
subjekt_dle_nazvu = res.json()
#print(subjekt_dle_nazvu)

res = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ciselniky-nazevniky/vyhledat", headers=headers, data=data2, verify=False)
ciselniky = res.json()
polozky_ciselniku = ciselniky['ciselniky'][0]['polozkyCiselniku']
#print(polozky_ciselniku)

def find_legal_form(a, b):
    for item in b:
        if item['kod'] == str(a): 
            for name in item['nazev']:
                return name['nazev']
    return None


if 'kod' in subjekt_dle_nazvu and subjekt_dle_nazvu['kod'] == 'CHYBA_VSTUPU':
    print(subjekt_dle_nazvu['popis']) #vypíše chybovou hlášku, pokud bude nalezeno více jak 1000 subjektů

else:
    pocet_subjektu = subjekt_dle_nazvu['pocetCelkem']
    seznam_subjektu = subjekt_dle_nazvu['ekonomickeSubjekty']

    print(f"Nalezeno subjektů: {pocet_subjektu}")
    for subjekt in seznam_subjektu:
        print(f"{subjekt['obchodniJmeno']}, {subjekt['ico']}, {find_legal_form(subjekt['pravniForma'], polozky_ciselniku)}")


    





