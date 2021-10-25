from view.ViewLogin import *
from view.ViewGestor import *
from view.ViewFuncionario import *
from model.Backend import *
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
        self.pageGestorMngP = GestorManageP()
        self.pageGestorRelatorios = GestorRelatorios()
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
        self.pageGestorMngP.hideGestorMngP()
        self.pageGestorRelatorios.hideGestorRelatorios()

    def btnConfigs(self):
        # Login
        self.pageLogin.btnLogin.config(command=lambda: self.validateLogin())

        # Funcionario Home
        self.pageFuncionario.btnCarIn.config(command=lambda: self.pageFuncionarioCarIN.showFuncionarioCarIN())
        self.pageFuncionario.btnCarOut.config(command=lambda: self.pageFuncionarioCarOUT.showFuncionarioCarOUT())
        self.pageFuncionario.btnLogoutF.config(command=lambda: self.logout())
        self.pageFuncionario.btnRefreshData.config(command=lambda: self.loadFuncionarioHomeData())

        # Funcionario Adicionar Registro
        self.pageFuncionarioCarIN.btnReturnIN.config(command=lambda: self.returnFHome())
        self.pageFuncionarioCarIN.btnAddCar.config(command=lambda: self.validateRecordInsert())

        # Funcionario Atualizar Registro
        self.pageFuncionarioCarOUT.btnReturnOut.config(command=lambda: self.returnFHome())
        self.pageFuncionarioCarOUT.btnClearInfo.config(command=lambda: self.pageFuncionarioCarOUT.clearEntrys())
        self.pageFuncionarioCarOUT.btnFindPlateOut.config(command=lambda: self.validateSearchPlate())
        self.pageFuncionarioCarOUT.btnConfirmExit.config(command=lambda: self.validateCarOUT())

        # Gestor Home
        self.pageGestorHome.btnLogoutG.config(command=lambda: self.logout())
        self.pageGestorHome.btnAddEmployee.config(command=lambda: self.loadGestorAddF())
        self.pageGestorHome.btnAddParking.config(command=lambda: self.pageGestorAddE.showGestorAddE())
        self.pageGestorHome.btnManageParking.config(command=lambda: self.loadGestorMngP())
        self.pageGestorHome.btnReports.config(command=lambda: self.loadGestorRelatorios())

        # Gestor Add Funcionário
        self.pageGestorAddF.btnReturn.config(command=lambda: self.returnGHome())
        self.pageGestorAddF.btnAddFuncionario.config(command=lambda: self.addFuncionario())

        # Gestor Add Estacionamento
        self.pageGestorAddE.btnReturnAddE.config(command=lambda: self.returnGHome())
        self.pageGestorAddE.btnAddE.config(command=lambda: self.addParking())

        # Gestor Gerenciar Estacionamento
        self.pageGestorMngP.btnReturnMngE.config(command=lambda: self.returnGHome())
        self.pageGestorMngP.btnLoadParking.config(command=lambda: self.loadParkingData())
        self.pageGestorMngP.btnClearInfo.config(command=lambda: self.loadGestorMngP())
        self.pageGestorMngP.btnUpdateParking.config(command=lambda: self.btnUpdateParking())
        self.pageGestorMngP.btnAddNotice.config(command=lambda: self.btnSendNotice())

        # Gestor Relatórios
        self.pageGestorRelatorios.btnReturnRelatorio.config(command=lambda: self.returnGHome())
        self.pageGestorRelatorios.btnLoadRelatorio.config(command=lambda: self.loadMeterData())
        self.pageGestorRelatorios.btnClearRelatorio.config(command=lambda: self.btnClearMeters())
        self.pageGestorRelatorios.btnRelatorioFull.config(command=lambda: self.btnFullReport())

    def validateLogin(self):
        if self.pageLogin.usernameEntry.get() == "" or self.pageLogin.passwordEntry.get() == "":
            self.pageLogin.loginError("IU")

        elif self.user.login(self.pageLogin.usernameEntry.get(), self.pageLogin.passwordEntry.get()):
            self.pageLogin.clearEntrys()
            self.hideEverything()
            if self.user.accountData["tipo"] == "F":
                self.loadFuncionarioHomeData()
                self.pageFuncionario.showFuncionario()
            elif self.user.accountData["tipo"] == "G":
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
                                                                 text="Olá, {}!".format(self.user.employeeData["nome"]))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("nameF", text="{}".format(self.user.employeeData["nome"]))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("cpf", text="{}".format(self.user.employeeData["cpf"]))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("email",
                                                                 text="{}".format(self.user.employeeData["email"]))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("phone",
                                                                 text="{}".format(self.user.employeeData["telefone"]))

        # Dados estacionamento
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("cpcar",
                                                                 text="{}".format(self.user.parkingData["totalcarro"]))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("cpbike",
                                                                 text="{}".format(self.user.parkingData["totalmoto"]))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("cptruck",
                                                                 text="{}".format(self.user.parkingData["totalcaminhao"]))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("slotcar",
                                                                 text="{}".format(self.user.parkingData["vagascarro"]))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("slotbike",
                                                                 text="{}".format(self.user.parkingData["vagasmoto"]))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("slottruck",
                                                                 text="{}".format(self.user.parkingData["vagascaminhao"]))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("namepark",
                                                                 text="{}".format(self.user.parkingData["nome"]))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("price",
                                                                 text="R$ {}".format(self.user.parkingData["valor"]))
        self.pageFuncionario.canvasFuncionarioHome.itemconfigure("alerttitle",
                                                                 text="{}".format(self.user.parkingData["avisotitulo"]))
        self.pageFuncionario.alertBox.configure(state="normal")
        self.pageFuncionario.alertBox.delete(1.0, 'end')
        self.pageFuncionario.alertBox.insert(END, self.user.parkingData["avisomsg"])
        self.pageFuncionario.alertBox.configure(state="disabled")

    def loadFuncionarioINData(self, plate):
        self.vehicleInfo = self.user.getRegisterData(plate)
        self.pageFuncionarioCarIN.canvasFuncionarioCarIN.itemconfigure("carplate",
                                                                       text="{}".format(self.vehicleInfo["placa"]),
                                                                       state="normal")
        self.pageFuncionarioCarIN.canvasFuncionarioCarIN.itemconfigure("datetime",
                                                                       text="{:02d}:{:02d}:{:02d} - {:02d}/{:02d}/{}"
                                                                       .format(self.vehicleInfo["dataentrada"].hour,
                                                                               self.vehicleInfo["dataentrada"].minute,
                                                                               self.vehicleInfo["dataentrada"].second,
                                                                               self.vehicleInfo["dataentrada"].day,
                                                                               self.vehicleInfo["dataentrada"].month,
                                                                               self.vehicleInfo["dataentrada"].year),
                                                                       state="normal")
        self.pageFuncionarioCarIN.canvasFuncionarioCarIN.itemconfigure("cartype",
                                                                       text="{}".format(self.vehicleInfo["tipo"]),
                                                                       state="normal")
        self.pageFuncionarioCarIN.canvasFuncionarioCarIN.itemconfigure("employee", text="{}".format(
            (self.user.getRegisterEmployeeName(self.vehicleInfo["idfuncionario"]))), state="normal")

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
        self.pageGestorMngP.clearEntrys()

    def validateRecordInsert(self):
        self.dt = datetime.now(tz=None)
        if self.pageFuncionarioCarIN.entryPlate.get() == "" or self.pageFuncionarioCarIN.comboType.current() == -1:
            self.pageFuncionarioCarIN.showError("Placa e/ou tipo de veículo inválido(s)!")

        elif len(self.pageFuncionarioCarIN.entryPlate.get()) != 7:
            self.pageFuncionarioCarIN.showError("A placa do veículo deve possuir 7 carácteres!")

        elif self.user.getAvailableSpace(self.user.parkingData["id"], self.pageFuncionarioCarIN.comboType.get()) is True:
            if self.user.insertRecord(self.user.parkingData["id"], self.user.employeeData["id"],
                                      self.pageFuncionarioCarIN.entryPlate.get(),
                                      self.pageFuncionarioCarIN.comboType.get(), self.dt) is True:
                self.pageFuncionarioCarIN.canvasFuncionarioCarIN.itemconfigure("sucessadd", state="normal")
                self.loadFuncionarioINData(self.pageFuncionarioCarIN.entryPlate.get())
            else:
                self.pageFuncionarioCarIN.showError("Este veículo já está dentro do estacionamento!")
        else:
            self.pageFuncionarioCarIN.showError("As vagas para este tipo de veículo esgotaram!")

    def validateSearchPlate(self):
        self.vehicleInfo = self.user.getRegisterData(self.pageFuncionarioCarOUT.entryPlateOut.get())
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
                                                                         text="{}".format(vehicleInfo["placa"]),
                                                                         state="normal")
        self.pageFuncionarioCarOUT.canvasFuncionarioCarOUT.itemconfigure("datetime",
                                                                         text="{:02d}:{:02d}:{:02d} - {:02d}/{:02d}/{}"
                                                                         .format(vehicleInfo["dataentrada"].hour,
                                                                                 vehicleInfo["dataentrada"].minute,
                                                                                 vehicleInfo["dataentrada"].second,
                                                                                 vehicleInfo["dataentrada"].day,
                                                                                 vehicleInfo["dataentrada"].month,
                                                                                 vehicleInfo["dataentrada"].year),
                                                                         state="normal")
        self.pageFuncionarioCarOUT.canvasFuncionarioCarOUT.itemconfigure("cartype", text="{}".format(vehicleInfo["tipo"]),
                                                                         state="normal")
        self.pageFuncionarioCarOUT.canvasFuncionarioCarOUT.itemconfigure("employee", text="{}".format(
            (self.user.getRegisterEmployeeName(self.vehicleInfo["idfuncionario"]))), state="normal")
        self.pageFuncionarioCarOUT.btnConfirmExit.config(state="normal")
        self.pageFuncionarioCarOUT.btnClearInfo.config(state="normal")

    def validateCarOUT(self):
        self.vehicleInfo = self.user.getRegisterData(self.pageFuncionarioCarOUT.entryPlateOut.get())
        self.dt = datetime.now(tz=None)
        self.elapsedtime = self.dt - self.vehicleInfo["dataentrada"]
        self.price = (self.elapsedtime.total_seconds() / 3600) * self.user.getParkingPrice(
            self.vehicleInfo["idestacionamento"])
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
                                                           text="Olá, {}!".format(self.user.employeeData["nome"]))
        self.pageGestorHome.canvasGestorHome.itemconfigure("nameG", text="{}".format(self.user.employeeData["nome"]))
        self.pageGestorHome.canvasGestorHome.itemconfigure("cpf", text="{}".format(self.user.employeeData["cpf"]))
        self.pageGestorHome.canvasGestorHome.itemconfigure("email",
                                                           text="{}".format(self.user.employeeData["email"]))
        self.pageGestorHome.canvasGestorHome.itemconfigure("phone",
                                                           text="{}".format(self.user.employeeData["telefone"]))

    def loadGestorAddF(self):
        for index, item in enumerate(tableEstacionamentos):
            self.pageGestorAddF.listaEstacionamento.insert(index, item["nome"])
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

    def loadGestorMngP(self):
        self.pageGestorMngP.clearEntrys()
        for index, item in enumerate(tableEstacionamentos):
            self.pageGestorMngP.listaEstacionamento.insert(index, item["nome"])

        self.pageGestorMngP.alertTitle.insert(0, "Título")
        self.pageGestorMngP.alertmsgArea.insert(END, "Mensagem")
        self.pageGestorMngP.disableEntrys()
        self.pageGestorMngP.showGestorMngP()

    def loadParkingData(self):
        if self.pageGestorMngP.listaEstacionamento.get(ANCHOR) != "":
            self.pageGestorMngP.enableEntrys()
            self.pageGestorMngP.alertTitle.delete(0, END)
            self.pageGestorMngP.alertmsgArea.delete(1.0, END)
            self.data = self.user.getParkingData(self.pageGestorMngP.listaEstacionamento.get(ANCHOR))
            self.pageGestorMngP.entryPName.insert(0, self.data["nome"])
            self.pageGestorMngP.entryCPCar.insert(0, self.data["totalcarro"])
            self.pageGestorMngP.entryCPBike.insert(0, self.data["totalmoto"])
            self.pageGestorMngP.entryCPTruck.insert(0, self.data["totalcaminhao"])
            self.pageGestorMngP.entryTax.insert(0, self.data["valor"])
            self.pageGestorMngP.alertTitle.insert(0, self.data["avisotitulo"])
            self.pageGestorMngP.alertmsgArea.insert(1.0, self.data["avisomsg"])

    def btnUpdateParking(self):
        self.pageGestorMngP.canvasManageP.itemconfigure("successmsg", state="hidden")
        self.pageGestorMngP.canvasManageP.itemconfigure("successbg", state="hidden")

        self.data = self.user.getParkingData(self.pageGestorMngP.listaEstacionamento.get(ANCHOR))
        self.parkedCars = self.data["totalcarro"] - self.data["vagascarro"]
        self.parkedBikes = self.data["totalmoto"] - self.data["vagasmoto"]
        self.parkedTrucks = self.data["totalcaminhao"] - self.data["vagascaminhao"]
        self.newCarSlots = (int(self.pageGestorMngP.entryCPCar.get()) - self.data["totalcarro"]) + self.data["vagascarro"]
        self.newBikeSlots = (int(self.pageGestorMngP.entryCPBike.get()) - self.data["totalmoto"]) + self.data["vagasmoto"]
        self.newTruckSlots = (int(self.pageGestorMngP.entryCPTruck.get()) - self.data["totalcaminhao"]) + self.data["vagasmoto"]

        if self.pageGestorMngP.entryPName.get() == "" or self.pageGestorMngP.entryCPCar.get() == "" \
                or self.pageGestorMngP.entryCPBike.get() == "" or self.pageGestorMngP.entryCPTruck.get() == "" \
                or self.pageGestorMngP.entryTax.get() == "":
            self.pageGestorMngP.showError("Preencha todos os campos!")
        elif self.pageGestorMngP.listaEstacionamento.get(ANCHOR) != self.pageGestorMngP.entryPName.get() and self.user.verifyParking(self.pageGestorMngP.entryPName.get()) is True:
            self.pageGestorMngP.showError("Já existe um estacionamento cadastrado com este nome!")
        elif int(self.pageGestorMngP.entryCPCar.get()) < self.parkedCars:
            self.pageGestorMngP.showError("Há mais carros estacionados do que a capacidade!")
        elif int(self.pageGestorMngP.entryCPBike.get()) < self.parkedBikes:
            self.pageGestorMngP.showError("Há mais motos estacionados do que a capacidade!")
        elif int(self.pageGestorMngP.entryCPTruck.get()) < self.parkedTrucks:
            self.pageGestorMngP.showError("Há mais caminhões estacionados do que a capacidade!")
        else:
            self.user.updateParking(self.data["id"], self.pageGestorMngP.entryPName.get(), self.pageGestorMngP.entryCPCar.get(),
                                    self.pageGestorMngP.entryCPBike.get(), self.pageGestorMngP.entryCPTruck.get(),
                                    self.pageGestorMngP.entryTax.get(), self.newCarSlots, self.newBikeSlots, self.newTruckSlots)
            self.pageGestorMngP.listaEstacionamento.config(state="normal")
            self.loadGestorMngP()
            self.pageGestorMngP.showSuccess("Estacionamento atualizado com sucesso!")

    def btnSendNotice(self):
        self.user.sendNotice(self.user.getParkingID(self.pageGestorMngP.listaEstacionamento.get(ANCHOR)), self.pageGestorMngP.alertTitle.get(), self.pageGestorMngP.alertmsgArea.get(1.0, END))
        self.pageGestorMngP.showSuccess("Noticia publicada com sucesso!")

    def loadGestorRelatorios(self):
        self.pageGestorRelatorios.clearEntrys()
        for index, item in enumerate(tableEstacionamentos):
            self.pageGestorRelatorios.listaEstacionamento.insert(index, item["nome"])
        self.pageGestorRelatorios.showGestorRelatorios()

    def loadMeterData(self):
        if self.pageGestorRelatorios.listaEstacionamento.get(ANCHOR) == "":
            pass
        else:
            self.pageGestorRelatorios.btnLoadRelatorio.config(state="disabled")
            self.data = self.user.getParkingData(self.pageGestorRelatorios.listaEstacionamento.get(ANCHOR))
            self.recordsData = self.user.getRecordsByParkingID(self.data['id'])
            self.revenue = 0
            self.records = 0
            self.pageGestorRelatorios.btnClearRelatorio.config(state="normal")

            # Cálculos
            self.dt = datetime.now(tz=None)
            for record in self.recordsData:
                if record["datasaida"].year == self.dt.year and record["datasaida"].month == self.dt.month and record["datasaida"].day == self.dt.day:
                    self.revenue += record['valorpagar']
                    self.records += 1
            self.usedCar = self.data['totalcarro'] - self.data['vagascarro']
            self.usedBike = self.data['totalmoto'] - self.data['vagasmoto']
            self.usedTruck = self.data['totalcaminhao'] - self.data['vagascaminhao']
            self.capacity = ((self.usedCar + self.usedBike + self.usedTruck) * 100) / (self.data['vagascarro'] + self.data['vagasmoto'] + self.data['vagascaminhao'])
            self.pageGestorRelatorios.loadMeters(self.usedCar, self.data['totalcarro'], self.usedBike, self.data['totalmoto'], self.usedTruck, self.data['totalcaminhao'],
                                                 self.records, self.capacity, self.revenue)

    def btnClearMeters(self):
        self.pageGestorRelatorios.clearEntrys()
        self.pageGestorRelatorios.btnLoadRelatorio.config(state="normal")
        self.loadGestorRelatorios()

    def btnFullReport(self):
        webbrowser.open_new_tab('https://docs.google.com/spreadsheets/d/1m1kkVpsRF4z3jxf5eXWXAkbunY7C4nPt_BJbyrVXtPw/')
        self.user.getFullReport(relative_to_assets('sheets.json'))
