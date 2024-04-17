from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.models.forms import RegisterForm, FilterForm
from app.models.tables import User
import pandas as pd
import numpy as np

@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def index():
    db.create_all()
    form = RegisterForm()
    if form.validate_on_submit():
        i = User(form.name.data,form.number_cpf.data,form.hostname.data,form.machine_model.data,form.mac_address.data,form.area.data,form.antivirus.data,form.atualizacao.data,form.email.data,form.name_job.data,0)
        print(i)
        db.create_all()
        db.session.add(i)
        db.session.commit()
        flash("Registro realizado com sucesso!")
        return redirect(url_for('confirm'))
    else:
        flash("Aconteceu um erro inesperado, por favor preencha novamente!")
    return render_template('index.html', form= form)

@app.route('/confirm')
def confirm():
    return render_template('confirm.html')

@app.route('/validation',methods=['GET', 'POST'])
def validation():
    try:
        form = User.query.all()
        result = [x.__dict__ for x in form]
        df = pd.DataFrame(result)
        df = df.drop(["_sa_instance_state","id"],axis=1)
        df = df.rename(columns={"name":"Nome","cpf":"CPF","machine_model":"Modelo","area":"Area","atualizacao":"Atualização","name_job":"Empresa","hostname":"Hostname","mac_address":"Mac Address","antivirus":"Antivírus","email":"Email","confirm":"Validação"})
    except:
        df = pd.DataFrame({"Nome":"","CPF": "","Modelo":"","Area": "","Atualização": "","Empresa": "","Hostname": "","Mac Address": "","Antivírus": "","Email": "","Validação": ""}, index=[0]) 
    df = df.reindex(sorted(df.columns),axis=1)
    table_teste = df.style.set_table_attributes('class="table_teste"')
    filter_form = FilterForm()
    if filter_form.is_submitted():
        try:
            name = filter_form.filter.data
            i = User.query.filter_by(name="%s" % (name)).first()
            user_name = i.name
            confirm = i.confirm
        except:
            user_name = " "
            confirm = False    
    else:
        user_name = " "
        confirm = False
    return render_template('validation.html', table=table_teste.to_html(), form = filter_form, user_name = user_name, confirm = confirm )


@app.route('/select/all')
def select():
    i = User.query.all()
    if i :
        print(i)
        return "Ok"
    else:
        print(i)
        return "Table empty"
    
#Route Update User
@app.route('/update/<users>')
def update(users):
    i = User.query.filter_by(name="%s" % (users)).first()
    i.confirm = True
    db.create_all()
    db.session.add(i)
    db.session.commit()
    return redirect(url_for('validation'))


#Route Delete User
@app.route('/delete/<users>')
def delete(users):
    try:
        i = User.query.filter_by(name="%s" % (users)).first()
        db.session.delete(i)
        db.session.commit()
        return "Usuário deletado"
    except:
        return "Usuário não existe"
