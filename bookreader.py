import PyPDF2
import pyttsx3

print("Skopiuj ścieżkę do pliku który chcesz odsłuchać\n"
      "Uwaga! Wklej ścieżkę bez cudzysłowia!\n"
      "sciezka:", end=' ')
while True:
    try:
        k = input()
        for i in k:
            if i == "\/":
                i == "\\"

        ksiazka = open(k, 'rb')
        czyt_pdf = PyPDF2.PdfFileReader(ksiazka)
        break

    except OSError:
        print('Nieprawidłowa ścieżka!\n'
              'Spróbuj ponownie:', end=' ')

print("Podaj numer stronu od ktorej chcesz zacząć czytanie:", end=' ')
numer = int(input())
od_strony = czyt_pdf.getPage(numer)
tekst = od_strony.extractText()

print("Podaj predkosc odtwarzania:  \n"
      "50 - 0.5x \n"
      "100 - normalna \n"
      "200 - 2x\n"
      "Predkosc:", end=' ')
Predkosc = input()
glos = pyttsx3.init()
glos.setProperty("rate", int(Predkosc))

print("wybierz język:\n"
      "1: polski \n"
      "2: angielski - amerykański\n"
      "3: angielski - brytyjski \n"
      "jezyk:", end=' ')

j = input()
i = int(j)
while True:

    if i == 1:
        voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PL-PL_PAULINA_11.0"
        break

    elif i == 2:
        voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        break

    elif i == 3:
        voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0"
        break
    else:
        print('podany numer jest nieprawidłowy sprobuj jeszcze raz')
        j = input()
        i = int(j)

glos.setProperty('voice', voice_id)
glos.say(tekst)
glos.runAndWait()
