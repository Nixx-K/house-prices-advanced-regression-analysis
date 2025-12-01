# Wymogi i wytyczne dotyczące projektu końcowego

## Cel projektu
Celem projektu jest praktyczne zastosowanie umiejętności zdobytych w trakcie kursu do analizy rzeczywistego zbioru danych i zbudowania modelu uczenia maszynowego.

## Forma projektu
- **Zespoły**: Praca indywidualna lub zespołowa (maksymalnie 3 osoby)
- **Język programowania**: Python
- **Środowisko pracy**: Jupyter Notebook/Lab lub Google Colab
- **Prezentacja wyników**: 
  - Spójny raport w formacie PDF
  - Kody źródłowe w formatach: .ipynb i .py

## Wymagania dotyczące danych
- Zbiór danych musi zawierać:
  - Minimum 10 zmiennych objaśniających (cech)
  - Zarówno zmienne kategoryczne, jak i ciągłe
  - Minimalna liczba obserwacji: 1000
- Źródła danych:
  - Własne zbiory danych
  - Publicznie dostępne repozytoria (np. Kaggle, UCI ML Repository)
  - API z danymi
- Problem musi być jednoznacznie zdefiniowany jako:
  - Klasyfikacja (binarna lub wieloklasowa)
  - Regresja
Powyższe wymagania mogą być przedmiotem dyskusji. W przypadku gdy student posiada temat, który nie spełnia podanych kryteriów, ale jest szczególnie wartościowy merytorycznie i dydaktycznie, istnieje możliwość indywidualnego ustalenia warunków realizacji projektu.

## Struktura projektu
1. **Wprowadzenie**
   - Cel projektu
   - Opis problemu biznesowego/naukowego

2. **Eksploracja i analiza danych**
   - Opis zbioru danych
   - Opis wszystkich zmiennych
   - Analiza brakujących wartości i wartości odstających
   - Analiza statystyczna zmiennych
   - Identyfikacja kluczowych zależności

3. **Wizualizacja danych**
   - Wizualizacje rozkładów wszystkich zmiennych
   - Wykresy zależności między zmiennymi objaśniającymi a docelowymi
   - Macierz korelacji dla zmiennych ciągłych
   - Wykresy pudełkowe dla analizy zmiennych kategorycznych
   - Podsumowanie i wnioski z analizy wizualnej
   Uwaga: Każdy wykres musi posiadać tytuł, nazwy osi, legendę i odpowiednie etykiety.

4. **Przetwarzanie danych**
   - Czyszczenie danych
   - Kodowanie zmiennych kategorycznych
   - Skalowanie i normalizacja
   - Feature engineering
   - Wybór zmiennych
   - Podział na zbiór treningowy i testowy
   - Jak największa część przetwarzania powinna być w pipeline'ach

5. **Budowa modelu**
   - Wybór i uzasadnienie wybranych modeli
   - Trenowanie modeli
   - Optymalizacja hiperparametrów
   - Ocena jakości modeli

6. **Wyniki i wnioski**
   - Podsumowanie wyników
   - Wnioski z analizy

## Wymagania techniczne
- **Jakość kodu**:
  - Czytelność i odpowiednie formatowanie kodu
  - Zgodność ze standardem PEP 8
  - Logiczny podział na sekcje
  - Komentarze wyjaśniające kluczowe fragmenty kodu
  
- **Wykorzystane biblioteki** (minimalny zakres):
  - NumPy i Pandas - przetwarzanie danych
  - Matplotlib/Seaborn - wizualizacja danych
  - Scikit-learn - budowa modeli i tworzenie pipeline'ów danych

## Harmonogram realizacji
1. **Tydzień 4**: Wybór tematu i zespołu
   - Przesłanie propozycji tematu projektu i podziału grup
   - Charakterystyka planowanego zbioru danych

2. **Tydzień 8**: Wstępna analiza danych (po rozdziałach z Pandas)
   - Eksploracja wybranego zbioru danych
   - Wstępne analizy statystyczne
   - Wykrycie potencjalnych problemów

3. **Tydzień 12**: Wizualizacje (po rozdziałach z wizualizacją)
   - Kluczowe wizualizacje danych
   - Wstępne zależności między zmiennymi
   - Wnioski z analiz

4. **Ostatnie zajęcia**: Złożenie projektu końcowego
   - Kompletny raport w formie Jupyter Notebook
   - Działający kod
   - Prezentacja wyników

## Kryteria oceny (100%)
1. **Jakość i złożoność rozwiązania** (40%)
   - Trafność wyboru i zastosowania metod analitycznych
   - Stopień zaawansowania i adekwatność zastosowanych rozwiązań

2. **Dokumentacja i raportowanie** (30%)
   - Przejrzystość i spójność raportu końcowego
   - Jakość i czytelność wykonanych wizualizacji
   - Rzetelność i trafność wyciągniętych wniosków
   - Logiczna struktura prezentacji wyników

3. **Jakość kodu** (30%)
   - Czytelność i organizacja kodu źródłowego
   - Zastosowanie dobrych praktyk programistycznych
   - Jakość komentarzy i dokumentacji kodu

## Przydatne linki
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)
- [Scikit-learn dokumentacja](https://scikit-learn.org/stable/user_guide.html)
- [Pandas dokumentacja](https://pandas.pydata.org/docs/)

## Kontakt
Wszelkie pytania i wątpliwości związane z realizacją projektu proszę kierować do prowadzącego zajęcia drogą mailową.
