from view.Configs import *

class ViewFuncionarioHome:
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

        self.canvasFuncionarioHome.create_text(
            155.0,
            400.0,
            tag="alertmsg",
            anchor="nw",
            text="Nenhum aviso no \nmomento.",
            fill="#F44336",
            font=("Poppins Regular", 14 * -1)
        )

        self.canvasFuncionarioHome.create_text(
            181.0,
            374.0,
            tag="alerttitle",
            anchor="nw",
            text="Aviso",
            fill="#F44336",
            font=("Poppins Medium", 16 * -1)
        )

    def showFuncionario(self):
        self.canvasFuncionarioHome.place(x=0, y=0)

    def hideFuncionario(self):
        self.canvasFuncionarioHome.place_forget()

