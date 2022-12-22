from ast import Try
import sqlite3

def validarusua(user,password):
    db=sqlite3.connect("database/base.s3db") 
    db.row_factory=sqlite3.Row
    cursor=db.cursor()
    consulta="SELECT *from user where username='"+user+"' and password='"+password+"' and estado='1'"
    cursor.execute(consulta)
    result=cursor.fetchall()
    return result

def registrar(fullname,username,password,codact):
    try:
        db=sqlite3.connect("database/base.s3db") 
        db.row_factory=sqlite3.Row
        cursor=db.cursor()
        consulta="insert into user (fullname,username,password,estado,codact) values ('"+fullname+"','"+username+"','"+password+"','0','"+codact+"')"
        cursor.execute(consulta)
        db.commit()
        return "usuario registrado satisfactoriamente" 
    except:
        return "Correo ya registrado"   

def activate(codact):
    db=sqlite3.connect("database/base.s3db") 
    db.row_factory=sqlite3.Row
    cursor=db.cursor()
    consulta="update user set estado='1' where codact='"+codact+"'"
    cursor.execute(consulta)
    db.commit()

    consulta2="SELECT *from user where codact='"+codact+"' and estado= '1' "
    cursor.execute(consulta2)
    result=cursor.fetchall()
    return result
    
    return "check"    

def listadestinatarios(user):
    db=sqlite3.connect("database/base.s3db") 
    db.row_factory=sqlite3.Row
    cursor=db.cursor()
    consulta="SELECT *from user where username<>'"+user+"'"
    cursor.execute(consulta)
    result=cursor.fetchall()
    return result

def crear_registro(remitente, destinatario, asunto, mensaje):
    db=sqlite3.connect("database/base.s3db") 
    db.row_factory=sqlite3.Row
    cursor=db.cursor()
    consulta="insert into messages (asunto,mensaje,fecha,hora,id_env,id_rec,estado) values ('"+asunto+"','"+mensaje+"',DATE('now'),TIME('now'),'"+remitente+"','"+destinatario+"','0')"
    cursor.execute(consulta)
    db.commit()
    return "check"


def Verenviados(correo):
    db=sqlite3.connect("database/base.s3db") 
    db.row_factory=sqlite3.Row
    cursor=db.cursor()
    consulta="select m.asunto,m.mensaje,m.fecha,m.hora,u.fullname from user u, messages m where u.username=m.id_rec and m.id_env='"+correo+"' order by fecha desc"
    cursor.execute(consulta)
    result=cursor.fetchall()
    return result

def Verrecibidos(correo):
    db=sqlite3.connect("database/base.s3db") 
    db.row_factory=sqlite3.Row
    cursor=db.cursor()
    consulta="select m.asunto,m.mensaje,m.fecha,m.hora,u.fullname from user u, messages m where u.username=m.id_env and m.id_rec='"+correo+"' order by fecha desc"
    cursor.execute(consulta)
    result=cursor.fetchall()
    return result

def cambiopass(password, correo):
    db=sqlite3.connect("database/base.s3db") 
    db.row_factory=sqlite3.Row
    cursor=db.cursor()
    consulta="update user set password='"+password+"' where username='"+correo+"'"
    cursor.execute(consulta)
    db.commit()
    return "check"