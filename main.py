import PySimpleGUI as ps

ps.theme()


layout_1 = [
    [ps.Text("Mi primer menu",size=(40,10), auto_size_text=True)],
    [ps.Button("Dark Souls , Dark Souls 2, Dark Souls 3",key="BOTON", auto_size_button=True), 
     ps.Button("O Bloodborne",key="BOTON2",auto_size_button=True)],
     [ps.Output(size=(40,10))],
     [ps.Image("BB_Dec_SS_7_1427134535.jpg")]
]

menu = ps.Window("Dark Souls 4Life",layout=layout_1)




while True:
    eventos, valores = menu.read()
    if eventos == ps.WIN_CLOSED:
        break
    if eventos == "BOTON":
        print("BOTON PRESIONADO")
    if eventos == "BOTON2":
        print("BOTON PRESIONADO 2")