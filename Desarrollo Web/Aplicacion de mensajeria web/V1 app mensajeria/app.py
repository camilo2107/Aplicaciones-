from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import hashlib
import controlador
import secrets
import enviomail


app = Flask (__name__)



secret = secrets.token_urlsafe(32)
app.secret_key = secret

originuser=""
 
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def log1():
    return render_template("inicio.html")
    
@app.route("/register")
def reg1():
    return render_template("registro.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usu=request.form["correo"]
        usu=usu.replace("SELECT","").replace("DELETE","").replace("INSERT","").replace("WHERE","").replace("UPDATE","")
        pas=request.form["password"]
        pas=pas.replace("SELECT","").replace("DELETE","").replace("INSERT","").replace("WHERE","").replace("UPDATE","")
        pas2=pas.encode()
        pas2=hashlib.sha384(pas2).hexdigest()
        response=controlador.validarusua(usu,pas2)
        global originuser
        if len(response)==0:
            originuser=""
            flash("Usuario inexistente o contraseña invalida")
            return render_template("principal.html")
        else:
            originuser=usu
            response2=controlador.listadestinatarios(usu)
            return render_template("principal.html",datas=response2)




@app.route('/register', methods=['GET', 'POST'])
def register():
     if request.method == 'POST':
        name=request.form["txtnombre"]
        name=name.replace("SELECT","").replace("DELETE","").replace("INSERT","").replace("WHERE","").replace("UPDATE","")
        usu=request.form["txtusuarioregistro"]
        usu=usu.replace("SELECT","").replace("DELETE","").replace("INSERT","").replace("WHERE","").replace("UPDATE","")
        pas=request.form["txtpassregistro"]
        pas=pas.replace("SELECT","").replace("DELETE","").replace("INSERT","").replace("WHERE","").replace("UPDATE","")
        pas2=pas.encode()
        pas2=hashlib.sha384(pas2).hexdigest()

        codact=datetime.now()
        codact2=str(codact)
        codact2=codact2.replace("-","")
        codact2=codact2.replace(" ","")
        codact2=codact2.replace(":","")
        codact2=codact2.replace(".","")
        print(codact2)

        mensaje= "Sr"+name+", usuario su codigo de activacion es :\n\n"+codact2+"\n\n Recuerde copiarlo y pegarlo para validarlo en la seccion de login y activar su cuenta.\n\nMuchas Gracias"
        enviomail.enviar(usu,mensaje,"código de activación")

        response=controlador.registrar(name,usu,pas2,codact2)

        
        flash(response)
        return render_template("inicio.html")
        

@app.route('/validate', methods=['GET', 'POST'])
def validate():
    if request.method == 'POST':
        codact=request.form["txtcodigo"]
        codac=codac.replace("SELECT","").replace("DELETE","").replace("INSERT","").replace("WHERE","").replace("UPDATE","")

    response=controlador.activate(codact)

    if len(response)==0:
        flash("El codigo es incorrecto intente de nuevo")
        return render_template("inicio.html")
    else:
        flash("usuario activo")
        return render_template("inicio.html")   



@app.route("/enviarMail", methods=['GET', 'POST'])
def enviarMAIL():
    if request.method == 'POST':
        destino=request.form["destino"]
        asunto=request.form["asunto"]
        mensaje=request.form["mensaje"]
        controlador.crear_registro(originuser,destino,asunto,mensaje)
        mensaje2= "tiene nuevos mensajes"
        #enviomail.enviar(destino,mensaje2,"Nuevo mensaje recibido") # aca desactivar para correo de la u
        return "Mensaje enviado"


@app.route("/Historialenviados", methods=['GET', 'POST'])        
def historialenviados():
    resultado=controlador.Verenviados(originuser)
    return render_template("respuesta.html",datas=resultado)


@app.route("/Historialrecibidos", methods=['GET', 'POST'])        
def historialrecibidos():
    resultado=controlador.Verrecibidos(originuser)
    return render_template("respuesta.html",datas=resultado)

@app.route("/Actualizapas", methods=['GET', 'POST'])
def Actualizapas():
    if request.method == 'POST':
        Npass=request.form["pass"]
        Npas2=Npass.encode()
        Npas2=hashlib.sha384(Npas2).hexdigest()
        controlador.cambiopass(Npas2,originuser)
        #flash("clave actualizada")
        return "Password actualizada"


    