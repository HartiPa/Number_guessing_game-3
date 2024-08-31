from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    min_val = 1
    max_val = 1000
    attempts = 10
    guess = (max_val - min_val) // 2 + min_val
    return render_template('index.html', guess=guess, attempts=attempts, min_val=min_val, max_val=max_val)


@app.route('/guess', methods=['POST'])
def guess():
    # Získání odpovědi od uživatele
    response = request.form['response']

    # Získání aktuálních hodnot z formuláře
    min_val = int(request.form['min_val'])
    max_val = int(request.form['max_val'])
    attempts = int(request.form['attempts']) - 1
    guess = int(request.form['guess'])

    if response == 'correct':
        return render_template('success.html', guess=guess)
    elif response == 'higher':
        min_val = guess + 1
    elif response == 'lower':
        max_val = guess - 1


    if attempts > 0:
        guess = (max_val - min_val) // 2 + min_val
        return render_template('index.html', guess=guess, attempts=attempts, min_val=min_val, max_val=max_val)
    else:
        return render_template('failure.html')


if __name__ == '__main__':
    app.run(debug=True)

"""
Implementace reverzní hry na hádání čísel ve webové aplikaci pomocí frameworku Flask.
Uživatel má k dispozici formulář se třemi tlačítky: Příliš malý, Příliš velký, Vyhrál jsi.
Ukládání informací o aktuálních proměnných min a max do skrytých polí formuláře (pole typu hidden).
Poznámka: toto řešení není bezpečné, protože uživatel může toto html ručně změnit, například pomocí Firebugu.
V této situaci je však zcela dostačující.
Nejhorší, co se zde může stát, je, že si uživatel zkazí vlastní zábavu.
"""