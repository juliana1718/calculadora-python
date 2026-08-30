import tkinter as tk
from tkinter import messagebox


def abrir_resta(ventana_principal):

    ventana = tk.Toplevel(ventana_principal)
    ventana.title("RESTA")
    ventana.geometry("450x650")

    # Título
    titulo = tk.Label(
        ventana,
        text="RESTA",
        font=("Arial", 24, "bold")
    )
    titulo.pack(pady=8)

    # Primer número
    tk.Label(
        ventana,
        text="Primer número"
    ).pack()

    numero1 = tk.Entry(
        ventana,
        font=("Arial", 14),
        justify="center"
    )
    numero1.pack(pady=2)

    # Segundo número
    tk.Label(
        ventana,
        text="Segundo número"
    ).pack()

    numero2 = tk.Entry(
        ventana,
        font=("Arial", 14),
        justify="center"
    )
    numero2.pack(pady=2)

    # Resultado
    tk.Label(
        ventana,
        text="Resultado"
    ).pack(pady=3)

    resultado = tk.Entry(
        ventana,
        font=("Arial", 14),
        justify="center"
    )
    resultado.pack(pady=2)

    # Entrada seleccionada
    entrada_actual = [numero1]

    def seleccionar_numero1(event):
        entrada_actual[0] = numero1

    def seleccionar_numero2(event):
        entrada_actual[0] = numero2

    numero1.bind("<Button-1>", seleccionar_numero1)
    numero2.bind("<Button-1>", seleccionar_numero2)

    # Escribir números
    def poner_numero(numero):
        entrada_actual[0].insert(tk.END, numero)

    # Borrar
    def borrar():
        entrada_actual[0].delete(0, tk.END)

    # Limpiar
    def limpiar():
        numero1.delete(0, tk.END)
        numero2.delete(0, tk.END)
        resultado.delete(0, tk.END)

    # Calcular
    def calcular():
        try:
            n1 = float(numero1.get())
            n2 = float(numero2.get())

            total = n1 - n2

            resultado.delete(0, tk.END)
            resultado.insert(0, total)

        except ValueError:
            messagebox.showerror(
                "Error",
                "Debe ingresar los dos números."
            )

    # Teclado numérico
    teclado = tk.Frame(ventana)
    teclado.pack(pady=5)

    botones = [
        "7", "8", "9",
        "4", "5", "6",
        "1", "2", "3",
        "0", "."
    ]

    for i, numero in enumerate(botones):

        fila = i // 3
        columna = i % 3

        tk.Button(
            teclado,
            text=numero,
            width=5,
            height=1,
            font=("Arial", 12),
            command=lambda n=numero: poner_numero(n)
        ).grid(
            row=fila,
            column=columna,
            padx=3,
            pady=3
        )

    # Botón BORRAR
    tk.Button(
        teclado,
        text="BORRAR",
        width=5,
        height=1,
        font=("Arial", 9),
        command=borrar
    ).grid(
        row=3,
        column=2,
        padx=3,
        pady=3
    )

    # Botón CALCULAR
    tk.Button(
        ventana,
        text="CALCULAR",
        width=20,
        height=1,
        font=("Arial", 11, "bold"),
        command=calcular
    ).pack(pady=4)

    # Botón LIMPIAR
    tk.Button(
        ventana,
        text="LIMPIAR",
        width=20,
        height=1,
        font=("Arial", 10),
        command=limpiar
    ).pack(pady=3)

    # Botón VOLVER
    tk.Button(
        ventana,
        text="VOLVER",
        width=20,
        height=1,
        font=("Arial", 10),
        command=ventana.destroy
    ).pack(pady=3)
