from view.ViewLogin import *
from view.ViewFuncionario import *
from model.Contas import *


class Controller:
    def __init__(self):
        self.pageLogin = ViewLogin()
        self.pageFuncionario = ViewFuncionarioHome()
        self.user = Conta()

    def startApp(self):
        self.hideEverything()
        self.pageLogin.showLogin()
        window.mainloop()

    def hideEverything(self):
        self.pageLogin.hideLogin()
        self.pageFuncionario.hideFuncionario()

    def btnConfigs(self):
        #Login
        app.pageLogin.btnLogin.config(command=lambda: app.validateLogin())

        #Funcionario Home
        app.pageFuncionario.btnCarIn.config(command=lambda: app.validateLogin())
        app.pageFuncionario.btnCarOut.config(command=lambda: app.validateLogin())
        app.pageFuncionario.btnLogoutF.config(command=lambda: app.logoutF())
        app.pageFuncionario.btnRefreshData.config(command=lambda: app.loadFuncionarioHomeData())


    def validateLogin(self):
        if self.pageLogin.usernameEntry.get() == "" or self.pageLogin.passwordEntry.get() == "":
            self.pageLogin.loginError("IU")

        elif self.user.login(self.pageLogin.usernameEntry.get(), self.pageLogin.passwordEntry.get()):
            self.pageLogin.clearEntrys()
            self.hideEverything()
            if self.user.accountData.tipo == "F":
                self.loadFuncionarioHomeData()
                self.pageFuncionario.showFuncionario()
        elif self.user.login(self.pageLogin.usernameEntry.get(), self.pageLogin.passwordEntry.get()) is False:
            self.pageLogin.loginError("WU")
        else:
            self.pageLogin.loginError("")

    def logoutF(self):
        self.user.clearData()
        self.hideEverything()
        self.pageLogin.showLogin()

    def loadFuncionarioHomeData(self):
        self.user.refreshDataF()
        # Dados funcionário
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("welcome", text="Olá, {}!".format(self.user.employeeData.nome))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("nameF", text="{}".format(self.user.employeeData.nome))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("cpf", text="{}".format(self.user.employeeData.cpf))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("email", text="{}".format(self.user.employeeData.email))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("phone", text="{}".format(self.user.employeeData.telefone))

        # Dados estacionamento
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("cpcar", text="{}".format(self.user.parkingData.totalcarro))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("cpbike", text="{}".format(self.user.parkingData.totalmoto))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("cptruck", text="{}".format(self.user.parkingData.totalcaminhao))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("slotcar", text="{}".format(self.user.parkingData.vagascarro))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("slotbike", text="{}".format(self.user.parkingData.vagasmoto))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("slottruck", text="{}".format(self.user.parkingData.vagascaminhao))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("namepark", text="{}".format(self.user.parkingData.nome))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("price", text="R$ {}".format(self.user.parkingData.valor))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("alerttitle", text="{}".format(self.user.parkingData.avisotitulo))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("alertmsg", text="{}".format(self.user.parkingData.avisomsg))


if __name__ == '__main__':
    app = Controller()
    app.btnConfigs()
    app.startApp()
