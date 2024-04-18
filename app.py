from flask import Flask, render_template, request, flash, redirect,url_for,make_response
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

@app.route("/")
def test():
    return render_template("index.html")

@app.route("/logistics")
def logistics():
    return render_template("logistics.html")

@app.route("/scc")
def scc():
    return render_template("scc.html")

@app.route("/srb")
def srb():
    return render_template("srb.html")

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        try:
            # Process the form data
            fname = request.form.get('fname')
            lname = request.form.get('lname')
            email = request.form.get('email')
            subject = request.form.get('subject')
            message = request.form.get('message')

            # Check if all fields are provided
            if not (fname and lname and email and subject and message):
                raise ValueError("All fields are required")

            # Validate email address
            v = validate_email(email)
            email = v.normalized if v else None

            if not email:
                raise EmailNotValidError("Invalid email address")

            # Send the email
            msg = Message('New Form from website',
                          sender=('Epac-logix website', 'contact.form2307@gmail.com'),
                          recipients=['info@epac-logix.rs'])
            msg.body = f"Name: {fname} {lname}\nEmail: {email}\n\nMessage:\n{message}"
            mail.send(msg)

            success_message = 'Thank you for your message!'
            flash(success_message, 'success')
            return redirect(url_for('index'))

        except (EmailNotValidError, ValueError) as e:
            flash(str(e), 'error')
        except Exception as e:
            flash(f"An error occurred: {str(e)}", 'error')

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
