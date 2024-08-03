import base64
from flask import Flask,render_template,request
import qrcode
from io import BytesIO
from base64 import b64encode


app=Flask(__name__)
#it is going to initialize our app

@app.route('/')

def home():
    #make sure you put your files in a folder named templates if you want it to work accordingly.
    return render_template('index.html')

@app.route('/',methods=['POST'])
def generateQR():
    memory=BytesIO()
    data=request.form.get('link')#the link is the name of the input zone in index.html
    img = qrcode.make(data)#we get the data here
    img.save(memory)#saving it to memory
    memory.seek(0)#reading the memory (the data from the memory from the beginning)
    
    base64_img='data:image/png;base64,' + \
        b64encode()(memory.getvalue()).decode('ascii')#encoding the data from the memory this is the raw value of it (memory.getvalue)
    return render_template('index.html',data=base64_img)#this will return and will allow us to basically rendering it.
if __name__=='__main__':
    app.run(debug=True)