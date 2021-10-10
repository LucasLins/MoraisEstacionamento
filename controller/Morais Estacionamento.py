from view.ViewLogin import *
from view.ViewGestor import *
from view.ViewFuncionario import *
from model.Contas import *
from datetime import datetime


class Controller:
    def __init__(self):
        self.pageLogin = ViewLogin()
        self.pageFuncionario = FuncionarioHome()
        self.pageFuncionarioCarIN = FuncionarioCarIN()
        self.pageFuncionarioCarOUT = FuncionarioCarOUT()
        self.pageGestorHome = GestorHome()
        self.pageGestorAddF = GestorAddF()
        self.pageGestorAddE = GestorAddE()
        self.user = Conta()

    def startApp(self):
        self.hideEverything()
        self.pageLogin.showLogin()
        window.mainloop()

    def hideEverything(self):
        self.pageLogin.hideLogin()
        self.pageFuncionario.hideFuncionario()
        self.pageFuncionarioCarIN.hideFuncionarioCarIN()
        self.pageFuncionarioCarOUT.hideFuncionarioCarOUT()
        self.pageGestorHome.hideGestorHome()
        self.pageGestorAddF.hideGestorAddF()
        self.pageGestorAddE.hideGestorAddE()

    def btnConfigs(self):
        # Login
        app.pageLogin.btnLogin.config(command=lambda: app.validateLogin())

        # Funcionario Home
        app.pageFuncionario.btnCarIn.config(command=lambda: app.pageFuncionarioCarIN.showFuncionarioCarIN())
        app.pageFuncionario.btnCarOut.config(command=lambda: app.pageFuncionarioCarOUT.showFuncionarioCarOUT())
        app.pageFuncionario.btnLogoutF.config(command=lambda: app.logout())
        app.pageFuncionario.btnRefreshData.config(command=lambda: app.loadFuncionarioHomeData())

        # Funcionario Adicionar Registro
        app.pageFuncionarioCarIN.btnReturnIN.config(command=lambda: app.returnFHome())
        app.pageFuncionarioCarIN.btnAddCar.config(command=lambda: app.validateRecordInsert())

        # Funcionario Atualizar Registro
        app.pageFuncionarioCarOUT.btnReturnOut.config(command=lambda: app.returnFHome())
        app.pageFuncionarioCarOUT.btnClearInfo.config(command=lambda: app.pageFuncionarioCarOUT.clearEntrys())
        app.pageFuncionarioCarOUT.btnFindPlateOut.config(command=lambda: app.validateSearchPlate())
        app.pageFuncionarioCarOUT.btnConfirmExit.config(command=lambda: app.validateCarOUT())

        # Gestor Home
        app.pageGestorHome.btnLogoutG.config(command=lambda: app.logout())
        app.pageGestorHome.btnAddEmployee.config(command=lambda: app.loadGestorAddF())
        app.pageGestorHome.btnAddParking.config(command=lambda: app.pageGestorAddE.showGestorAddE())
        app.pageGestorHome.btnManageParking.config(command=lambda: app.logout())
        app.pageGestorHome.btnReports.config(command=lambda: app.logout())

        # Gestor Add Funcionário
        app.pageGestorAddF.btnReturn.config(command=lambda: app.returnGHome())
        app.pageGestorAddF.btnAddFuncionario.config(command=lambda: app.addFuncionario())

        # Gestor Add Estacionamento
        app.pageGestorAddE.btnReturnAddE.config(command=lambda: app.returnGHome())
        app.pageGestorAddE.btnAddE.config(command=lambda: app.addParking())


    def validateLogin(self):
        if self.pageLogin.usernameEntry.get() == "" or self.pageLogin.passwordEntry.get() == "":
            self.pageLogin.loginError("IU")

        elif self.user.login(self.pageLogin.usernameEntry.get(), self.pageLogin.passwordEntry.get()):
            self.pageLogin.clearEntrys()
            self.hideEverything()
            if self.user.accountData.tipo == "F":
                self.loadFuncionarioHomeData()
                self.pageFuncionario.showFuncionario()
            elif self.user.accountData.tipo == "G":
                self.loadGestorHomeData()
                self.pageGestorHome.showGestorHome()
        elif self.user.login(self.pageLogin.usernameEntry.get(), self.pageLogin.passwordEntry.get()) is False:
            self.pageLogin.loginError("WU")
        else:
            self.pageLogin.loginError("")

    def logout(self):
        self.user.clearData()
        self.hideEverything()
        self.pageLogin.showLogin()

    def loadFuncionarioHomeData(self):
        self.user.refreshDataF()
        # Dados funcionário
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("welcome",
                                                                 text="Olá, {}!".format(self.user.employeeData.nome))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("nameF", text="{}".format(self.user.employeeData.nome))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("cpf", text="{}".format(self.user.employeeData.cpf))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("email",
                                                                 text="{}".format(self.user.employeeData.email))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("phone",
                                                                 text="{}".format(self.user.employeeData.telefone))

        # Dados estacionamento
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("cpcar",
                                                                 text="{}".format(self.user.parkingData.totalcarro))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("cpbike",
                                                                 text="{}".format(self.user.parkingData.totalmoto))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("cptruck",
                                                                 text="{}".format(self.user.parkingData.totalcaminhao))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("slotcar",
                                                                 text="{}".format(self.user.parkingData.vagascarro))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("slotbike",
                                                                 text="{}".format(self.user.parkingData.vagasmoto))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("slottruck",
                                                                 text="{}".format(self.user.parkingData.vagascaminhao))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("namepark",
                                                                 text="{}".format(self.user.parkingData.nome))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("price",
                                                                 text="R$ {}".format(self.user.parkingData.valor))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("alerttitle",
                                                                 text="{}".format(self.user.parkingData.avisotitulo))
        self.pageFuncionario.alertBox.configure(state="normal")
        self.pageFuncionario.alertBox.delete(1.0, 'end')
        self.pageFuncionario.alertBox.insert(END, self.user.parkingData.avisomsg)
        self.pageFuncionario.alertBox.configure(state="disabled")

    def loadFuncionarioINData(self, plate):
        self.vehicleInfo = self.user.getRegisterData(plate)
        self.pageFuncionarioCarIN.canvasFuncionarioCarIN.itemconfigure("carplate",
                                                                       text="{}".format(self.vehicleInfo.placa),
                                                                       state="normal")
        self.pageFuncionarioCarIN.canvasFuncionarioCarIN.itemconfigure("datetime",
                                                                       text="{:02d}:{:02d}:{:02d} - {:02d}/{:02d}/{}"
                                                                       .format(self.vehicleInfo.dataentrada.hour,
                                                                               self.vehicleInfo.dataentrada.minute,
                                                                               self.vehicleInfo.dataentrada.second,
                                                                               self.vehicleInfo.dataentrada.day,
                                                                               self.vehicleInfo.dataentrada.month,
                                                                               self.vehicleInfo.dataentrada.year),
                                                                       state="normal")
        self.pageFuncionarioCarIN.canvasFuncionarioCarIN.itemconfigure("cartype",
                                                                       text="{}".format(self.vehicleInfo.tipo),
                                                                       state="normal")
        self.pageFuncionarioCarIN.canvasFuncionarioCarIN.itemconfigure("employee", text="{}".format(
            (self.user.getRegisterEmployeeName(self.vehicleInfo.idfuncionario))), state="normal")

    def returnFHome(self):
        self.hideEverything()
        self.loadFuncionarioHomeData()
        self.pageFuncionario.showFuncionario()
        self.pageFuncionarioCarIN.clearEntrys()
        self.pageFuncionarioCarOUT.clearEntrys()

    def returnGHome(self):
        self.hideEverything()
        self.loadGestorHomeData()
        self.pageGestorHome.showGestorHome()
        self.pageGestorAddF.clearEntrys()
        self.pageGestorAddE.clearEntrys()


    def validateRecordInsert(self):
        self.dt = datetime.now(tz=None)
        if app.pageFuncionarioCarIN.entryPlate.get() == "" or app.pageFuncionarioCarIN.comboType.current() == -1:
            self.pageFuncionarioCarIN.showError("Placa e/ou tipo de veículo inválido(s)!")

        elif len(app.pageFuncionarioCarIN.entryPlate.get()) != 7:
            self.pageFuncionarioCarIN.showError("A placa do veículo deve possuir 7 carácteres!")

        elif self.user.getAvailableSpace(self.user.parkingData.id, self.pageFuncionarioCarIN.comboType.get()) is True:
            if self.user.insertRecord(self.user.parkingData.id, self.user.employeeData.id,
                                      self.pageFuncionarioCarIN.entryPlate.get(),
                                      self.pageFuncionarioCarIN.comboType.get(), self.dt) is True:
                self.pageFuncionarioCarIN.canvasFuncionarioCarIN.itemconfigure("sucessadd", state="normal")
                self.loadFuncionarioINData(self.pageFuncionarioCarIN.entryPlate.get())
            else:
                self.pageFuncionarioCarIN.showError("Este veículo já está dentro do estacionamento!")
        else:
            self.pageFuncionarioCarIN.showError("As vagas para este tipo de veículo esgotaram!")

    def validateSearchPlate(self):
        self.vehicleInfo = self.user.getRegisterData(app.pageFuncionarioCarOUT.entryPlateOut.get())
        self.pageFuncionarioCarOUT.canvasFuncionarioCarOUT.itemconfigure("errormsg", text="")
        self.pageFuncionarioCarOUT.canvasFuncionarioCarOUT.itemconfigure("errorbg", state="hidden")
        if self.pageFuncionarioCarOUT.entryPlateOut.get() == "" or len(
                self.pageFuncionarioCarOUT.entryPlateOut.get()) != 7:
            self.pageFuncionarioCarOUT.showError("Placa do veículo inválida!")

        elif self.vehicleInfo is None:
            self.pageFuncionarioCarOUT.showError("Veículo não encontrado!")

        else:
            self.loadFuncionarioOUTData(self.vehicleInfo)
            self.pageFuncionarioCarOUT.entryPlateOut.config(state="disabled")
            self.pageFuncionarioCarOUT.btnFindPlateOut.config(state="disabled")

    def loadFuncionarioOUTData(self, vehicleInfo):
        self.pageFuncionarioCarOUT.canvasFuncionarioCarOUT.itemconfigure("carplate",
                                                                         text="{}".format(vehicleInfo.placa),
                                                                         state="normal")
        self.pageFuncionarioCarOUT.canvasFuncionarioCarOUT.itemconfigure("datetime",
                                                                         text="{:02d}:{:02d}:{:02d} - {:02d}/{:02d}/{}"
                                                                         .format(vehicleInfo.dataentrada.hour,
                                                                                 vehicleInfo.dataentrada.minute,
                                                                                 vehicleInfo.dataentrada.second,
                                                                                 vehicleInfo.dataentrada.day,
                                                                                 vehicleInfo.dataentrada.month,
                                                                                 vehicleInfo.dataentrada.year),
                                                                         state="normal")
        self.pageFuncionarioCarOUT.canvasFuncionarioCarOUT.itemconfigure("cartype", text="{}".format(vehicleInfo.tipo),
                                                                         state="normal")
        self.pageFuncionarioCarOUT.canvasFuncionarioCarOUT.itemconfigure("employee", text="{}".format(
            (self.user.getRegisterEmployeeName(self.vehicleInfo.idfuncionario))), state="normal")
        self.pageFuncionarioCarOUT.btnConfirmExit.config(state="normal")
        self.pageFuncionarioCarOUT.btnClearInfo.config(state="normal")

    def validateCarOUT(self):
        self.vehicleInfo = self.user.getRegisterData(app.pageFuncionarioCarOUT.entryPlateOut.get())
        self.dt = datetime.now(tz=None)
        self.elapsedtime = self.dt - self.vehicleInfo.dataentrada
        self.price = (self.elapsedtime.total_seconds() / 3600) * self.user.getParkingPrice(
            self.vehicleInfo.idestacionamento)
        self.user.updateRecord(self.vehicleInfo, self.dt, self.price)
        self.user.updateSlot(self.vehicleInfo)
        self.pageFuncionarioCarOUT.canvasFuncionarioCarOUT.itemconfigure("datetimeend",
                                                                         text="{:02d}:{:02d}:{:02d} - {:02d}/{:02d}/{}"
                                                                         .format(self.dt.hour,
                                                                                 self.dt.minute,
                                                                                 self.dt.second,
                                                                                 self.dt.day,
                                                                                 self.dt.month,
                                                                                 self.dt.year),
                                                                         state="normal")
        self.pageFuncionarioCarOUT.canvasFuncionarioCarOUT.itemconfigure("elapsedtime", state="normal",
                                                                         text="{:.2f} hora(s)".format(
                                                                             (self.elapsedtime.total_seconds() / 3600)))
        self.pageFuncionarioCarOUT.canvasFuncionarioCarOUT.itemconfigure("price", state="normal",
                                                                         text="R$ {:.2f}".format(self.price))
        self.pageFuncionarioCarOUT.canvasFuncionarioCarOUT.itemconfigure("sucessmsg", state="normal")
        self.pageFuncionarioCarOUT.btnConfirmExit.config(state="disabled")

    def loadGestorHomeData(self):
        self.pageGestorHome.canvasGestorHome.itemconfigure("welcome",
                                                           text="Olá, {}!".format(self.user.employeeData.nome))
        self.pageGestorHome.canvasGestorHome.itemconfigure("nameG", text="{}".format(self.user.employeeData.nome))
        self.pageGestorHome.canvasGestorHome.itemconfigure("cpf", text="{}".format(self.user.employeeData.cpf))
        self.pageGestorHome.canvasGestorHome.itemconfigure("email",
                                                           text="{}".format(self.user.employeeData.email))
        self.pageGestorHome.canvasGestorHome.itemconfigure("phone",
                                                           text="{}".format(self.user.employeeData.telefone))

    def loadGestorAddF(self):
        for index, item in enumerate(tableEstacionamentos):
            self.pageGestorAddF.listaEstacionamento.insert(index, item.nome)
        self.pageGestorAddF.showGestorAddF()

    def addFuncionario(self):
        self.pageGestorAddF.canvasGestorAddEmp.itemconfigure("successmsg", state="hidden")
        if self.pageGestorAddF.userEntry.get() == "" or self.pageGestorAddF.passEntry.get() == "" \
                or self.pageGestorAddF.entryName.get() == "" or self.pageGestorAddF.entryCPF.get() == "___.___.___-__" \
                or self.pageGestorAddF.entryEmail.get() == "" or self.pageGestorAddF.entryPhone.get() == "(__)9____-____" \
                or self.pageGestorAddF.comboGender.get() == "" or self.pageGestorAddF.entryCPF.get()[-1] == "_" \
                or self.pageGestorAddF.entryPhone.get()[-1] == "_":
            self.pageGestorAddF.showError("Todos os campos devem ser preenchidos.")

        elif self.pageGestorAddF.listaEstacionamento.get(ANCHOR) == "":
            self.pageGestorAddF.showError("Selecione o estacionamento que o funcionário vai trabalhar!")

        elif self.user.verifyUsername(self.pageGestorAddF.userEntry.get()) is True:
            self.pageGestorAddF.showError("Já existe uma conta com este usuário!")

        elif self.user.verifyCPF(self.pageGestorAddF.entryCPF.get()) is True:
            self.pageGestorAddF.showError("Já existe um funcionário com este CPF!")

        else:
            self.user.addEmployee(self.pageGestorAddF.userEntry.get(), self.pageGestorAddF.passEntry.get(),
                                  self.pageGestorAddF.entryName.get(),
                                  self.pageGestorAddF.entryCPF.get(), self.pageGestorAddF.entryEmail.get(),
                                  self.pageGestorAddF.entryPhone.get(),
                                  self.pageGestorAddF.comboGender.get(),
                                  self.pageGestorAddF.listaEstacionamento.get(ANCHOR))
            self.pageGestorAddF.clearEntrys()
            self.pageGestorAddF.canvasGestorAddEmp.itemconfigure("successmsg", state="normal")

    def addParking(self):
        self.pageGestorAddE.canvasGestorAddE.itemconfigure("successmsg", state="hidden")
        if self.pageGestorAddE.entryPName.get() == "" or self.pageGestorAddE.entryCPCar.get() == ""\
                or self.pageGestorAddE.entryCPBike.get() == "" or self.pageGestorAddE.entryCPTruck.get() == ""\
                or self.pageGestorAddE.entryTax.get() == "":
            self.pageGestorAddE.showError("Preencha todos os campos!")
        elif self.user.verifyParking(self.pageGestorAddE.entryPName.get()) is True:
            self.pageGestorAddE.showError("Já existe um estacionamento cadastrado com este nome!")
        else:
            self.user.addParking(self.pageGestorAddE.entryPName.get(), self.pageGestorAddE.entryCPCar.get(),
                                 self.pageGestorAddE.entryCPBike.get(), self.pageGestorAddE.entryCPTruck.get(),
                                 self.pageGestorAddE.entryTax.get())
            self.pageGestorAddE.clearEntrys()
            self.pageGestorAddE.canvasGestorAddE.itemconfigure("successmsg", state="normal")


if __name__ == '__main__':
    app = Controller()
    app.btnConfigs()
    app.startApp()
