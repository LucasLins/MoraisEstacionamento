import webbrowser
from WindowConfigs import *
import Funcionario

canvasLogin = Canvas(
    window,
    bg="#FFFFFF",
    height=768,
    width=1280,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

image_image_1 = PhotoImage(
    file=relative_to_assets("loginbg.png"))
image_1 = canvasLogin.create_image(
    640.0,
    384.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("loginframe.png"))
image_2 = canvasLogin.create_image(
    640.0,
    384.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("github.png"))
button_1 = Button(
    canvasLogin,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open_new_tab("https://github.com/LucasLins"),
    relief="flat"
)
button_1.place(
    x=701.0,
    y=615.0,
    width=32.0,
    height=32.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("linkedin.png"))
button_2 = Button(
    canvasLogin,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open_new_tab("https://www.linkedin.com/in/lucaslins-/"),
    relief="flat"
)
button_2.place(
    x=733.0,
    y=615.0,
    width=32.0,
    height=32.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("entrar.png"))
button_3 = Button(
    canvasLogin,
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: showFuncionario(),
    relief="flat"
)
button_3.place(
    x=704.0,
    y=443.0,
    width=334.0,
    height=44.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("usuariobox.png"))
entry_bg_1 = canvasLogin.create_image(
    869.0,
    315.0,
    image=entry_image_1
)
entry_1 = Entry(
    canvasLogin,
    bd=0,
    bg="#EFEFEF",
    highlightthickness=0
)
entry_1.place(
    x=709.0,
    y=290.0 + 16,
    width=320.0,
    height=30.0
)

canvasLogin.create_text(
    712.0 - 2,
    293.0,
    anchor="nw",
    text="Usuário",
    fill="#494949",
    font=("Poppins SemiBold", 12 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("senhabox.png"))
entry_bg_2 = canvasLogin.create_image(
    869.0,
    390.0,
    image=entry_image_2
)
entry_2 = Entry(
    canvasLogin,
    bd=0,
    bg="#EFEFEF",
    highlightthickness=0
)
entry_2.place(
    x=709.0,
    y=365.0 + 16,
    width=320.0,
    height=30.0
)

canvasLogin.create_text(
    712.0 - 2,
    368.0,
    anchor="nw",
    text="Senha",
    fill="#494949",
    font=("Poppins SemiBold", 12 * -1)
)

canvasLogin.create_text(
    704.0,
    594.0,
    anchor="nw",
    text="Projeto desenvolvido por Lucas Lins",
    fill="#828282",
    font=("Poppins Medium", 12 * -1)
)


def showLogin():
    hideEverything()
    canvasLogin.place(x=0, y=0)

def showFuncionario():
    hideEverything()
    Funcionario.canvas.place(x=0, y=0)

def hideEverything():
    canvasLogin.place_forget()
    Funcionario.canvas.place_forget()


showLogin()
window.mainloop()
