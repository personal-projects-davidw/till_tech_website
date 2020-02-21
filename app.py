from flask import Flask, flash, redirect, render_template, request

# Configure application
app = Flask(__name__)

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
        flash("Contact details submitted our team will be in touch shortly!")
        return redirect("/")


if __name__ == '__main__':
    app.run()
