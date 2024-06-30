from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email, ValidationError
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
import math
import numpy as np
import pandas as pd
import data_preprocessing
import model_training
import model_testing
import prediction
import os


# secret_key_file = 'secret_key.txt'


# if not os.path.exists(secret_key_file):
#     with open(secret_key_file, 'w') as f:
#         f.write(os.urandom(16).hex())


# with open(secret_key_file, 'r') as f:
#     secret_key = f.read()




app = Flask(__name__)
app.config['SECRET_KEY'] = "fraud_detection"
#csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
#app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
migrate = Migrate(app, db)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
    email = StringField(validators=[InputRequired(), Email(), Length(min=4, max=120)], render_kw={"placeholder": "Email"})
    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError('That username already exists. Please choose a different one.')

    def validate_email(self, email):
        existing_user_email = User.query.filter_by(email=email.data).first()
        if existing_user_email:
            raise ValidationError('That email already exists. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField('Login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/predict_transaction',methods=['POST'])
def predict_transaction():
    if request.method== 'POST':
        Time=float(request.form.get('Time'))
        V1=float(request.form.get('V1'))
        V2=float(request.form.get('V2'))
        V3=float(request.form.get('V3'))
        V4=float(request.form.get('V4'))
        V5=float(request.form.get('V5'))
        V6=float(request.form.get('V6'))
        V7=float(request.form.get('V7'))
        V8=float(request.form.get('V8'))
        V9=float(request.form.get('V9'))
        V10=float(request.form.get('V10'))
        V11=float(request.form.get('V11'))
        V12=float(request.form.get('V12'))
        V13=float(request.form.get('V13'))
        V14=float(request.form.get('V14'))
        V15=float(request.form.get('V15'))
        V19=float(request.form.get('V19'))
        V20=float(request.form.get('V20'))
        V21=float(request.form.get('V21'))
        V22=float(request.form.get('V22'))
        V23=float(request.form.get('V23'))
        V24=float(request.form.get('V24'))
        V25=float(request.form.get('V25'))
        V26=float(request.form.get('V26'))
        V27=float(request.form.get('V27'))
        V28=float(request.form.get('V28'))
        Amount=float(request.form.get('Amount'))
        geometry=int(request.form.get('geometry'))
        Amount_log=math.log(Amount)
        form_entries=[Time,V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,Amount_log,geometry]
        array_entries=np.array(form_entries)
        columns=['Time','V1','V2','V3','V4','V5','V6','V7','V8','V9','V10','V11','V12','V13','V14','V15','V19','V20','V21','V22','V23','V24','V25','V26','V27','V28','Amount_log','geometry']
        data=[form_entries]
        new_data=pd.DataFrame(data,columns=columns)
        data=data_preprocessing.load_data("data/finaldataset.csv")
        data_preprocessing.preprocess_data(data)
        x_train,x_test,y_train,y_test=data_preprocessing.split_data(data)
        x_train_scaled,x_test_scaled=data_preprocessing.scale_data(x_train,x_test)
        x_train_smt,y_train_smt=data_preprocessing.balance_data(x_train_scaled,y_train)
        final_model=model_training.train_model(x_train_smt,y_train_smt)
        y_pred_initial,time_taken_initial=model_testing.test_model(final_model,x_test_scaled)
        accuracy,roc_auc,f1=model_testing.evaluate_model(y_test,y_pred_initial)

        new_data_scaled=prediction.prepare_data(new_data,x_train)
        y_pred_new=prediction.make_prediction(final_model,new_data_scaled)
        #accu_score=prediction.display_prediction(y_pred_new,y_test)
        #accuracy_new,roc_auc_new,f1_new=prediction.display_prediction(y_test,y_pred_new)

        return render_template('prediction_result.html',prediction=y_pred_new,accuracy=accuracy,roc_auc=roc_auc,f1=f1)

@app.route('/prediction_result/<int:prediction>/<float:accuracy>/<float:roc_auc>/<float:f1>',methods=['GET'])
def prediction_result(prediction,accuracy,roc_auc,f1):
    return render_template(prediction_result.html,prediction=prediction,accuracy=accuracy,roc_auc=roc_auc,f1=f1)
        


if __name__ == '__main__':
    app.run(port=5000, debug=True)