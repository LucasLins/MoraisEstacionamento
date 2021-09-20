import webbrowser
from view.Configs import *


class ViewLogin:
    def __init__(self):
        self.canvasLogin = Canvas(
            window,
            bg="#FFFFFF",
            height=768,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("loginbg.png"))
        self.image_1 = self.canvasLogin.create_image(
            640.0,
            384.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("loginframe.png"))
        self.image_2 = self.canvasLogin.create_image(
            640.0,
            384.0,
            image=self.image_image_2
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("github.png"))
        self.button_1 = Button(
            self.canvasLogin,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: webbrowser.open_new_tab("https://github.com/LucasLins"),
            relief="flat"
        )

        self.button_1.place(
            x=701.0,
            y=615.0,
            width=32.0,
            height=32.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("linkedin.png"))
        self.button_2 = Button(
            self.canvasLogin,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: webbrowser.open_new_tab("https://www.linkedin.com/in/lucaslins-/"),
            relief="flat"
        )
        self.button_2.place(
            x=733.0,
            y=615.0,
            width=32.0,
            height=32.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("entrar.png"))
        self.btnLogin = Button(
            self.canvasLogin,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.btnLogin.place(
            x=704.0,
            y=443.0,
            width=334.0,
            height=44.0
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("usuariobox.png"))
        self.entry_bg_1 = self.canvasLogin.create_image(
            869.0,
            315.0,
            image=self.entry_image_1
        )
        self.usernameEntry = Entry(
            self.canvasLogin,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0
        )
        self.usernameEntry.place(
            x=709.0,
            y=290.0 + 18,
            width=320.0,
            height=28.0
        )

        self.canvasLogin.create_text(
            712.0 - 2,
            293.0,
            anchor="nw",
            text="Usuário",
            fill="#494949",
            font=("Poppins SemiBold", 12 * -1)
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("senhabox.png"))
        self.entry_bg_2 = self.canvasLogin.create_image(
            869.0,
            390.0,
            image=self.entry_image_2
        )
        self.passwordEntry = Entry(
            self.canvasLogin,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            show="\u2022"
        )
        self.passwordEntry.place(
            x=709.0,
            y=365.0 + 18,
            width=320.0,
            height=28.0
        )

        self.canvasLogin.create_text(
            712.0 - 2,
            368.0,
            anchor="nw",
            text="Senha",
            fill="#494949",
            font=("Poppins SemiBold", 12 * -1)
        )

        self.canvasLogin.create_text(
            704.0,
            594.0,
            anchor="nw",
            text="Projeto desenvolvido por Lucas Lins",
            fill="#828282",
            font=("Poppins Medium", 12 * -1)
        )

        self.errorLabel = self.canvasLogin.create_text(
            703.0,
            265.0,
            anchor="nw",
            tag="errorlb",
            text="",
            fill="#eb4034",
            font=("Poppins SemiBold", 12 * -1)
        )

    def clearEntrys(self):
        self.usernameEntry.delete(0, 'end')
        self.passwordEntry.delete(0, 'end')

    def showLogin(self):
        self.canvasLogin.place(x=0, y=0)

    def hideLogin(self):
        self.canvasLogin.place_forget()

    def loginError(self, errortype):
        if errortype == "IU":
            self.canvasLogin.itemconfigure("errorlb", text="Os campos de usuário e/ou senha não podem ficar vazios!")

        elif errortype == "WU":
            self.canvasLogin.itemconfigure("errorlb", text="Usuário e/ou senha incorreto(s)!")

        else:
            self.canvasLogin.itemconfigure("errorlb",
                                           text="Erro desconhecido, entre em contato com o administrador do sistema!")
