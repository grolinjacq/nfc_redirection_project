from flask import Flask, request, redirect, render_template, url_for
import sqlite3

app = Flask(__name__)
db_path = 'nfc_data.db'  # Path to your SQLite database file

# API endpoint to update the configurable URL for a specific NFC tag ID
@app.route('/update_url', methods=['POST'])
def update_url():
    data = request.get_json()
    nfc_tag_id = data.get('nfc_tag_id')
    new_url = data.get('url')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("UPDATE nfc_tags SET url = ? WHERE tag_id = ?", (new_url, nfc_tag_id))
    conn.commit()
    conn.close()

    return 'URL updated successfully.'

# API endpoint to handle NFC tag redirection
@app.route('/redirect/<nfc_tag_id>')
def redirect_nfc(nfc_tag_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT url FROM nfc_tags WHERE tag_id = ?", (nfc_tag_id,))
    result = cursor.fetchone()
    conn.close()

    if result:
        return redirect(result[0])
    else:
        return 'NFC tag not found.'

# Home route to display the index.html page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nfc_id = request.form['nfc_id']
        return redirect(url_for('redirect_nfc', nfc_tag_id=nfc_id))
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
