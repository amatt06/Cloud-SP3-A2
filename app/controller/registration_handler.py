from flask import request, redirect, url_for, render_template


def handle_registration():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the email already exists in the database
        user = User.query.filter_by(email=email).first()
        if user:
            return render_template('register.html', message='The email already exists.')

        # If the email is unique, create a new user and add them to the database
        new_user = User(email=email, username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        # Redirect the user to the login page
        return redirect(url_for('login'))

    # If the request method is not POST, render the registration page
    return render_template('register.html')
