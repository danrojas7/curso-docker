from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    # "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr05/15/9/anigif_enhanced-buzz-26388-1381844103-11.gif",
    # "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr01/15/9/anigif_enhanced-buzz-31540-1381844535-8.gif",
    # "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr05/15/9/anigif_enhanced-buzz-26390-1381844163-18.gif",
    # "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr06/15/10/anigif_enhanced-buzz-1376-1381846217-0.gif",
    # "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr03/15/9/anigif_enhanced-buzz-3391-1381844336-26.gif",
    # "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr06/15/10/anigif_enhanced-buzz-29111-1381845968-0.gif",
    # "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr03/15/9/anigif_enhanced-buzz-3409-1381844582-13.gif",
    # "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr02/15/9/anigif_enhanced-buzz-19667-1381844937-10.gif",
    # "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr05/15/9/anigif_enhanced-buzz-26358-1381845043-13.gif",
    # "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr06/15/9/anigif_enhanced-buzz-18774-1381844645-6.gif",
    # "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr06/15/9/anigif_enhanced-buzz-25158-1381844793-0.gif",
    # "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr03/15/10/anigif_enhanced-buzz-11980-1381846269-1.gif"
    
    "https://imagendegatos.com/wp-content/uploads/2017/03/Imagenes-Con-Movimiento.gif",
    "https://imagendegatos.com/wp-content/uploads/2017/03/Imagenes-De-Gato-Bailando.gif",
    "https://imagendegatos.com/wp-content/uploads/2017/03/Imagenes-De-Gatos-Con-Movimientos-De-Caricias.gif",
    "https://imagendegatos.com/wp-content/uploads/2017/03/Imagenes-De-Gatos-Encima-Del-Perro.gif",
    "https://imagendegatos.com/wp-content/uploads/2017/03/Imagenes-Gif-De-Gato-Limpiando.gif",
    "https://imagendegatos.com/wp-content/uploads/2017/03/Imagenes-Gif-De-Gato-Limpiando.gif",
    "https://imagendegatos.com/wp-content/uploads/2017/03/Imagenes-Gif-De-Gatos-Cari\u00F1osos.gif",
    "https://imagendegatos.com/wp-content/uploads/2017/03/Imagenes-Gif-De-Gatos-Para-Descargar.gif",
    "https://imagendegatos.com/wp-content/uploads/2017/03/Imagenes-Gif-De-Gatos-1.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")