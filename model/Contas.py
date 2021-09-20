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
