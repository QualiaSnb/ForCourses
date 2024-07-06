import random

kelime_listesi = ["kaya", "kara", "kare", "uzay", "yapay", "uzak"]

def kelime_sec():
    kelime = random.choice(kelime_listesi)
    return kelime.upper()

def oyun(kelime):
    word_display = "_" * len(kelime)
    tahmin = False
    tahmin_harfler = []
    tahmin_kelime = []
    hak = 6

    print(f"Hazırsan başlayalım! {hak} hakkın var ")
    print(word_display)
    print("\n")

    while not tahmin and hak > 0:
        oyuncunun_tahmini = input("Tahmininizi yazınız: ").upper()

        if len(oyuncunun_tahmini) == 1 and oyuncunun_tahmini.isalpha():
            if oyuncunun_tahmini in tahmin_harfler:
                print(f"{oyuncunun_tahmini} harfini daha önce denediniz.")
            elif oyuncunun_tahmini not in kelime:
                hak -= 1
                print (f"{oyuncunun_tahmini} harfi kelimede yok. {hak} hakkın kaldı.")
                tahmin_harfler.append(oyuncunun_tahmini)
            else:
                print(f"{oyuncunun_tahmini} harfi kelimede var.")
                tahmin_harfler.append(oyuncunun_tahmini)
                word_as_array = list(word_display)
                endeksler = [i for i, letter in enumerate(kelime) if letter == oyuncunun_tahmini]
                for index in endeksler:
                    word_as_array[index] = oyuncunun_tahmini
                word_display = "".join(word_as_array)
                if "_" not in word_display:
                    tahmin = True
        elif len(oyuncunun_tahmini) == len(kelime) and oyuncunun_tahmini.isalpha():
            if oyuncunun_tahmini == kelime:
                tahmin = True
                word_display = kelime
            elif oyuncunun_tahmini in tahmin_kelime:
                print(f"{oyuncunun_tahmini} kelimesini da önce denediniz.")
            else:
                print("Üzgünüm, bilemediniz.")
                tahmin_kelime.append(oyuncunun_tahmini)
                hak -= 1
        else:
            print("Geçersiz karakter!")
        print(word_display)
        print("\n")


    if tahmin:
        print("Tebrikler, bildiniz.")
    else:
        print(f"Bilemediniz. Doğru cevap: {kelime}")

def main():
    kelime = kelime_sec()
    oyun(kelime)

main()