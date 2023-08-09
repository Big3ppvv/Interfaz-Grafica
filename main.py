import PySimpleGUI as ps

ps.theme()


layout_1 = [
    [ps.Text("Mi primer menu",size=(40,10), auto_size_text=True)],
    [ps.Button("Dark Souls , Dark Souls 2, Dark Souls 3",key="BOTON", auto_size_button=True), 
    ps.Button("O Bloodborne",key="BOTON2",auto_size_button=True)],
    [ps.Output(size=(40,10))],
    [ps.Image(source='./mario (1).png')]
    
]

layout_2 = [
    [ps.Combo(['Opcion 1', 'Opcion2', 'Opcion 3'], key="Elige")]
]

menu = ps.Window("Dark Souls 4Life",layout=layout_1)





while True:
    eventos, valores = menu.read()
    if eventos == ps.WIN_CLOSED:
        break
    if eventos == "BOTON":
        menu.hide()
        menu2 = ps.Window("Eleccion", layout=layout_2)
        while True:
            eventos_2, valores_2 = menu2.read()
            if eventos_2 == ps.WIN_CLOSED:
                menu.un_hide()
                menu2.close()
                break
            if eventos_2 == "Elige":
                print("elegiste")
        print("BOTON PRESIONADO")
    if eventos == "BOTON2":
        print("BOTON PRESIONADO 2")
    if eventos == "BOTON2":
        ps.popup("Creando un popup", title="BOTON2")
