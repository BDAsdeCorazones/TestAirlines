from Conexion import *
import hashlib
import cherrypy

class Administrador(object):
    
    @cherrypy.expose
    def index(self):
        return """<html>
             <head></head>
             <body>
               <a href="aviones"> Aviones </a> </br>
               <a href="registrarse"> Registrarse </a>
             </body>
           </html> """

    @cherrypy.expose
    def registrarse(self):
        return """<html>
        <head></head>
        <body>
        <form action="createlogin">
          Nombres:
          <input type="text" name="nombre"><br>
          Apellidos:
          <input type="text" name="apellido"><br>
          Correo:
          <input type="text" name="correo"><br>
          Contrasena:
          <input type="password" name="secreto"><br>
          Confirma Contrasena:
          <input type="password" name="secreto"><br> 
              <button type="submit">Registrar</button>
        </form>
        </body>
        </html>"""

    @cherrypy.expose
    def createlogin(self, nombre, apellido, correo, secreto):
        con = Conexion()
        secret = hashlib.sha1()
        secret.update(secreto)
        if con.actualiza("insert into logins values('"+correo+"', '"+secret.hexdigest()+"', 'y');") == 1 :
            if con.actualiza("insert into administrador values('"+correo+"', '"+nombre+"', '"+apellido+"');") == 1:
                return "se creo"
            return "no se creo"
        else:
            return "no se creo"

    @cherrypy.expose
    def login(self):
        return """<html>
        <head>
          <scrip>
            
          </script>
        </head>
        <body>
        <form method="get" action="inicia">
          Correo:
          <input type="text" value="" name="correo"><br>
          Contrasena:
          <input type="password" value="" name="secreto"><br>
              <button type="submit">Give it now!</button>
        </form>
        </body>
        </html>"""
    
    @cherrypy.expose
    def inicia(self, correo, secreto):
        con = Conexion()
        secret = hashlib.sha1()
        secret.update(secreto)
        if(con.consulta("select secreto from logins where correo = '"+correo+"';") is None):
            return self.login()
        else:
            if(con.consulta("select secreto from logins where correo = '"+correo+"';")[0][0] == secret.hexdigest()):
                return self.admin(correo)
        return self.login()
    
    @cherrypy.expose
    def admin(self, correo):
        con = Conexion()
        usuario = con.consulta("select * from administrador where correo = '"+ correo+ "';")
        return "Bienvenido "+ usuario[0][1]
    
    @cherrypy.expose
    def promociones(self):
        return "Aqui se manejaran las promociones"

    @cherrypy.expose
    def estadisticas(self):
        return "Aqui se pondra todo lo de las estadisticas"

    @cherrypy.expose
    def vuelos(self):
        return "vuelos lalalala"
        
    @cherrypy.expose
    def aviones(self):
        con = Conexion()
        cuerpo = """<html>
          <head></head>
        <body>"""
        
        aviones = con.consulta("select * from avion")
        for avion in aviones:
            cuerpo = cuerpo + avion[1] + " "+ avion [2]+"" + " </br>"

        cuerpo = cuerpo + """
        </body>
        </html>"""
        return cuerpo

    @cherrypy.expose
    def viajes(self):
        con = Conexion()
        cuerpo = """<html>
        <head>
          <script>
            function quita(){
              var x = document.getElementById("viaje_origen");
              var s = x.value;
              var y = "Todos menos seleccionado "+ s;
              var n = document.getElementById("viaje_destino");
              var i;
              var j;
              for(j = 0; j < x.length; j++){
                n.remove(0);
              }
              if(s == 0){
                var o = document.createElement("option");
                o.text = "no ha seleccionado un pais";
                o.value = 0;
                fecha(0);
              } else{
                for(i = 1; i < x.length; i++){
                  if(s != x.options[i].value){
                    var o = document.createElement("option");
                    o.text = x.options[i].text;
                    o.value = x.options[i].value;
                    n.add(o);
                  }
                } 
                fecha(1);
              } 
            }
            function fecha(p){
              var m = document.getElementById("viaje_mes");
              var v = m.value;
              var i;
              var meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sept", "Oct", "Nov", "Dic"];
              if(p == 1){
                for(i = 0; i < 12; i++){
                  var o = document.createElement("option");
                  o.text = meses[i];
                  m.add(o);
                }
              } else {
                for(i = 0; i < 12; i++){
                  m.remove(0);
                }
              }
            }
          </script>
        </head>
        <body >
        <form method="post" action="createlogin">
          Origen:
          <select id="viaje_origen" name="origen" onchange="quita()">
            <option value="0">--Selecciona</option>"""
        ciudades = con.consulta("select nombre from ciudads")
        for ciudad in ciudades:
            cuerpo = cuerpo + """<option value=\""""+ ciudad[0] +"""">"""+ ciudad[0]+"""</option>"""
        cuerpo = cuerpo + """</select><br>Destino: <select id="viaje_destino" name="destino">"""
        cuerpo = cuerpo + """</select></br> Fecha:<select id="viaje_anio" name="anio">
        <option value="2014">2014</option><option value="2015">2015</option></select>
        <select id="viaje_mes" name="mes">
        </select>
        <select id="viaje_dia" name="dia"></select></br>
        Hora Salida: <select id="viaje_hora" name="hora"></select>
        <select id="viaje_minuto" name="minuto"></select></br>
        Distancia<input id="viaje_distancia" type="text" name="distancia"/></br>
        Avion:<select id="viaje_avion" name="idavion">
        """
        aviones = con.consulta("select * from avion")
        for avion in aviones:
            cuerpo = cuerpo + """<option value""""+avion[0]+"""">"""+avion[1]+", capacidad "+str(avion[3]+avion[4])+"""</option>"""
        cuerpo = cuerpo + """</select></br><button type="submit">Crea Viaje</button>
        </form>
        </body>
        </html>"""
        return cuerpo

        
if __name__ == '__main__':
    cherrypy.quickstart(Administrador())
