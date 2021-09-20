from view.Configs import *

class ViewFuncionario:
    def __init__(self):
        self.canvasFuncionario = Canvas(
            window,
            bg = "#FFFFFF",
            height = 768,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvasFuncionario.create_image(
            640.0,
            384.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvasFuncionario.create_image(
            640.0,
            384.0,
            image=self.image_image_2
        )

    def showFuncionario(self):
        self.canvasFuncionario.place(x=0, y=0)

    def hideFuncionario(self):
        self.canvasFuncionario.place_forget()

