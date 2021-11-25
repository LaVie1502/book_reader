import PyPDF2
import pyttsx3

print("Skopiuj ścieżkę do pliku który chcesz odsłuchać\n"
      "Uwaga! Wklej ścieżkę bez cudzysłowia!\n"
      "sciezka:", end=' ')
while True:
    try:
        b = input()
        for i in b:
            if i == "\/":
                i == "\\"

        book = open(b, 'rb')
        read_pdf = PyPDF2.PdfFileReader(book)
        break

    except OSError:
        print('Nieprawidłowa ścieżka!\n'
              'Spróbuj ponownie:', end=' ')

print("Podaj numer stronu od ktorej chcesz zacząć czytanie:", end=' ')
number = int(input())
from_page = read_pdf.getPage(number)
text = from_page.extractText()

print("Podaj predkosc odtwarzania:  \n"
      "50 - 0.5x \n"
      "100 - normalna \n"
      "200 - 2x\n"
      "Predkosc:", end=' ')
speed = input()
voice = pyttsx3.init()
voice.setProperty("rate", int(speed))

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

voice.setProperty('voice', voice_id)
voice.say(text)
voice.runAndWait()
