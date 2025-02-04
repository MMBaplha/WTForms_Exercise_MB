from flask import Flask, render_template, redirect, url_for, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "mardoAdopt"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
toolbar = DebugToolbarExtension(app)

connect_db(app)

with app.app_context():
    db.create_all()

@app.route("/")
def show_list_pets():
    """List of all pets."""
    
    pets = Pet.query.all()
    return render_template("pet_list.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def show_add_pet():
    """Add a pet."""

    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} has been added.", "success")
        return redirect(url_for('show_list_pets'))

    return render_template("add_pet.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def show_edit_pet(pet_id):
    """Edit pet and pet details."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} has been updated.", "success")
        return redirect(url_for('show_list_pets'))
    else:
        flash("Error: Form submission failed.", "danger")
        return render_template("pet_edit.html", form=form, pet=pet)

@app.route("/api/pets/<int:pet_id>", methods=['GET'])
def api_get_pet(pet_id):
    """Return info of pets in JSON."""

    pet = Pet.query.get_or_404(pet_id)
    info = {
        "name": pet.name,
        "age": pet.age,
        "species": pet.species,
        "available": pet.available
    }

    return jsonify(info)