from flask import Flask, render_template, request, flash, redirect,url_for, send_file
from flask_mail import Mail, Message
from email_validator import validate_email, EmailNotValidError

app = Flask(__name__)
app.secret_key = 'jT4RzqLmR4B9bQwZH3fSgTUV8kHy'

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'contact.form2307@gmail.com'
app.config['MAIL_PASSWORD'] = 'wlfqkpkvfasoyvbp'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# Initialize Flask-Mail
mail = Mail(app)


@app.route("/",methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/LICENSE.txt")
def get_license():
    license_file_path = "LICENSE.txt"
    return send_file(license_file_path, mimetype="application/octet-stream")

@app.route("/service")
def service():
    return render_template("service.html")


@app.route("/containers")
def containers():
    return render_template("containers.html")


@app.route("/adr")
def adr():
    return render_template("adr.html")


@app.route("/slopage")
def slopage():
    return render_template("slopage.html")


@app.route("/sloservice")
def sloservice():
    return render_template("sloservice.html")


@app.route("/slocontainers")
def slocontainers():
    return render_template("slocontainers.html")


@app.route("/sloadr")
def sloadr():
    return render_template("sloadr.html")




@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        # Process the form data
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        try:
            # Validate email address
            v = validate_email(email)
            email = v.normalized if v else None

            if not email:
                raise EmailNotValidError("Invalid email address")
            # Send the email
            msg = Message('New Form from website',
                          sender=('Epac-logix website', 'contact.form2307@gmail.com'),
                          recipients=['amefis1991@gmail.com'])
            msg.body = f"Name: {fname} {lname}\nEmail: {email}\n\nMessage:\n{message}"
            mail.send(msg)

            success_message = 'Thank you for your message!'
            print("Success message flashed:", success_message)
            flash(success_message, 'success')
            return redirect(url_for('index'))
        except EmailNotValidError:
            flash('Please enter a valid email address.', 'error')
        except Exception as e:
            flash(f"An error occurred: {str(e)}", 'error')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
