from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    date_of_birth = db.Column(db.Date)

    contacts = db.relationship('Contacts', backref='user', lazy=True)
    education = db.relationship('Education', backref='user', lazy=True)
    skills = db.relationship('Skills', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.firstname} {self.lastname}>'

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contact_type_id = db.Column(db.Integer, db.ForeignKey('contact_types.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    contact_value = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return f'<Contact {self.contact_value}>'

class ContactTypes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contact_type = db.Column(db.String(30), nullable=False)
    contact = db.relationship('Contacts', backref='contact_type', lazy=True)

    def __repr__(self):
        return f'<ContactType {self.contact_type}>'

class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    education_type_id = db.Column(db.Integer, db.ForeignKey('education_types.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    education_value = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return f'<Education {self.education_value}>'

class EducationTypes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    education_type = db.Column(db.String(50), nullable=False)
    education = db.relationship('Education', backref='education_type', lazy=True)

    def __repr__(self):
        return f'<EducationType {self.education_type}>'

class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill_type_id = db.Column(db.Integer, db.ForeignKey('skill_types.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    skill_value = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return f'<Skill {self.skill_value}>'

class SkillTypes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill_type = db.Column(db.String(50), nullable=False)
    skill = db.relationship('Skills', backref='skill_type', lazy=True)

    def __repr__(self):
        return f'<SkillType {self.skill_type}>'