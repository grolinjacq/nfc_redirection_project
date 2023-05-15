from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

# Dictionary of NFC IDs and corresponding URLs
nfc_urls = {
    '0001': 'https://google.com',
    '0002': 'https://www.amazon.com/dp/B0987N5Q9L/ref=twister_B0987M7HB6?_encoding=UTF8&th=1&psc=1',
    '0003': 'https://netflix.com'
}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nfc_id = request.form['nfc_id']
        return redirect(url_for('nfc_redirect', nfc_id=nfc_id))
    else:
        return render_template('index.html')

@app.route('/nfc-redirect/<nfc_id>', methods=['GET'])
def nfc_redirect(nfc_id):
    if nfc_id in nfc_urls:
        return redirect(nfc_urls[nfc_id])
    else:
        return "Error: NFC ID not found."

if __name__ == '__main__':
    app.run(debug=True, port=8080)