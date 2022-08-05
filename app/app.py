from flask import *
from src.database import Connect, LoginCycle, RegisterLogin, sqlite3


app = Flask(__name__)
app.secret_key = "ChicoApp"


@app.route("/")
def index():
    if session.get("id") == "admin":
        return render_template("admin.html")

    if session.get("loggedIn"):
        return render_template("home.html")

    return render_template("login.html")


@app.get("/register")
def register():
    return render_template("register.html")

@app.get("/admin")
def admin():
    return render_template("admin.html")
  
@app.get("/cadCliente")
def cadCliente():
    return render_template("cadCliente.html")
  
@app.get("/cadPass")
def cadPass():
    return render_template("cadPass.html")
  
@app.get("/cadVeiculo")
def cadVeiculo():
    return render_template("cadVeiculo.html")
  
@app.get("/registroVeiculo")
def registroVeiculo():
    return render_template("registroVeiculo.html") 
  


@app.get("/login")
def login():
    if session.get("email"):
        return render_template("home.html")

    return render_template("login.html")
  


@app.get("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.get("/home")
def home():
    return render_template("home.html")


@app.post("/login")
def loginRoute():
  try:
    cpf      = request.form.get("cpf")
    email    = request.form.get("email")
    password = request.form.get("password")


  except Exception as err:
    flash("erro interno", "error")
    return redirect("/")

  if LoginCycle(cpf, email, password, Connect("app.db")):
    if email == "admin@admin.com":
      session["id"] = "admin"
      return redirect("/")

    session.clear()
    session["loggedIn"] = True
    session["email"] = email
    session.update()

    return redirect("/")

  flash("usuario nao encontrado", "error")
  return redirect("/")


@app.post("/register")
def registerRoute():
    try:
      name     = request.form.get("nome")
      cpf      = request.form.get("cpf")
      date     = request.form.get("date")
      city     = request.form.get("cidade")
      cep      = request.form.get("cep")
      email    = request.form.get("email")
      password = request.form.get("password")  
    except Exception as err:
      flash("erro interno", "error")
      return redirect("/")

    if RegisterLogin(name, cpf, date, city, cep, email, password, Connect("app.db")):
          session["loggedIn"] = True
          session["email"] = email
          session.update()

          return redirect("/")
    else:
        flash("erro interno", "error")
        return redirect("/")

if __name__ == "__main__":
    app.run()
