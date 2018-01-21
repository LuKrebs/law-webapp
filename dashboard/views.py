from laracunha import app, db, uploaded_images
from flask import redirect, render_template, request, url_for, session, abort, flash

from sqlalchemy.sql import or_, and_, desc, asc

from dashboard.models import User
from dashboard.form import LoginForm
from dashboard.decorators import login_required, admin_required

from home.models import History, Area
from home.form import HistoryForm, AreaForm

from helpers import get_history

import bcrypt

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if session.get('email'):
        return redirect('dashboard')

    form = LoginForm()
    data = request.form
    error = None

    email    = data.get('email')
    password = data.get('password')

    if request.method == 'GET' and request.args.get('next'):
        session['next'] = request.args.get('next', None)

    if form.validate_on_submit():
        user = User.query.filter_by(email=email).first()

        if not user:
            error = "User doesn't exist"
            return render_template("dashboard/pages/admin.html", form=form, error=error)

        if not bcrypt.hashpw(password, user.password) == user.password:
            error = "Incorrect username or password"
            return render_template("dashboard/pages/admin.html", form=form, error=error)


        if user.is_admin:
            session['email']    = user.email
            session['fullname'] = user.fullname
            session['is_admin'] = user.is_admin

        if 'next' in session:
            next = session.get('next')
            session.pop('next')
            return redirect(next)

        return(redirect(url_for('dashboard')))

    return render_template("dashboard/pages/admin.html", form=form, error=error)


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    if not request.method == "GET":
        abort(401)

    session.pop('email')
    session.pop('fullname')
    session.pop('is_admin')

    return redirect(url_for("home"))

@app.route("/dashboard", methods=["GET"])
@login_required
@admin_required
def dashboard():
    user = User.query.filter_by(email=session.get('email')).first()

    return render_template('dashboard/pages/dashboard.html', user=user)


@app.route("/history/create", methods=["GET", "POST"])
@login_required
@admin_required
def create_history():
    form = HistoryForm()

    if form.validate_on_submit():
        history = History(
            complete_description=form.complete_description.data,
            short_description=form.short_description.data,
            office_name=form.office_name.data
        )

        db.session.add(history)
        db.session.commit()

        flash('Descrição criada com sucesso')

        return redirect(url_for('edit_history', history_id=history.id))

    return render_template('dashboard/pages/history/create.html', form=form, action="create")


@app.route("/history/edit", methods=["GET", "POST"])
@app.route("/history/<int:history_id>/edit", methods=["GET", "POST"])
@login_required
@admin_required
def edit_history(history_id=None):
    history = get_history(history_id)
    form = HistoryForm(obj=history)

    if form.validate_on_submit():
        form.populate_obj(history)
        db.session.commit()

        return render_template('dashboard/pages/history/show.html', history=history)

    return render_template('dashboard/pages/history/edit.html', history=history, form=form, action="edit")



@app.route("/history/<int:history_id>/show", methods=["GET", "POST"])
@login_required
@admin_required
def show_history(history_id):
    history = History.query.filter(and_(History.active==True, History.id==history_id)).first()

    return render_template('dashboard/pages/history/show.html', history=history)


@app.route("/area/create", methods=["GET", "POST"])
@login_required
@admin_required
def create_area():
    form = AreaForm()

    if form.validate_on_submit():
        image = request.files.get('image')
        filename = None
        try:
            filename = uploaded_images.save(image)
        except:
            flash("The image was not uploaded")

        area = Area(
            name=form.name.data,
            image=filename,
        )

        db.session.add(area)
        db.session.commit()

        flash('Área criada com sucesso')

        return redirect(url_for('edit_area', area_id=area.id))

    return render_template('dashboard/pages/area/create.html', form=form, action="create")


@app.route("/area/<int:area_id>/edit", methods=["GET", "POST"])
@login_required
@admin_required
def edit_area(area_id):
    area = Area.query.get(area_id)
    form = AreaForm(obj=area)

    if form.validate_on_submit():
        form.populate_obj(area)

        if form.image.has_file():
            image = request.files.get('image')
            filename = uploaded_images.save(image)
            area.image = filename

        db.session.commit()

        return redirect(url_for('show_area', area_id=area.id))

    return render_template('dashboard/pages/area/edit.html', area=area, form=form, action="edit")


@app.route("/area/<int:area_id>/show", methods=["GET", "POST"])
@login_required
@admin_required
def show_area(area_id):
    area = Area.query.get(area_id)

    return render_template('dashboard/pages/area/show.html', area=area)
