from flask import Flask, request,  jsonify, render_template, url_for, send_file
from gtts import gTTS  
from slugify import slugify
#from tempfile import  TemporaryFile
#from playsound import playsound
import time



app = Flask(__name__)
app.config.from_pyfile('config.py')



@app.route('/')
def index():
    #term=request.args.get('q')
    #if not term:
    #    term = 'bhojpuri'

    #data =UAPI.search(term)
    #request.args.get('q')
    #print(data)
    data ='';
    return render_template('reader-board.html', data = data)


@app.route('/speak', methods=['GET', 'POST'])
def uwiki_speak():

    #request.args.get('q')
    response=request.form['txt']
    filepath="uploads/"+slugify(response[0:30], to_lower=True)+"_"+str(time.time_ns())+".mp3"
    print("Writing start")
    tts = gTTS(text=response, lang='en', slow=False) 
    
    #f = TemporaryFile()
    #tts.write_to_fp(f)
    #f.seek(0)
    #playsound(f)
    #time.sleep(5)
    #f.close()

    tts.save(filepath)
    return send_file(filepath, as_attachment=True)
    #return "Hello"
    #response =UAPI.search(request.args.get('q'))
    #pass
    #redirect(url_for('dashboard',name = user))
    #return jsonify("Successfully")


@app.errorhandler(404)
def not_found(error):
    return 'Page not found!' 