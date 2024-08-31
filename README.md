# Flask Guessing Game

This application is a simple web-based game where the computer guesses a number that the user chooses between 1 and 1000. The computer has a total of 10 attempts and uses a binary search method to find the correct number. The user helps the computer by indicating whether the guess is higher, lower, or correct.

## Functionality

1. **Game Initialization**: The game starts with the computer making its first guess in the middle of the 1 to 1000 range.

2. **User Responses**: The user has three buttons:
   - **Higher**: The response when the chosen number is higher than the computer's guess.
   - **Lower**: The response when the chosen number is lower than the computer's guess.
   - **Correct**: The response when the computer guesses the correct number.

3. **Game Continuation**: Based on the user's response, the computer adjusts its guess and tries again until it either guesses correctly or runs out of attempts.

4. **Win/Loss**: If the computer guesses the number correctly, a success page is displayed. If the computer fails to guess the number within 10 attempts, a failure page is displayed.

## Usage

### 1. Install Dependencies

First, install Flask:

```bash
pip install flask


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Flask Hádací Hra

Tato aplikace je jednoduchá webová hra, kde počítač hádá číslo, které si uživatel zvolí mezi 1 a 1000. Počítač má celkem 10 pokusů a používá metodu binárního hledání pro nalezení správného čísla. Uživatel pomáhá počítači tím, že mu odpovídá, zda je jeho odhad vyšší, nižší, nebo zda počítač číslo uhádl správně.

## Funkcionalita

1. **Inicializace hry**: Hra začíná tím, že počítač provede první odhad čísla uprostřed intervalu 1 až 1000.

2. **Uživatelské odpovědi**: Uživatel má tři tlačítka:
   - **Vyšší**: Odpověď, když je číslo, které si uživatel zvolil, vyšší než odhad počítače.
   - **Nižší**: Odpověď, když je číslo nižší než odhad počítače.
   - **Správně**: Odpověď, když počítač uhodne správné číslo.

3. **Pokračování hry**: Počítač na základě odpovědi uživatele upraví svůj odhad a pokouší se znovu, dokud buď neuhodne číslo, nebo mu nedojdou pokusy.

4. **Výhra/Prohra**: Pokud počítač uhodne číslo, zobrazí se stránka s informací o úspěchu. Pokud počítač neuhodne číslo v rámci 10 pokusů, zobrazí se stránka s informací o neúspěchu.

## Použití

### 1. Instalace závislostí

Nejprve nainstalujte Flask:

```bash
pip install flask
