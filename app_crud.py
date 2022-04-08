
flask_login.login_required
# If you decorate a view(route) with this, it will ensure that the current user is logged in and authenticated before calling the actual view.
# (If they are not, it calls the LoginManager.unauthorized callback.).
# Use this example for Hack #3.
@app_crud.route('/')
@login_required  # Flask-Login uses this decorator to restrict access to logged in users
def crud():
    """obtains all Users from table and loads Admin Form"""
    return render_template("crud.html", table=users_all())

# Unauthorised users do not get access to the SQL CRUD
# Flask-Login directs unauthorised users to this unauthorized_handler
@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    return redirect(url_for('crud.crud_login'))
