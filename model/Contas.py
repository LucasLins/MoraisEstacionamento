from model.dao import *


class Conta:
    def __init__(self):
        self.accountData = None
        self.employeeData = None
        self.parkingData = None

    def login(self, user, password):
        self.accountData = tableContas.find_one(usuario=user, senha=password)

        if self.accountData is not None:
            if self.accountData.tipo == "F":
                self.employeeData = tableFuncionarios.find_one(idconta=self.accountData.id)
                self.parkingData = tableEstacionamentos.find_one(id=self.employeeData.idestacionamento)
            else:
                self.employeeData = tableGestores.find_one(idconta=self.accountData.id)
            return True
        return False

    def clearData(self):
        self.accountData = None
        self.employeeData = None
        self.parkingData = None

    def refreshDataF(self):
        self.parkingData = tableEstacionamentos.find_one(id=self.employeeData.idestacionamento)

    def insertRecord(self, parkingId, employeeId, vehiclePlate, vehicleType, inDate):
        self.record = tableRegistros.find_one(pago=False, placa=vehiclePlate)
        if self.record is None:
            tableRegistros.insert(dictRegistroEntrada(parkingId, employeeId, vehiclePlate, vehicleType, inDate))
            self.slot = tableEstacionamentos.find_one(id=parkingId)
            if vehicleType == "Carro":
                tableEstacionamentos.update(dict(id=parkingId, vagascarro=(self.slot.vagascarro - 1)), ['id'])
            elif vehicleType == "Moto":
                tableEstacionamentos.update(dict(id=parkingId, vagasmoto=(self.slot.vagasmoto - 1)), ['id'])
            elif vehicleType == "Caminhão":
                tableEstacionamentos.update(dict(id=parkingId, vagascaminhao=(self.slot.vagascaminhao-1)), ['id'])

            return True
        return False
    
    def updateSlot(self, record):
        self.parkingId = record.idestacionamento
        self.slot = tableEstacionamentos.find_one(id=self.parkingId)
        if record.tipo == "Carro":
            tableEstacionamentos.update(dict(id=self.parkingId, vagascarro=(self.slot.vagascarro + 1)), ['id'])
        elif record.tipo == "Moto":
            tableEstacionamentos.update(dict(id=self.parkingId, vagasmoto=(self.slot.vagasmoto + 1)), ['id'])
        elif record.tipo == "Caminhão":
            tableEstacionamentos.update(dict(id=self.parkingId, vagascaminhao=(self.slot.vagascaminhao + 1)), ['id'])

    def updateRecord(self, record, outDate, payValue):
        tableRegistros.update(dictRegistroSaida(record.id, outDate, payValue), ['id'])

    def getRegisterData(self, plate):
        return tableRegistros.find_one(pago=False, placa=plate)

    def getRegisterEmployeeName(self, id):
        self.data = tableFuncionarios.find_one(id=id)
        return self.data.nome

    def getParkingPrice(self, id):
        self.data = tableEstacionamentos.find_one(id=id)
        return self.data.valor

    def getAvailableSpace(self, id, vType):
        self.data = tableEstacionamentos.find_one(id=id)
        if vType == "Carro" and self.data.vagascarro > 0:
            return True
        elif vType == "Moto" and self.data.vagasmoto > 0:
            return True
        elif vType == "Caminhão" and self.data.vagascaminhao > 0:
            return True
        return False

    def verifyUsername(self, user):
        self.data = tableContas.find_one(usuario=user)
        if self.data != None:
            return True
        else:
            return False

    def verifyCPF(self, cpf):
        self.data = tableFuncionarios.find_one(cpf=cpf)
        if self.data != None:
            return True
        else:
            return False

    def getParkingID(self, name):
        self.data = tableEstacionamentos.find_one(nome=name)
        return self.data.id

    def getAccountID(self, user):
        self.data = tableContas.find_one(usuario=user)
        return self.data.id

    def addEmployee(self, username, password, name, cpf, email, phone, gender, parking):
        tableContas.insert(dictConta(username, password, "F"))
        tableFuncionarios.insert(dictFuncionario(self.getAccountID(username), self.getParkingID(parking), name, gender, cpf, phone, email))
