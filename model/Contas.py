from model.dao import *


class Conta:
    def __init__(self):
        self.accountData = None
        self.typeData = None

    def login(self, user, password):
        self.accountData = tableContas.find_one(usuario=user, senha=password)

        if self.accountData is not None:
            if self.accountData.tipo == "F":
                self.typeData = tableFuncionarios.find_one(idconta=self.accountData.id)
            else:
                self.typeData = tableGestores.find_one(idconta=self.accountData.id)
            return True
        return False
