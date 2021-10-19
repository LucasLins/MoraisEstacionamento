import dataset
from sqlalchemy import false, true, create_engine
from stuf import stuf
import pandas as pd
import pygsheets

db = dataset.connect('postgresql://postgres:2967@localhost:5432/MoraisEstacionamento', row_type=stuf)

tableContas = db['contas']
tableFuncionarios = db['funcionarios']
tableEstacionamentos = db['estacionamentos']
tableGestores = db['gestores']
tableRegistros = db['registros']


def dictConta(user, password, accType):
    return dict(usuario=user, senha=password, tipo=accType)


def dictFuncionario(accountid, parkingid, name, gender, cpf, phone, email):
    return dict(idconta=accountid, idestacionamento=parkingid, nome=name, sexo=gender, cpf=cpf, telefone=phone, email=email)


def dictEstacionamento(name, totalCar, totalMotorcycle, totalTruck, price, carSlots, motorcycleSlots, truckSlots):
    return dict(nome=name, totalcarro=totalCar, totalmoto=totalMotorcycle, totalcaminhao=totalTruck, valor=price,
                vagascarro=carSlots, vagasmoto=motorcycleSlots, vagascaminhao=truckSlots)


def dictUpdateEstacionamento(id, name, totalCar, totalMotorcycle, totalTruck, price, carSlots, motorcycleSlots, truckSlots):
    return dict(id=id, nome=name, totalcarro=totalCar, totalmoto=totalMotorcycle, totalcaminhao=totalTruck, valor=price,
                vagascarro=carSlots, vagasmoto=motorcycleSlots, vagascaminhao=truckSlots)

def dictSendNotice(id, title, text):
    return dict(id=id, avisotitulo=title, avisomsg=text)


def dictRegistroEntrada(parkingId, employeeId, vehiclePlate, vehicleType, inDate):
    return dict(idestacionamento=parkingId, idfuncionario=employeeId, placa=vehiclePlate, tipo=vehicleType,
                dataentrada=inDate, pago=False)


def dictRegistroSaida(regId, outDate, payValue):
    return dict(id=regId, datasaida=outDate, valorpagar=payValue, pago=True)

def gerarPlanilha(path):
    database = create_engine('postgresql://postgres:2967@localhost:5432/MoraisEstacionamento')

    with database.connect() as conn, conn.begin():
        dataF = pd.read_sql_query('SELECT * FROM funcionarios', database)
        dataE = pd.read_sql_query('SELECT * FROM estacionamentos', database)
        dataR = pd.read_sql_query('SELECT * FROM registros', database)

    gc = pygsheets.authorize(service_file=path)
    sh = gc.open_by_key('1m1kkVpsRF4z3jxf5eXWXAkbunY7C4nPt_BJbyrVXtPw')

    try:
        sh.add_worksheet("Funcionários")
        sh.add_worksheet("Estacionamentos")
        sh.add_worksheet("Registros")
        sh.del_worksheet(sh.worksheet_by_title("Sheet1"))
    except:
        pass

    wF = sh.worksheet_by_title("Funcionários")
    wF.clear('A1', None, '*')
    wF.set_dataframe(dataF, (1, 1), encoding='utf-8', fit=True)
    wF.frozen_rows = 1

    wE = sh.worksheet_by_title("Estacionamentos")
    wE.clear('A1', None, '*')
    wE.set_dataframe(dataE, (1, 1), encoding='utf-8', fit=True)
    wE.frozen_rows = 1

    wR = sh.worksheet_by_title("Registros")
    wR.clear('A1', None, '*')
    wR.set_dataframe(dataR, (1, 1), encoding='utf-8', fit=True)
    wR.frozen_rows = 1



