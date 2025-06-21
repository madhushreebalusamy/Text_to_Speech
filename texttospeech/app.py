from flask import Flask, render_template, request,send_file
import pyttsx3


app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    
    if request.method =='POST':
        text=request.form['text']
        voicen=int(request.form['voice'])
        rate=int(request.form['rate'])
        volume=float(request.form['volume'])

        engine=pyttsx3.init()
        voice=engine.getProperty('voices')
        engine.setProperty('voice',voice[voicen].id)
        engine.setProperty('rate', rate)
        engine.setProperty('volume', volume)
        filename = 'text.mp3'
        engine.save_to_file(text, filename)
        engine.runAndWait()
        return send_file(filename,as_attachment=True)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)