from view.Configs import *

#style = Style('cosmo')

class GestorHome:
    def __init__(self):
        self.canvasGestorHome = Canvas(
            window,
            bg="#FFFFFF",
            height=768,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvasGestorHome.place(x=0, y=0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("mainbg.png"))
        self.image_1 = self.canvasGestorHome.create_image(
            640.0,
            384.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("bg2.png"))
        self.image_2 = self.canvasGestorHome.create_image(
            640.0,
            384.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("mainHomeG.png"))
        self.image_3 = self.canvasGestorHome.create_image(
            773.0,
            206.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("bgMenuG.png"))
        self.image_4 = self.canvasGestorHome.create_image(
            265.0,
            264.0,
            image=self.image_image_4
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("btnLogoutG.png"))
        self.btnLogoutG = Button(
            self.canvasGestorHome,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.btnLogoutG.place(
            x=139.0,
            y=405.0,
            width=253.0,
            height=56.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("btnReports.png"))
        self.btnReports = Button(
            self.canvasGestorHome,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.btnReports.place(
            x=139.0,
            y=349.0,
            width=253.0,
            height=56.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("btnManageParkings.png"))
        self.btnManageParking = Button(
            self.canvasGestorHome,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.btnManageParking.place(
            x=139.0,
            y=293.0,
            width=253.0,
            height=56.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("btnAddParking.png"))
        self.btnAddParking = Button(
            self.canvasGestorHome,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.btnAddParking.place(
            x=139.0,
            y=237.0,
            width=253.0,
            height=56.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("btnAddEmployee.png"))
        self.btnAddEmployee = Button(
            self.canvasGestorHome,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.btnAddEmployee.place(
            x=139.0,
            y=181.0,
            width=253.0,
            height=56.0
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("bgUserInfo3.png"))
        self.image_5 = self.canvasGestorHome.create_image(
            582.5429077148438,
            251.0,
            image=self.image_image_5
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("bgUserInfo4.png"))
        self.image_6 = self.canvasGestorHome.create_image(
            928.63134765625,
            251.0,
            image=self.image_image_6
        )

        self.canvasGestorHome.create_text(
            422.0,
            60.0 + 15,
            anchor="nw",
            tag="welcome",
            text="Olá, {username}!",
            fill="#413D4B",
            font=("Poppins Regular", 24 * -1)
        )

        self.canvasGestorHome.create_text(
            438.0,
            235.0,
            anchor="nw",
            tag="nameG",
            text="{name}",
            fill="#413D4B",
            font=("Poppins SemiBold", 14 * -1)
        )

        self.canvasGestorHome.create_text(
            438.0,
            287.0,
            anchor="nw",
            tag="cpf",
            text="{CPF}",
            fill="#413D4B",
            font=("Poppins SemiBold", 14 * -1)
        )

        self.canvasGestorHome.create_text(
            784.0,
            235.0,
            anchor="nw",
            tag="email",
            text="{email}",
            fill="#413D4B",
            font=("Poppins SemiBold", 14 * -1)
        )

        self.canvasGestorHome.create_text(
            784.0,
            287.0,
            anchor="nw",
            tag="phone",
            text="{phone}",
            fill="#413D4B",
            font=("Poppins SemiBold", 14 * -1)
        )

    def showGestorHome(self):
        self.canvasGestorHome.place(x=0, y=0)

    def hideGestorHome(self):
        self.canvasGestorHome.place_forget()

class GestorAddF:
    def __init__(self):

        self.canvasGestorAddEmp = Canvas(
            window,
            bg="#FFFFFF",
            height=768,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvasGestorAddEmp.place(x=0, y=0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("mainbg.png"))
        self.image_1 = self.canvasGestorAddEmp.create_image(
            640.0,
            384.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("bg2.png"))
        self.image_2 = self.canvasGestorAddEmp.create_image(
            640.0,
            384.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("entryInfoBg.png"))
        self.image_3 = self.canvasGestorAddEmp.create_image(
            732.0,
            283.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("entryBGUser.png"))
        self.image_4 = self.canvasGestorAddEmp.create_image(
            559.0,
            154.0,
            image=self.image_image_4
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entryUser.png"))
        self.entry_bg_1 = self.canvasGestorAddEmp.create_image(
            559.0,
            148.0,
            image=self.entry_image_1
        )
        self.userEntry = Entry(
            self.canvasGestorAddEmp,
            bd=0,
            bg="#E2F1FF",
            highlightthickness=0
        )
        self.userEntry.place(
            x=449.0,
            y=136.0,
            width=220.0,
            height=22.0
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("entryBGPass.png"))
        self.image_5 = self.canvasGestorAddEmp.create_image(
            816.0,
            154.0,
            image=self.image_image_5
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entryPass.png"))
        self.entry_bg_2 = self.canvasGestorAddEmp.create_image(
            816.0,
            148.0,
            image=self.entry_image_2
        )
        self.passEntry = Entry(
            self.canvasGestorAddEmp,
            bd=0,
            bg="#E2F1FF",
            highlightthickness=0
        )
        self.passEntry.place(
            x=706.0,
            y=136.0,
            width=220.0,
            height=22.0
        )

        self.canvasGestorAddEmp.create_text(
            449.0,
            188.0,
            anchor="nw",
            text="Dados do funcionário",
            fill="#413D4B",
            font=("Poppins Regular", 24 * -1)
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("entryBGName.png"))
        self.image_6 = self.canvasGestorAddEmp.create_image(
            559.0,
            282.0,
            image=self.image_image_6
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entryName.png"))
        self.entry_bg_3 = self.canvasGestorAddEmp.create_image(
            559.0,
            276.0,
            image=self.entry_image_3
        )
        self.entryName = Entry(
            self.canvasGestorAddEmp,
            bd=0,
            bg="#E2F1FF",
            highlightthickness=0
        )
        self.entryName.place(
            x=449.0,
            y=264.0,
            width=220.0,
            height=22.0
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("entryBGEmail.png"))
        self.image_7 = self.canvasGestorAddEmp.create_image(
            559.0,
            350.0,
            image=self.image_image_7
        )

        self.image_image_8 = PhotoImage(
            file=relative_to_assets("entryBGGender.png"))
        self.image_8 = self.canvasGestorAddEmp.create_image(
            559.0,
            418.0,
            image=self.image_image_8
        )

        self.comboGender = Combobox(
            self.canvasGestorAddEmp,
            values=[
                "M",
                "F"],
            state="readonly"
        )

        self.comboGender.place(
            x=449.0,
            y=400.0,
            width=220.0,
            height=30.0
        )

        self.entry_image_5 = PhotoImage(
            file=relative_to_assets("entryEmail.png"))
        self.entry_bg_5 = self.canvasGestorAddEmp.create_image(
            559.0,
            344.0,
            image=self.entry_image_5
        )
        self.entryEmail = Entry(
            self.canvasGestorAddEmp,
            bd=0,
            bg="#E2F1FF",
            highlightthickness=0
        )
        self.entryEmail.place(
            x=449.0,
            y=332.0,
            width=220.0,
            height=22.0
        )

        self.image_image_9 = PhotoImage(
            file=relative_to_assets("entryBGPhone.png"))
        self.image_9 = self.canvasGestorAddEmp.create_image(
            816.0,
            350.0,
            image=self.image_image_9
        )

        self.entryPhone = MaskedWidget(
            self.canvasGestorAddEmp,
            'fixed',
            # bd=0,
            # bg="#E2F1FF",
            mask='(88)98888-8888',
            # highlightthickness=0
        )
        self.entryPhone.place(
            x=706.0,
            y=328.0,
            width=220.0,
            height=30.0
        )

        self.image_image_10 = PhotoImage(
            file=relative_to_assets("entryBGCPF.png"))
        self.image_10 = self.canvasGestorAddEmp.create_image(
            816.0,
            282.0,
            image=self.image_image_10
        )

        self.entryCPF = MaskedWidget(
            self.canvasGestorAddEmp,
            'fixed',
            # bd=0,
            # bg="#E2F1FF",
            mask='888.888.888-88',
            # highlightthickness=0
        )
        self.entryCPF.place(
            x=706.0,
            y=264.0 - 4,
            width=220.0,
            height=30.0
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("btnAddF.png"))
        self.btnAddFuncionario = Button(
            self.canvasGestorAddEmp,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.btnAddFuncionario.place(
            x=950.0,
            y=113.0,
            width=60.0,
            height=60.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("btnReturnAddF.png"))
        self.btnReturn = Button(
            self.canvasGestorAddEmp,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.btnReturn.place(
            x=137.0,
            y=60.0,
            width=255.0,
            height=76.0
        )

        self.image_image_11 = PhotoImage(
            file=relative_to_assets("errorBGAddF.png"))
        self.image_11 = self.canvasGestorAddEmp.create_image(
            687.0,
            468.0,
            tag="errorbg",
            state="hidden",
            image=self.image_image_11
        )

        self.canvasGestorAddEmp.create_text(
            491.0,
            459.0,
            anchor="nw",
            tag="errormsg",
            state="hidden",
            text="Erro",
            fill="#852019",
            font=("Poppins Regular", 14 * -1)
        )

        self.image_image_12 = PhotoImage(
            file=relative_to_assets("successmsgAddF.png"))
        self.image_12 = self.canvasGestorAddEmp.create_image(
            687.0,
            468.0,
            tag="successmsg",
            state="hidden",
            image=self.image_image_12
        )

        self.image_image_13 = PhotoImage(
            file=relative_to_assets("bgParkingList.png"))
        self.image_13 = self.canvasGestorAddEmp.create_image(
            264.25999450683594,
            330.0,
            image=self.image_image_13
        )

        self.listaEstacionamento = Listbox(self.canvasGestorAddEmp, selectmode=SINGLE, bg="#E2F1FF", highlightthickness=0, bd=0)
        self.listaEstacionamento.place(x=148,y=213, width=230, height=285)

    def showGestorAddF(self):
        self.canvasGestorAddEmp.place(x=0,y=0)

    def hideGestorAddF(self):
        self.canvasGestorAddEmp.place_forget()

    def clearEntrys(self):
        self.userEntry.delete(0, 'end')
        self.passEntry.delete(0, 'end')
        self.entryName.delete(0, 'end')
        self.entryEmail.delete(0, 'end')
        self.entryCPF.clean()
        self.entryPhone.clean()
        self.canvasGestorAddEmp.itemconfigure("errormsg", state="hidden")
        self.canvasGestorAddEmp.itemconfigure("errorbg", state="hidden")
        self.canvasGestorAddEmp.itemconfigure("successmsg", state="hidden")
        self.listaEstacionamento.delete(0, "end")

    def showError(self, message):
        self.canvasGestorAddEmp.itemconfigure("errormsg", state="normal", text=message)
        self.canvasGestorAddEmp.itemconfigure("errorbg", state="normal")
        

class GestorAddE:
    def __init__(self):
        self.canvasGestorAddE = Canvas(
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
        self.image_1 = self.canvasGestorAddE.create_image(
            640.0,
            384.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("bg2.png"))
        self.image_2 = self.canvasGestorAddE.create_image(
            640.0,
            384.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("bgAddE.png"))
        self.image_3 = self.canvasGestorAddE.create_image(
            772.0,
            155.0,
            image=self.image_image_3
        )

        self.canvasGestorAddE.create_text(
            449.0,
            60.0,
            anchor="nw",
            text="Dados do Estacionamento",
            fill="#413D4B",
            font=("Poppins Regular", 24 * -1)
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("entryBGNameE.png"))
        self.image_4 = self.canvasGestorAddE.create_image(
            559.0,
            154.0,
            image=self.image_image_4
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entryNameE.png"))
        self.entry_bg_1 = self.canvasGestorAddE.create_image(
            559.0,
            148.0,
            image=self.entry_image_1
        )
        self.entryPName = Entry(
            self.canvasGestorAddE,
            bd=0,
            bg="#E2F1FF",
            highlightthickness=0
        )
        self.entryPName.place(
            x=449.0,
            y=136.0,
            width=220.0,
            height=22.0
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("entryBGCPC.png"))
        self.image_5 = self.canvasGestorAddE.create_image(
            720.0,
            154.0,
            image=self.image_image_5
        )

        self. entry_image_2 = PhotoImage(
            file=relative_to_assets("entryCPC.png"))
        self.entry_bg_2 = self.canvasGestorAddE.create_image(
            720.5,
            148.0,
            image=self.entry_image_2
        )
        self.entryCPCar = Entry(
            self.canvasGestorAddE,
            bd=0,
            bg="#E2F1FF",
            highlightthickness=0
        )
        self.entryCPCar.place(
            x=688.0,
            y=136.0,
            width=65.0,
            height=22.0
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("entryBGCPB.png"))
        self.image_6 = self.canvasGestorAddE.create_image(
            792.0,
            154.0 + 3,
            image=self.image_image_6
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entryCPB.png"))
        self.entry_bg_3 = self.canvasGestorAddE.create_image(
            792.5,
            148.0,
            image=self.entry_image_3
        )
        self.entryCPBike = Entry(
            self.canvasGestorAddE,
            bd=0,
            bg="#E2F1FF",
            highlightthickness=0
        )
        self.entryCPBike.place(
            x=760.0,
            y=136.0,
            width=65.0,
            height=22.0
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("entryBGCPT.png"))
        self.image_7 = self.canvasGestorAddE.create_image(
            864.0,
            154.0 + 3,
            image=self.image_image_7
        )

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entryCPT.png"))
        self.entry_bg_4 = self.canvasGestorAddE.create_image(
            864.5,
            148.0,
            image=self.entry_image_4
        )
        self.entryCPTruck = Entry(
            self.canvasGestorAddE,
            bd=0,
            bg="#E2F1FF",
            highlightthickness=0
        )
        self.entryCPTruck.place(
            x=832.0,
            y=136.0,
            width=65.0,
            height=22.0
        )

        self.image_image_8 = PhotoImage(
            file=relative_to_assets("entryBGTax.png"))
        self.image_8 = self.canvasGestorAddE.create_image(
            948.0,
            154.0 + 1,
            image=self.image_image_8
        )

        self.entry_image_5 = PhotoImage(
            file=relative_to_assets("entryTax.png"))
        self.entry_bg_5 = self.canvasGestorAddE.create_image(
            948.0,
            148.0,
            image=self.entry_image_5
        )
        self.entryTax = Entry(
            self.canvasGestorAddE,
            bd=0,
            bg="#E2F1FF",
            highlightthickness=0
        )
        self.entryTax.place(
            x=916.0,
            y=136.0,
            width=64.0,
            height=22.0
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("btnAddE.png"))
        self.btnAddE = Button(
            self.canvasGestorAddE,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.btnAddE.place(
            x=1060.0,
            y=114.0,
            width=60.0,
            height=60.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("btnReturnAddE.png"))
        self.btnReturnAddE = Button(
            self.canvasGestorAddE,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.btnReturnAddE.place(
            x=137.0,
            y=60.0,
            width=255.0,
            height=76.0
        )

        self.image_image_9 = PhotoImage(
            file=relative_to_assets("bgErrorAddE.png"))
        self.image_9 = self.canvasGestorAddE.create_image(
            687.0,
            215.0,
            tag="errorbg",
            state="hidden",
            image=self.image_image_9
        )

        self.canvasGestorAddE.create_text(
            491.0,
            206.0,
            anchor="nw",
            tag="errormsg",
            text="Erro",
            state="hidden",
            fill="#852019",
            font=("Poppins Regular", 14 * -1)
        )

        self.image_image_10 = PhotoImage(
            file=relative_to_assets("bgSuccessBgE.png"))
        self.image_10 = self.canvasGestorAddE.create_image(
            687.0,
            215.0,
            tag="successmsg",
            state="hidden",
            image=self.image_image_10
        )

    def hideGestorAddE(self):
        self.canvasGestorAddE.place_forget()

    def showGestorAddE(self):
        self.canvasGestorAddE.place(x=0,y=0)

    def clearEntrys(self):
        self.entryPName.delete(0, 'end')
        self.entryCPCar.delete(0, 'end')
        self.entryCPBike.delete(0, 'end')
        self.entryCPTruck.delete(0, 'end')
        self.entryTax.delete(0, 'end')
        self.canvasGestorAddE.itemconfigure("successmsg", state="hidden")
        self.canvasGestorAddE.itemconfigure("errormsg", state="hidden")
        self.canvasGestorAddE.itemconfigure("errorbg", state="hidden")

    def showError(self, message):
        self.canvasGestorAddE.itemconfigure("errorbg", state="normal")
        self.canvasGestorAddE.itemconfigure("errormsg", state="normal", text=message)
        

class GestorManageP:
    def __init__(self):
        self.canvasManageP = Canvas(
            window,
            bg="#FFFFFF",
            height=768,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvasManageP.place(x=0, y=0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("mainbg.png"))
        self.image_1 = self.canvasManageP.create_image(
            640.0,
            384.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("bg2.png"))
        self.image_2 = self.canvasManageP.create_image(
            640.0,
            384.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("ManageParkingBG.png"))
        self.image_3 = self.canvasManageP.create_image(
            774.0,
            302.0,
            image=self.image_image_3
        )

        self.canvasManageP.create_text(
            449.0,
            60.0,
            anchor="nw",
            text="Atualizar dados",
            fill="#413D4B",
            font=("Poppins Regular", 24 * -1)
        )

        self.canvasManageP.create_text(
            449.0,
            204.0,
            anchor="nw",
            text="Publicar aviso",
            fill="#413D4B",
            font=("Poppins Regular", 24 * -1)
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("entryBGNameE.png"))
        self.image_4 = self.canvasManageP.create_image(
            559.0,
            154.0,
            image=self.image_image_4
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entryNameE.png"))
        self.entry_bg_1 = self.canvasManageP.create_image(
            559.0,
            148.0,
            image=self.entry_image_1
        )
        self.entryPName = Entry(
            self.canvasManageP,
            bd=0,
            bg="#E2F1FF",
            highlightthickness=0
        )
        self.entryPName.place(
            x=449.0,
            y=136.0,
            width=220.0,
            height=22.0
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("entryBGCPC.png"))
        self.image_5 = self.canvasManageP.create_image(
            720.0,
            154.0,
            image=self.image_image_5
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entryCPC.png"))
        self.entry_bg_2 = self.canvasManageP.create_image(
            720.5,
            148.0,
            image=self.entry_image_2
        )
        self.entryCPCar = Entry(
            self.canvasManageP,
            bd=0,
            bg="#E2F1FF",
            highlightthickness=0
        )
        self.entryCPCar.place(
            x=688.0,
            y=136.0,
            width=65.0,
            height=22.0
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("entryBGCPB.png"))
        self.image_6 = self.canvasManageP.create_image(
            792.0,
            154.0 + 3,
            image=self.image_image_6
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entryCPB.png"))
        self.entry_bg_3 = self.canvasManageP.create_image(
            792.5,
            148.0,
            image=self.entry_image_3
        )
        self.entryCPBike = Entry(
            self.canvasManageP,
            bd=0,
            bg="#E2F1FF",
            highlightthickness=0
        )
        self.entryCPBike.place(
            x=760.0,
            y=136.0,
            width=65.0,
            height=22.0
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("entryBGCPT.png"))
        self.image_7 = self.canvasManageP.create_image(
            864.0,
            154.0 + 3,
            image=self.image_image_7
        )

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entryCPT.png"))
        self.entry_bg_4 = self.canvasManageP.create_image(
            864.5,
            148.0,
            image=self.entry_image_4
        )
        self.entryCPTruck = Entry(
            self.canvasManageP,
            bd=0,
            bg="#E2F1FF",
            highlightthickness=0
        )
        self.entryCPTruck.place(
            x=832.0,
            y=136.0,
            width=65.0,
            height=22.0
        )

        self.image_image_8 = PhotoImage(
            file=relative_to_assets("entryBGTax.png"))
        self.image_8 = self.canvasManageP.create_image(
            948.0,
            154.0 + 1,
            image=self.image_image_8
        )

        self.entry_image_5 = PhotoImage(
            file=relative_to_assets("entryTax.png"))
        self.entry_bg_5 = self.canvasManageP.create_image(
            948.0,
            148.0,
            image=self.entry_image_5
        )
        self.entryTax = Entry(
            self.canvasManageP,
            bd=0,
            bg="#E2F1FF",
            highlightthickness=0
        )
        self.entryTax.place(
            x=916.0,
            y=136.0,
            width=64.0,
            height=22.0
        )

        self.entry_image_6 = PhotoImage(
            file=relative_to_assets("alertTitle.png"))
        self.entry_bg_6 = self.canvasManageP.create_image(
            565.0,
            290.0,
            image=self.entry_image_6
        )
        self.alertTitle = Entry(
            self.canvasManageP,
            fg="#F44336",
            bd=0,
            bg="#FEECEB",
            font=("Poppins Medium", 14),
            highlightthickness=0
        )
        self.alertTitle.place(
            x=491.0,
            y=278.0,
            width=148.0,
            height=22.0
        )

        self.entry_image_7 = PhotoImage(
            file=relative_to_assets("alertMsg.png"))
        self.entry_bg_7 = self.canvasManageP.create_image(
            548.5,
            374.5,
            image=self.entry_image_7
        )
        self.alertmsgArea = Text(
            self.canvasManageP,
            fg="#F44336",
            bd=0,
            bg="#FEECEB",
            font=("Poppins Medium", 14 * -1),
            highlightthickness=0
        )
        self.alertmsgArea.place(
            x=458.0,
            y=306.0,
            width=181.0,
            height=135.0
        )

        self.image_image_9 = PhotoImage(
            file=relative_to_assets("parkingListBg.png"))
        self.image_9 = self.canvasManageP.create_image(
            264.0,
            343.0,
            image=self.image_image_9
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("btnUpdateParking.png"))
        self.btnUpdateParking = Button(
            self.canvasManageP,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.btnUpdateParking.place(
            x=1060.0,
            y=114.0,
            width=60.0,
            height=60.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("btnAddNotice.png"))
        self.btnAddNotice = Button(
            self.canvasManageP,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.btnAddNotice.place(
            x=676.0,
            y=328.0,
            width=60.0,
            height=60.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("btnLoadParking.png"))
        self.btnLoadParking = Button(
            self.canvasManageP,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.btnLoadParking.place(
            x=198.0,
            y=476.0,
            width=62.0,
            height=64.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("btnClearPInfo.png"))
        self.btnClearInfo = Button(
            self.canvasManageP,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.btnClearInfo.place(
            x=267.0,
            y=476.0,
            width=62.0,
            height=64.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("btnReturnMngE.png"))
        self.btnReturnMngE = Button(
            self.canvasManageP,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        self.btnReturnMngE.place(
            x=137.0,
            y=60.0,
            width=255.0,
            height=76.0
        )

        self.image_image_10 = PhotoImage(
            file=relative_to_assets("errorbg.png"))
        self.image_10 = self.canvasManageP.create_image(
            687.0,
            510.0,
            tag="errorbg",
            state="hidden",
            image=self.image_image_10
        )

        self.canvasManageP.create_text(
            491.0,
            501.0,
            tag="errormsg",
            state="hidden",
            anchor="nw",
            text="Erro",
            fill="#852019",
            font=("Poppins Regular", 14 * -1)
        )

        self.image_image_11 = PhotoImage(
            file=relative_to_assets("successbg2.png"))
        self.image_11 = self.canvasManageP.create_image(
            687.0,
            510.0,
            tag="successbg",
            state="hidden",
            image=self.image_image_11
        )

        self.canvasManageP.create_text(
            491.0,
            501.0,
            tag="successmsg",
            state="hidden",
            anchor="nw",
            text="Estacionamento cadastrado com sucesso!",
            fill="#176226",
            font=("Poppins Regular", 14 * -1)
        )

        self.listaEstacionamento = Listbox(self.canvasManageP, selectmode=SINGLE, bg="#E2F1FF", highlightthickness=0, bd=0)
        self.listaEstacionamento.place(x=148, y=203-5, width=230, height=265)
        
    def hideGestorMngP(self):
        self.canvasManageP.place_forget()

    def showGestorMngP(self):
        self.canvasManageP.place(x=0,y=0)

    def clearEntrys(self):
        self.entryPName.delete(0, 'end')
        self.entryCPCar.delete(0, 'end')
        self.entryCPBike.delete(0, 'end')
        self.entryCPTruck.delete(0, 'end')
        self.entryTax.delete(0, 'end')
        self.canvasManageP.itemconfigure("successbg", state="hidden")
        self.canvasManageP.itemconfigure("successmsg", state="hidden")
        self.canvasManageP.itemconfigure("errormsg", state="hidden")
        self.canvasManageP.itemconfigure("errorbg", state="hidden")
        self.alertTitle.delete(0, END)
        self.alertmsgArea.delete(1.0, END)
        self.listaEstacionamento.delete(0, "end")

    def showError(self, message):
        self.canvasManageP.itemconfigure("errorbg", state="normal")
        self.canvasManageP.itemconfigure("errormsg", state="normal", text=message)

    def showSuccess(self, message):
        self.canvasManageP.itemconfigure("successbg", state="normal")
        self.canvasManageP.itemconfigure("successmsg", state="normal", text=message)

    def disableEntrys(self):
        self.btnLoadParking.config(state="normal")
        self.listaEstacionamento.config(state="normal")
        self.entryPName.config(state="disabled")
        self.entryCPCar.config(state="disabled")
        self.entryCPBike.config(state="disabled")
        self.entryCPTruck.config(state="disabled")
        self.entryTax.config(state="disabled")
        self.alertTitle.config(state="disabled")
        self.alertmsgArea.config(state="disabled")
        self.btnUpdateParking.config(state="disabled")
        self.btnAddNotice.config(state="disabled")
        self.btnClearInfo.config(state="disabled")
        
    def enableEntrys(self):
        self.btnLoadParking.config(state="disabled")
        self.listaEstacionamento.config(state="disabled")
        self.entryPName.config(state="normal")
        self.entryCPCar.config(state="normal")
        self.entryCPBike.config(state="normal")
        self.entryCPTruck.config(state="normal")
        self.entryTax.config(state="normal")
        self.alertTitle.config(state="normal")
        self.alertmsgArea.config(state="normal")
        self.btnUpdateParking.config(state="normal")
        self.btnAddNotice.config(state="normal")
        self.btnClearInfo.config(state="normal")


# noinspection PyTypeChecker
class GestorRelatorios:
    def __init__(self):
        self.canvasGestorRelatorio = Canvas(
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
        self.image_1 = self.canvasGestorRelatorio.create_image(
            640.0,
            384.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("bg2.png"))
        self.image_2 = self.canvasGestorRelatorio.create_image(
            640.0,
            384.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("bgRelatorio.png"))
        self.image_3 = self.canvasGestorRelatorio.create_image(
            774.0,
            384.0,
            image=self.image_image_3
        )

        self.canvasGestorRelatorio.create_text(
            449.0,
            60.0,
            anchor="nw",
            text="Relatório do dia",
            fill="#413D4B",
            font=("Poppins Regular", 24 * -1)
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("parkingListBg.png"))
        self.image_4 = self.canvasGestorRelatorio.create_image(
            264.0,
            343.0,
            image=self.image_image_4
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("btnRelatorioGeral.png"))
        self.btnRelatorioFull = Button(
            self.canvasGestorRelatorio,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.btnRelatorioFull.place(
            x=136.0,
            y=556.0,
            width=255.0,
            height=76.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("btnLoadParking.png"))
        self.btnLoadRelatorio = Button(
            self.canvasGestorRelatorio,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.btnLoadRelatorio.place(
            x=198.0,
            y=476.0,
            width=62.0,
            height=64.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("btnClearPInfo.png"))
        self.btnClearRelatorio = Button(
            self.canvasGestorRelatorio,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            state="disabled",
            relief="flat"
        )
        self.btnClearRelatorio.place(
            x=267.0,
            y=476.0,
            width=62.0,
            height=64.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("btnReturnRelatorio.png"))
        self.btnReturnRelatorio = Button(
            self.canvasGestorRelatorio,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.btnReturnRelatorio.place(
            x=137.0,
            y=60.0,
            width=255.0,
            height=76.0
        )

        self.listaEstacionamento = Listbox(self.canvasGestorRelatorio, selectmode=SINGLE, bg="#E2F1FF", highlightthickness=0, bd=0)
        self.listaEstacionamento.place(x=148, y=203 - 5, width=230, height=265)

        self.mCar = Meter(master=self.canvasGestorRelatorio, metersize=180, amountused=0, amounttotal=100, padding=20,
                        metertype='semi', labeltext='Carros', textappend='/100', interactive=False, stripethickness=10,
                        meterstyle='info.TMeter')
        self.mBike = Meter(master=self.canvasGestorRelatorio, metersize=180, amountused=0, amounttotal=100, padding=20,
                        metertype='semi', labeltext='Motos', textappend='/100', interactive=False, stripethickness=5,
                        meterstyle='info.TMeter')
        self.mTruck = Meter(master=self.canvasGestorRelatorio, metersize=180, amountused=0, amounttotal=100, padding=20,
                        metertype='semi', labeltext='Caminhões', textappend='/100', interactive=False, stripethickness=15,
                        meterstyle='info.TMeter')
        self.mCar.place(x=480 - 21, y=100)
        self.mBike.place(x=685 - 21, y=100)
        self.mTruck.place(x=890 - 21, y=100)

        self.mRecords = Meter(master=self.canvasGestorRelatorio, metersize=180, amountused=0, amounttotal=100, padding=20,
                              labeltext='Registros', textappend='Veículos', interactive=False, stripethickness=10,
                              meterstyle='danger.TMeter')
        self.mTotalCP = Meter(master=self.canvasGestorRelatorio, metersize=180, amountused=0, amounttotal=100, padding=20,
                              stripethickness=2, labeltext='Lotação', textappend='%', interactive=False, meterstyle='warning.TMeter')
        self.mRevenue = Meter(master=self.canvasGestorRelatorio, metersize=180, amountused=0, amounttotal=100, padding=20,
                              labeltext='Receita', textappend='R$', interactive=False, stripethickness=5, meterstyle='success.TMeter')
        self.mRecords.place(x=480 - 21, y=300)
        self.mTotalCP.place(x=685 - 21, y=300)
        self.mRevenue.place(x=890 - 21, y=300)

    def showGestorRelatorios(self):
        self.canvasGestorRelatorio.place(x=0,y=0)

    def hideGestorRelatorios(self):
        self.canvasGestorRelatorio.place_forget()

    def clearEntrys(self):
        self.listaEstacionamento.delete(0, "end")
        self.mCar = Meter(master=self.canvasGestorRelatorio, metersize=180, amountused=0, amounttotal=100, padding=20,
                          metertype='semi', labeltext='Carros', textappend='/100', interactive=False,
                          stripethickness=10,
                          meterstyle='info.TMeter')
        self.mBike = Meter(master=self.canvasGestorRelatorio, metersize=180, amountused=0, amounttotal=100, padding=20,
                           metertype='semi', labeltext='Motos', textappend='/100', interactive=False, stripethickness=5,
                           meterstyle='info.TMeter')
        self.mTruck = Meter(master=self.canvasGestorRelatorio, metersize=180, amountused=0, amounttotal=100, padding=20,
                            metertype='semi', labeltext='Caminhões', textappend='/100', interactive=False,
                            stripethickness=15,
                            meterstyle='info.TMeter')
        self.mCar.place(x=480 - 21, y=100)
        self.mBike.place(x=685 - 21, y=100)
        self.mTruck.place(x=890 - 21, y=100)

        self.mRecords = Meter(master=self.canvasGestorRelatorio, metersize=180, amountused=0, amounttotal=100,
                              padding=20,
                              labeltext='Registros', textappend='Veículos', interactive=False, stripethickness=10,
                              meterstyle='danger.TMeter')
        self.mTotalCP = Meter(master=self.canvasGestorRelatorio, metersize=180, amountused=0, amounttotal=100,
                              padding=20,
                              stripethickness=2, labeltext='Lotação', textappend='%', interactive=False,
                              meterstyle='warning.TMeter')
        self.mRevenue = Meter(master=self.canvasGestorRelatorio, metersize=180, amountused=0, amounttotal=100,
                              padding=20,
                              labeltext='Receita', textappend='R$', interactive=False, stripethickness=5,
                              meterstyle='success.TMeter')
        self.mRecords.place(x=480 - 21, y=300)
        self.mTotalCP.place(x=685 - 21, y=300)
        self.mRevenue.place(x=890 - 21, y=300)

    def loadMeters(self, usedCar, totalCar, usedBike, totalBike, usedTruck, totalTruck, records, capacity, revenue):

        self.mCar = Meter(master=self.canvasGestorRelatorio, metersize=180, amountused=usedCar, amounttotal=totalCar, padding=20,
                          metertype='semi', labeltext='Carros', textappend=f'/{totalCar}', interactive=False, stripethickness=10,
                          meterstyle='info.TMeter')
        self.mBike = Meter(master=self.canvasGestorRelatorio, metersize=180, amountused=usedBike, amounttotal=totalBike, padding=20,
                           metertype='semi', labeltext='Motos', textappend=f'/{totalBike}', interactive=False, stripethickness=5,
                           meterstyle='info.TMeter')
        self.mTruck = Meter(master=self.canvasGestorRelatorio, metersize=180, amountused=usedTruck, amounttotal=totalTruck, padding=20,
                            metertype='semi', labeltext='Caminhões', textappend=f'/{totalTruck}', interactive=False, stripethickness=15,
                            meterstyle='info.TMeter')
        self.mCar.place(x=480 - 21, y=100)
        self.mBike.place(x=685 - 21, y=100)
        self.mTruck.place(x=890 - 21, y=100)

        self.mRecords = Meter(master=self.canvasGestorRelatorio, metersize=180, amountused=records, amounttotal=records+1,
                              padding=20, labeltext='Registros', textappend='Veículos', interactive=False, stripethickness=10,
                              meterstyle='danger.TMeter')
        self.mTotalCP = Meter(master=self.canvasGestorRelatorio, metersize=180, amountused=f'{capacity:.0f}', amounttotal=100,
                              padding=20, stripethickness=2, labeltext='Lotação', textappend='%', interactive=False,
                              meterstyle='warning.TMeter')
        self.mRevenue = Meter(master=self.canvasGestorRelatorio, metersize=180, amountused=f'{revenue:.1f}', amounttotal=revenue+1,
                              padding=20, labeltext='Receita', textappend='R$', interactive=False, stripethickness=5,
                              meterstyle='success.TMeter')
        self.mRecords.place(x=480 - 21, y=300)
        self.mTotalCP.place(x=685 - 21, y=300)
        self.mRevenue.place(x=890 - 21, y=300)
        
        
