from view.Configs import *

class FuncionarioHome:
    def __init__(self):
        self.canvasFuncionarioHome = Canvas(
            window,
            bg="#FFFFFF",
            height=768,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvasFuncionarioHome.place(x=0, y=0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("mainbg.png"))
        self.image_1 = self.canvasFuncionarioHome.create_image(
            640.0,
            384.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("bg2.png"))
        self.image_2 = self.canvasFuncionarioHome.create_image(
            640.0,
            384.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("mainhomef.png"))
        self.image_3 = self.canvasFuncionarioHome.create_image(
            743.0,
            384.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("menuf.png"))
        self.image_4 = self.canvasFuncionarioHome.create_image(
            238.0,
            206.0,
            image=self.image_image_4
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("btcarin.png"))
        self.btnCarIn = Button(
            self.canvasFuncionarioHome,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.btnCarIn.place(
            x=139.0,
            y=181.0,
            width=199.0,
            height=56.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("btcarout.png"))
        self.btnCarOut = Button(
            self.canvasFuncionarioHome,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.btnCarOut.place(
            x=139.0,
            y=237.0,
            width=199.0,
            height=56.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("btlogout.png"))
        self.btnLogoutF = Button(
            self.canvasFuncionarioHome,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.btnLogoutF.place(
            x=139.0,
            y=293.0,
            width=199.0,
            height=56.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("btnrefresh.png"))
        self.btnRefreshData = Button(
            self.canvasFuncionarioHome,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.btnRefreshData.place(
            x=1074.0,
            y=66.0,
            width=60.0,
            height=60.0
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("infouser1.png"))
        self.image_5 = self.canvasFuncionarioHome.create_image(
            516.0,
            251.0,
            image=self.image_image_5
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("cpe.png"))
        self.image_6 = self.canvasFuncionarioHome.create_image(
            458.0,
            489.0,
            image=self.image_image_6
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("infoe.png"))
        self.image_7 = self.canvasFuncionarioHome.create_image(
            884.0,
            489.0,
            image=self.image_image_7
        )

        self.image_image_8 = PhotoImage(
            file=relative_to_assets("slotse.png"))
        self.image_8 = self.canvasFuncionarioHome.create_image(
            671.0,
            489.0,
            image=self.image_image_8
        )

        self.image_image_9 = PhotoImage(
            file=relative_to_assets("infouser2.png"))
        self.image_9 = self.canvasFuncionarioHome.create_image(
            850.0,
            251.0,
            image=self.image_image_9
        )

        self.image_image_10 = PhotoImage(
            file=relative_to_assets("alertbox.png"))
        self.image_10 = self.canvasFuncionarioHome.create_image(
            238.0,
            454.0,
            image=self.image_image_10
        )

        self.canvasFuncionarioHome.create_text(
            803.0,
            458.0,
            anchor="nw",
            tag="namepark",
            text="Nome Estacionamento",
            fill="#413D4B",
            font=("Poppins SemiBold", 14 * -1)
        )

        self.canvasFuncionarioHome.create_text(
            804.0,
            508.0,
            tag="price",
            anchor="nw",
            text="R$ 0,00",
            fill="#413D4B",
            font=("Poppins SemiBold", 14 * -1)
        )

        self.canvasFuncionarioHome.create_text(
            361.0,
            60.0 + 15,
            tag="welcome",
            anchor="nw",
            text="Olá, {username}!",
            fill="#413D4B",
            font=("Poppins Regular", 24 * -1)
        )

        self.canvasFuncionarioHome.create_text(
            377.0,
            235.0,
            tag="nameF",
            anchor="nw",
            text="Nome Funcionário",
            fill="#413D4B",
            font=("Poppins SemiBold", 14 * -1)
        )

        self.canvasFuncionarioHome.create_text(
            377.0,
            287.0,
            tag="cpf",
            anchor="nw",
            text="000.000.000-00",
            fill="#413D4B",
            font=("Poppins SemiBold", 14 * -1)
        )

        self.canvasFuncionarioHome.create_text(
            711.0,
            235.0,
            tag="email",
            anchor="nw",
            text="email@email.com",
            fill="#413D4B",
            font=("Poppins SemiBold", 14 * -1)
        )

        self.canvasFuncionarioHome.create_text(
            711.0,
            287.0,
            tag="phone",
            anchor="nw",
            text="(00)90000-0000",
            fill="#413D4B",
            font=("Poppins SemiBold", 14 * -1)
        )

        self.canvasFuncionarioHome.create_text(
            427.0,
            441.0,
            tag="cpcar",
            anchor="nw",
            text="0",
            fill="#656565",
            font=("Poppins SemiBold", 14 * -1)
        )

        self.canvasFuncionarioHome.create_text(
            427.0,
            498.0,
            tag="cpbike",
            anchor="nw",
            text="0",
            fill="#656565",
            font=("Poppins SemiBold", 14 * -1)
        )

        self.canvasFuncionarioHome.create_text(
            427.0,
            555.0,
            tag="cptruck",
            anchor="nw",
            text="0",
            fill="#656565",
            font=("Poppins SemiBold", 14 * -1)
        )

        self.canvasFuncionarioHome.create_text(
            640.0,
            441.0,
            tag="slotcar",
            anchor="nw",
            text="0",
            fill="#656565",
            font=("Poppins SemiBold", 14 * -1)
        )

        self.canvasFuncionarioHome.create_text(
            640.0,
            498.0,
            tag="slotbike",
            anchor="nw",
            text="0",
            fill="#656565",
            font=("Poppins SemiBold", 14 * -1)
        )

        self.canvasFuncionarioHome.create_text(
            640.0,
            555.0,
            tag="slottruck",
            anchor="nw",
            text="0",
            fill="#656565",
            font=("Poppins SemiBold", 14 * -1)
        )

        self.alertBox = Text(
            self.canvasFuncionarioHome,
            fg="#F44336",
            bd=0,
            bg="#FEECEB",
            font=("Poppins Medium", 14 * -1),
            highlightthickness=0,
            state="disabled"
        )
        self.alertBox.place(
            x=148.0,
            y=402.0,
            width=181.0,
            height=135.0
        )

        self.canvasFuncionarioHome.create_text(
            181.0,
            374.0,
            tag="alerttitle",
            anchor="nw",
            text="Aviso",
            fill="#F44336",
            font=("Poppins Medium", 14)
        )

    def showFuncionario(self):
        self.canvasFuncionarioHome.place(x=0, y=0)

    def hideFuncionario(self):
        self.canvasFuncionarioHome.place_forget()


class FuncionarioCarIN:
    def __init__(self):
        self.canvasFuncionarioCarIN = Canvas(
            window,
            bg="#FFFFFF",
            height=768,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("mainbg.png"))
        self.image_1 = self.canvasFuncionarioCarIN.create_image(
            640.0,
            384.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("bg2.png"))
        self.image_2 = self.canvasFuncionarioCarIN.create_image(
            640.0,
            384.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("vehicleinput.png"))
        self.image_3 = self.canvasFuncionarioCarIN.create_image(
            730.0,
            144.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("vehicleoutput.png"))
        self.image_4 = self.canvasFuncionarioCarIN.create_image(
            730.0,
            393.0,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("platebg.png"))
        self.image_5 = self.canvasFuncionarioCarIN.create_image(
            559.0,
            154.0,
            image=self.image_image_5
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entryplate.png"))
        self.entry_bg_1 = self.canvasFuncionarioCarIN.create_image(
            559.0,
            148.0,
            image=self.entry_image_1
        )
        self.entryPlate = Entry(
            self.canvasFuncionarioCarIN,
            bd=0,
            bg="#E2F1FF",
            highlightthickness=0
        )
        self.entryPlate.place(
            x=449.0,
            y=136.0,
            width=220.0,
            height=22.0
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("typebg.png"))
        self.image_6 = self.canvasFuncionarioCarIN.create_image(
            816.0,
            154.0,
            image=self.image_image_6
        )

        self.comboType = Combobox(
            self.canvasFuncionarioCarIN,
            values=[
                "Carro",
                "Moto",
                "Caminhão"],
            state="readonly"
        )
        self.comboType.place(
            x=706.0,
            y=136.0,
            width=220.0,
            height=22.0
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("btnaddcar.png"))
        self.btnAddCar = Button(
            self.canvasFuncionarioCarIN,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.btnAddCar.place(
            x=950.0,
            y=113.0,
            width=60.0,
            height=60.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("btnreturnin.png"))
        self.btnReturnIN = Button(
            self.canvasFuncionarioCarIN,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.btnReturnIN.place(
            x=137.0,
            y=60.0,
            width=202.0,
            height=76.0
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("iconsdata.png"))
        self.image_7 = self.canvasFuncionarioCarIN.create_image(
            473.0,
            418.0,
            image=self.image_image_7
        )

        self.canvasFuncionarioCarIN.create_text(
            508.0,
            337.0 - 7,
            state="hidden",
            tag="carplate",
            anchor="nw",
            text="BRA2021",
            fill="#313131",
            font=("Poppins Regular", 18 * -1)
        )

        self.image_image_8 = PhotoImage(
            file=relative_to_assets("errorbg.png"))
        self.image_8 = self.canvasFuncionarioCarIN.create_image(
            687.0,
            205.0,
            image=self.image_image_8,
            tag="errorbg",
            state="hidden",
        )

        self.canvasFuncionarioCarIN.create_text(
            491.0,
            196.0,
            tag="errorcarin",
            anchor="nw",
            fill="#852019",
            font=("Poppins Regular", 14 * -1)
        )

        self.image_image_9 = PhotoImage(
            file=relative_to_assets("sucessbg.png"))
        self.image_9 = self.canvasFuncionarioCarIN.create_image(
            687.0,
            205.0,
            image=self.image_image_9,
            tag="sucessadd",
            state="hidden",
        )

        self.canvasFuncionarioCarIN.create_text(
            508.0,
            385.0,
            state="hidden",
            tag="datetime",
            anchor="nw",
            text="00/00/0000 00:00:00",
            fill="#313131",
            font=("Poppins Regular", 18 * -1)
        )

        self.canvasFuncionarioCarIN.create_text(
            508.0,
            439.0,
            state="hidden",
            tag="cartype",
            anchor="nw",
            text="Veículo",
            fill="#313131",
            font=("Poppins Regular", 18 * -1)
        )

        self.canvasFuncionarioCarIN.create_text(
            508.0,
            487.0,
            state="hidden",
            tag="employee",
            anchor="nw",
            text="Funcionário",
            fill="#313131",
            font=("Poppins Regular", 18 * -1)
        )

    def showFuncionarioCarIN(self):
        self.canvasFuncionarioCarIN.place(x=0, y=0)

    def hideFuncionarioCarIN(self):
        self.canvasFuncionarioCarIN.place_forget()

    def clearEntrys(self):
        self.entryPlate.delete(0, "end")
        self.canvasFuncionarioCarIN.itemconfigure("errorbg", state="hidden")
        self.canvasFuncionarioCarIN.itemconfigure("errorcarin", text="")
        self.canvasFuncionarioCarIN.itemconfigure("sucessadd", state="hidden")
        self.canvasFuncionarioCarIN.itemconfigure("carplate", state="hidden")
        self.canvasFuncionarioCarIN.itemconfigure("datetime", state="hidden")
        self.canvasFuncionarioCarIN.itemconfigure("cartype", state="hidden")
        self.canvasFuncionarioCarIN.itemconfigure("employee", state="hidden")

    def showError(self, text):
        self.canvasFuncionarioCarIN.itemconfigure("sucessadd", state="hidden")
        self.canvasFuncionarioCarIN.itemconfigure("errorbg", state="normal")
        self.canvasFuncionarioCarIN.itemconfigure("errorcarin", text=text)


class FuncionarioCarOUT:
    def __init__(self):
        self.canvasFuncionarioCarOUT = Canvas(
            window,
            bg="#FFFFFF",
            height=768,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvasFuncionarioCarOUT.place(x=0, y=0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("mainbg.png"))
        self.image_1 = self.canvasFuncionarioCarOUT.create_image(
            640.0,
            384.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("bg2.png"))
        self.image_2 = self.canvasFuncionarioCarOUT.create_image(
            640.0,
            384.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("vehicleInfo.png"))
        self.image_3 = self.canvasFuncionarioCarOUT.create_image(
            818.0,
            384.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("findVehicleBG.png"))
        self.image_4 = self.canvasFuncionarioCarOUT.create_image(
            517.0,
            195.0,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("entryPlateBG2.png"))
        self.image_5 = self.canvasFuncionarioCarOUT.create_image(
            517.0,
            156.0,
            image=self.image_image_5
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entryPlateOut.png"))
        self.entry_bg_1 = self.canvasFuncionarioCarOUT.create_image(
            517.0,
            148.0,
            image=self.entry_image_1
        )
        self.entryPlateOut = Entry(
            self.canvasFuncionarioCarOUT,
            bd=0,
            bg="#E2F1FF",
            highlightthickness=0
        )
        self.entryPlateOut.place(
            x=407.0,
            y=136.0,
            width=220.0,
            height=22.0
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("btnFindOut.png"))
        self.btnFindPlateOut = Button(
            self.canvasFuncionarioCarOUT,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.btnFindPlateOut.place(
            x=485.0,
            y=199.0,
            width=60.0,
            height=60.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("btnReturnOut.png"))
        self.btnReturnOut = Button(
            self.canvasFuncionarioCarOUT,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.btnReturnOut.place(
            x=137.0,
            y=60.0,
            width=202.0,
            height=76.0
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("sucessOut.png"))
        self.image_6 = self.canvasFuncionarioCarOUT.create_image(
            819.0,
            646.0,
            tag="sucessmsg",
            state="hidden",
            image=self.image_image_6
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("iconsOut.png"))
        self.image_7 = self.canvasFuncionarioCarOUT.create_image(
            702.0,
            312.0,
            image=self.image_image_7
        )

        self.image_image_8 = PhotoImage(
            file=relative_to_assets("errorbg2.png"))
        self.image_8 = self.canvasFuncionarioCarOUT.create_image(
            517.0,
            294.0,
            tag="errorbg",
            state="hidden",
            image=self.image_image_8
        )

        self.canvasFuncionarioCarOUT.create_text(
            447.0,
            285.0 - 2,
            anchor="nw",
            tag="errormsg",
            text="",
            fill="#852019",
            font=("Poppins Regular", 14 * -1)
        )

        self.canvasFuncionarioCarOUT.create_text(
            741.0,
            462.0 - 7,
            state="hidden",
            tag="price",
            anchor="nw",
            text="Valor",
            fill="#313131",
            font=("Poppins Regular", 18 * -1)
        )

        self.canvasFuncionarioCarOUT.create_text(
            741.0,
            410.0 - 7,
            state="hidden",
            tag="elapsedtime",
            anchor="nw",
            text="Tempo dentro",
            fill="#313131",
            font=("Poppins Regular", 18 * -1)
        )

        self.canvasFuncionarioCarOUT.create_text(
            741.0,
            358.0 - 7,
            state="hidden",
            tag="datetimeend",
            anchor="nw",
            text="00/00/0000 00:00:00",
            fill="#313131",
            font=("Poppins Regular", 18 * -1)
        )

        self.canvasFuncionarioCarOUT.create_text(
            741.0,
            306.0 - 7,
            state="hidden",
            tag="datetime",
            anchor="nw",
            text="00/00/0000 00:00:00",
            fill="#313131",
            font=("Poppins Regular", 18 * -1)
        )

        self.canvasFuncionarioCarOUT.create_text(
            741.0,
            254.0 - 7,
            state="hidden",
            tag="employee",
            anchor="nw",
            text="Funcionário",
            fill="#313131",
            font=("Poppins Regular", 18 * -1)
        )

        self.canvasFuncionarioCarOUT.create_text(
            741.0,
            202.0 - 7,
            state="hidden",
            tag="cartype",
            anchor="nw",
            text="Veículo",
            fill="#313131",
            font=("Poppins Regular", 18 * -1)
        )

        self.canvasFuncionarioCarOUT.create_text(
            741.0,
            150.0 - 7,
            state="hidden",
            tag="carplate",
            anchor="nw",
            text="BRA2021",
            fill="#313131",
            font=("Poppins Regular", 18 * -1)
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("btnClearInfo.png"))
        self.btnClearInfo = Button(
            self.canvasFuncionarioCarOUT,
            state="disabled",
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.btnClearInfo.place(
            x=827.0,
            y=528.0,
            width=62.0,
            height=64.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("btnConfirmExit.png"))
        self.btnConfirmExit = Button(
            self.canvasFuncionarioCarOUT,
            state="disabled",
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.btnConfirmExit.place(
            x=748.0,
            y=528.0,
            width=64.0,
            height=64.0
        )

    def showFuncionarioCarOUT(self):
        self.canvasFuncionarioCarOUT.place(x=0, y=0)

    def hideFuncionarioCarOUT(self):
        self.canvasFuncionarioCarOUT.place_forget()

    def clearEntrys(self):
        self.canvasFuncionarioCarOUT.itemconfigure("carplate", state="hidden")
        self.canvasFuncionarioCarOUT.itemconfigure("cartype", state="hidden")
        self.canvasFuncionarioCarOUT.itemconfigure("employee", state="hidden")
        self.canvasFuncionarioCarOUT.itemconfigure("datetime", state="hidden")
        self.canvasFuncionarioCarOUT.itemconfigure("datetimeend", state="hidden")
        self.canvasFuncionarioCarOUT.itemconfigure("elapsedtime", state="hidden")
        self.canvasFuncionarioCarOUT.itemconfigure("price", state="hidden")
        self.canvasFuncionarioCarOUT.itemconfigure("errormsg", text="")
        self.canvasFuncionarioCarOUT.itemconfigure("errorbg", state="hidden")
        self.canvasFuncionarioCarOUT.itemconfigure("sucessmsg", state="hidden")
        self.btnClearInfo.config(state="disabled")
        self.btnConfirmExit.config(state="disabled")
        self.entryPlateOut.config(state="normal")
        self.btnFindPlateOut.config(state="normal")
        self.entryPlateOut.delete(0, "end")

    def showError(self, text):
        self.canvasFuncionarioCarOUT.itemconfigure("sucessmsg", state="hidden")
        self.canvasFuncionarioCarOUT.itemconfigure("errorbg", state="normal")
        self.canvasFuncionarioCarOUT.itemconfigure("errormsg", text=text)