from view.Configs import *

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
            height=22.0
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
            y=332.0,
            width=220.0,
            height=22.0
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
            y=264.0,
            width=220.0,
            height=22.0
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

        self.listaEstacionamento = Listbox(self.canvasGestorAddEmp, selectmode=SINGLE)
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