from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True,index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    secure_password = db.Column(db.String(255), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()

    def __str__(self):
        return f'User: {self.username} Email: {self.email}'

    def __repr__(self):
        return f'User: {self.username} Email: {self.email}'

    @property
    def password(self):
        raise AttributeError('cannot read password')

    @password.setter
    def password(self, password):
        pass_hash = generate_password_hash(password)
        self.secure_password = pass_hash

    def check_password(self, password):
        return check_password_hash(self.secure_password, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
