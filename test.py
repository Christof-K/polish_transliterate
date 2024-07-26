from polish_transliterate.core import PolishTransliterate


transliterator = PolishTransliterate(transliterate_ops={'accent_peculiarity', 'math_symbol'})
normalized_text = transliterator.transliterate("Matematyka: 5 + 5 = 10, 2 * 3 = 6.")

print(normalized_text)


# Przykładowy tekst z akronimami i datą
text = "Pan dr Jan Kowalski spotkał się z prof. Nowakiem 12.12.2023 roku."

# Konfiguracja transliteracji, tutaj transliterujemy akronimy i daty
ops = {'acronym_phoneme', 'date'}

# Utworzenie instancji transliteratora z wybranymi operacjami
transliterator = PolishTransliterate(transliterate_ops=ops)

# Wykonanie transliteracji
normalized_text = transliterator.transliterate(text)

# Wyświetlenie znormalizowanego tekstu
print(normalized_text)

# Przykładowy tekst z symbolami walut i numerami
text = "Kwota wynosi 1000 zł i 2000 €, a czas to 2 godziny 30 minut."

# Konfiguracja transliteracji, tutaj transliterujemy waluty i numery
ops = {'amount_money', 'number'}

# Utworzenie instancji transliteratora z wybranymi operacjami
transliterator = PolishTransliterate(transliterate_ops=ops)

# Wykonanie transliteracji
normalized_text = transliterator.transliterate(text)

# Wyświetlenie znormalizowanego tekstu
print(normalized_text)