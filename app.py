from flask import Flask, flash, redirect, render_template, request
from flask_mail import Mail, Message

# Configure application
app = Flask(__name__)

app.config['SECRET_KEY'] = None
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEBUG'] = False
app.config['MAIL_USERNAME'] = None
app.config['MAIL_PASSWORD'] = None
app.config['MAIL_DEFAULT_SENDER'] = 'autotilltech@gmail.com'
app.config['MAIL_MAX_EMAILS'] = 2
app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    # method is GET so render page
    if request.method == "GET":
        return render_template("index.html")
    # method is POST so contact button pressed - redirect
    else:
        return redirect("/contact")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/rental")
def rental():
    return render_template("rental.html")


@app.route("/products")
def products():
    return render_template("products.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    # method is GET so render page for first time
    if request.method == "GET":
        return render_template("contact.html")

    # method is POST so form submitted
    else:
        cus_bus = request.form.get("business")
        cus_first = request.form.get("firstname")
        cus_last = request.form.get("lastname")
        cus_phone = request.form.get("phone")
        cus_email = request.form.get("email")
        cus_message = request.form.get("message")

        msg = Message('New Till Tech Customer Query',
                      recipients=[])
        msg.body = f"{cus_first} {cus_last} says: {cus_message}. Please email: {cus_email} or call {cus_phone}."
        mail.send(msg)

        flash("Contact details submitted our team will be in touch shortly!")
        return redirect("/")


if __name__ == '__main__':
    app.run()
