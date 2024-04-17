from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, BooleanField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    number_cpf = IntegerField("number_cpf", validators=[DataRequired()])
    hostname = StringField("hostname", validators=[DataRequired()])
    machine_model = StringField("machine_model", validators=[DataRequired()])
    mac_address = StringField("mac_address", validators=[DataRequired()])
    area = StringField("area", validators=[DataRequired()])
    antivirus = StringField("antivirus", validators=[DataRequired()])
    atualizacao = StringField("atualizacao", validators=[DataRequired()])
    email= EmailField("email", validators=[DataRequired()])
    name_job = StringField("name_job", validators=[DataRequired()])

class FilterForm(FlaskForm):
    filter = StringField("filter")
