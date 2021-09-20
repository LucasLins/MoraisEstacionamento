from view.ViewLogin import *
from view.ViewFuncionario import *
from model.Contas import *


class Controller:
    def __init__(self):
        self.pageLogin = ViewLogin()
        self.pageFuncionario = ViewFuncionario()
        self.user = Conta()

    def startApp(self):
        self.pageLogin.showLogin()
        window.mainloop()

    def hideEverything(self):
        self.pageLogin.hideLogin()
        self.pageFuncionario.hideFuncionario()

    def btnConfigs(self):
        app.pageLogin.btnLogin.config(command=lambda: app.validateLogin())

    def validateLogin(self):
        if self.pageLogin.usernameEntry.get() == "" or self.pageLogin.passwordEntry.get() == "":
            self.pageLogin.loginError("IU")

        elif self.user.login(self.pageLogin.usernameEntry.get(), self.pageLogin.passwordEntry.get()):
            self.hideEverything()
            self.pageFuncionario.showFuncionario()

        else:
            self.pageLogin.loginError("WU")


if __name__ == '__main__':
    app = Controller()
    app.btnConfigs()
    app.startApp()
