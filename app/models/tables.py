from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    cpf = db.Column(db.Integer, unique=True)
    hostname = db.Column(db.String)
    machine_model = db.Column(db.String)
    mac_address = db.Column(db.Integer)
    area = db.Column(db.String)
    antivirus = db.Column(db.String)
    atualizacao = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    name_job = db.Column(db.String)
    confirm = db.Column(db.Boolean, default=False)

    def __init__(self,name, cpf,hostname,machine_model,mac_address, area, antivirus, atualizacao, email, name_job,confirm):
        self.name = name
        self.cpf = cpf
        self.hostname = hostname
        self.machine_model = machine_model
        self.mac_address = mac_address
        self.area = area
        self.antivirus = antivirus
        self.atualizacao = atualizacao
        self.email = email
        self.name_job = name_job
        self.confirm = confirm

    def __repr__(self):
        return f'{self.name},{self.cpf},{self.name_job}, {self.confirm}'