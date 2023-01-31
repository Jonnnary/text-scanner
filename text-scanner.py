def count_words(text):
    words = text.split()
    return len(words)

# Datei öffnen
with open("test.txt", "r") as file:
    # Inhalt der Datei als String auslesen
    text = file.read()

# Eingabeaufforderung
search_term = input("Nach welchem Wort möchten Sie suchen? ")

# Überprüfung, ob das gesuchte Wort in einer der Zeilen vorhanden ist
found = False
count = 0
line_numbers = []
lines = text.split("\n")
for line_number, line in enumerate(lines, start=1):
    if search_term in line:
        line_numbers.append(line_number)
        found = True
        count += 1

if found:
    if count == 1:
        print(f"Das gesuchte Wort wurde in Zeile {line_numbers[0]} gefunden.")
    else:
        print(f"Das gesuchte Wort wurde in Zeilen {line_numbers} {count} mal gefunden.")
else:
    print("Das gesuchte Wort wurde nicht gefunden.")

number_of_words = count_words(text)
print(f"Der Text enthält {number_of_words} Wörter.")
