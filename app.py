from flask import Flask, request, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from config import config

app = Flask(__name__)

# Set the Flask app configuration
app.config.from_object(config)

# Initialize the SQLAlchemy extension
db = SQLAlchemy(app)

# Define the NFC tag model
class NFCTag(db.Model):
    __tablename__ = 'nfc_tags'
    tag_id = db.Column(db.String(50), primary_key=True)
    url = db.Column(db.String(200))

    def __repr__(self):
        return f'<NFCTag {self.tag_id}>'

# API endpoint to handle NFC tag redirection
@app.route('/redirect/<nfc_tag_id>')
def redirect_nfc(nfc_tag_id):
    tag = NFCTag.query.filter_by(tag_id=nfc_tag_id).first()

    if tag:
        return redirect(tag.url)
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
