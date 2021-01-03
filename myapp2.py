from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from PIL import Image
from io import BytesIO
import pandas_datareader.data as web


app = Flask (__name__)

@app.route("/")
def main():
    hosturl = "http://127.0.0.1:5000"
    return render_template("mainpage.html", host=hosturl)

@app.route("/tables", methods=['GET', 'POST'])
def show_tables():
    if request.method == 'POST':
      start = request.form.get("startdate")
      end = request.form.get("enddate")
      symbol = request.form.get("stock")
    else:
      start = '2017-04-22'
      end = '2018-04-22'
      symbol='AMZN'
     
    print(start) 
    data = web.DataReader('AMZN', 'yahoo', start=start, end=end)
    
    close = data[['Close']]
# rename the column with symbole nameß
    close = close.rename(columns={'Close': symbol})
    ax = close.plot(title='Amazon')
    ax.set_xlabel('date')
    ax.set_ylabel('close price')
    ax.grid()    
   
    #plt.savefig('plot1.png')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    #im = Image.open(buf)
    databyte = base64.b64encode(buf.getvalue()).decode('utf8')  
    
    #with open("plot1.png", "rb") as image_file:
    #    databyte = base64.b64encode(image_file.read()).decode('utf8')   

    buf.close()
    
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += databyte
    #im = Image.open(BytesIO(base64.b64decode(data)))
    #im.save('image1.png', 'PNG')
    
    return render_template('view.html',tables=[data.to_html(classes='female')],
    titles = ['na', 'data'], image=pngImageB64String)
    
@app.route('/chart')
def testImg():
    return render_template('images.html')
    
if (__name__) == "__main__":
    app.run()