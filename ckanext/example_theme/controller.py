from flask import render_template

class MyLogic():
    def do_something():
        return render_template("iletisim.html")
    
    def show_acikveri():
        return render_template("acikveri.html")