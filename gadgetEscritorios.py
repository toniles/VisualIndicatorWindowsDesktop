import tkinter as tk
from tkinter import TOP, X
import keyboard
import pyautogui
import time

# Configura los nombres y colores de los escritorios simulados
desktops = [
    {"name": "MAIN", "color": "orange"},
    {"name": "HELPERS_1", "color": "green"},
    {"name": "HELPERS_2", "color": "green"},
    {"name": "NOTAS", "color": "purple"},
    {"name": "COMUNICACIÓN", "color": "blue"}  
]

# Variable para rastrear el índice del escritorio simulado actual
current_desktop_index = 0

def update_desktop_label(label):
    desktop = desktops[current_desktop_index]
    label.config(text=f"{desktop['name']}", bg=desktop["color"], fg="white")

def change_desktop(direction, label):
    global current_desktop_index
    new_index = current_desktop_index
    if direction == "up":
        if current_desktop_index < len(desktops) - 1:
            new_index += 1
            pyautogui.hotkey('ctrl', 'win', 'right')
    else:  # direction == "down"
        if current_desktop_index > 0:
            new_index -= 1
            pyautogui.hotkey('ctrl', 'win', 'left')
    if new_index != current_desktop_index:
        current_desktop_index = new_index
        update_desktop_label(label)
        time.sleep(0.05)  

def create_always_on_top_window():
    root = tk.Tk()
    root.title("Desktop Indicator")

    window_height = 28
    window_width = 150  # Ajusta este valor según lo que quieras mostrar
    root.geometry(f"{window_width}x{window_height}+0+0")  # Cambiado para pegar a la izquierda

    root.overrideredirect(True)
    root.attributes("-topmost", True)
    

    frame = tk.Frame(root, height=window_height, bg="black")
    frame.pack(fill=X, side=TOP)

    label = tk.Label(frame, text="", font=("Helvetica", 10), bg="black", fg="white")  # Asegura color uniforme
    label.pack(side=TOP, pady=(5, 0))

    update_desktop_label(label)

    # Asigna las funciones a las combinaciones de teclas "Ctrl + Flecha Arriba" y "Ctrl + Flecha Abajo"
    keyboard.add_hotkey('ctrl+right', lambda: change_desktop("up", label), suppress=True)
    keyboard.add_hotkey('ctrl+left', lambda: change_desktop("down", label), suppress=True)

    root.mainloop()

if __name__ == "__main__":
    create_always_on_top_window()
