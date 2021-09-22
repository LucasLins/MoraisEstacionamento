import dataset
from sqlalchemy import false, true
from stuf import stuf

db = dataset.connect('postgresql://postgres:2967@localhost:5432/MoraisEstacionamento', row_type=stuf)

tableContas = db['contas']
tableFuncionarios = db['funcionarios']
tableEstacionamentos = db['estacionamentos']
tableGestores = db['gestores']
tableRegistros = db['registros']


def dictConta(user, password, accType):
    return dict(usuario=user, senha=password, tipo=accType)


def dictFuncionario(accountid, parkingid, name, gender, cpf, phone):
    return dict(idconta=accountid, idestacionamento=parkingid, nome=name, sexo=gender, cpf=cpf, telefone=phone)


def dictEstacionamento(name, totalCar, totalMotorcycle, totalTruck, price, carSlots, motorcycleSlots, truckSlots):
    return dict(nome=name, totalcarro=totalCar, totalmoto=totalMotorcycle, totalcaminhao=totalTruck, valor=price,
                vagascarro=carSlots, vagasmoto=motorcycleSlots, vagascaminhao=truckSlots)


def dictRegistroEntrada(parkingId, employeeId, vehiclePlate, vehicleType, inDate):
    return dict(idestacionamento=parkingId, idfuncionario=employeeId, placa=vehiclePlate, tipo=vehicleType,
                dataentrada=inDate, pago=False)


def dictRegistroSaida(regId, outDate, payValue):
    return dict(id=regId, datasaida=outDate, valorpagar=payValue, pago=True)


