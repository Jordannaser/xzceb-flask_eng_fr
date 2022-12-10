from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/english_to_french")
def english_to_french():
    text_to_translate = request.args.get('text_to_translate')
    return_french_result = translator.english_to_french(str(text_to_translate))
    return return_french_result

@app.route("/french_to_english")
def french_to_english():
    text_to_translate = request.args.get('text_to_translate')
    return_english_result = translator.french_to_english(str(text_to_translate))
    return return_english_result

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
