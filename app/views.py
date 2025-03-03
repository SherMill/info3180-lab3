from app import app, mail
from flask import render_template, request, redirect, url_for, flash
from .forms import ContactForm
from flask_mail import Message

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


###
# The functions below should be applicable to all Flask apps.
###


"""New route for Contact"""
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        msg = Message(
                subject=form.subject.data,
                sender=("Sheri-lee Mills", "millssherilee@gmail.com"),
                recipients=["millssherilee@gmail.com"],
            )
        mail.send(msg)
        msg.body = form.message.data
        mail.send(msg)
        flash('Your message has been sent!!!', 'Successfully Sent')
        return redirect(url_for('home'))
    return render_template('contact.html', form=form)




# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
