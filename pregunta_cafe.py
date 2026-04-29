import flet as ft
import random


def main(page: ft.Page):
    page.title = "Vamos por un café el miércoles??"
    page.window.width = 400
    page.window.height = 300
    page.window.resizable = False

    mensaje = ft.Text(
        "",
        size=18,
        weight=ft.FontWeight.BOLD
    )

    def mover_boton_no(e):
        btn_no.top = random.randint(50, 200)
        btn_no.left = random.randint(20, 280)
        page.update()

    def mostrar_respuesta(e):
        mensaje.value = "Tenia el presentimiento que dirias que si jsjs"
        page.update()

    btn_si = ft.Button(
        "Sí",
        on_click=mostrar_respuesta,
        width=100
    )

    btn_no = ft.Button(
        "No",
        on_hover=mover_boton_no,
        width=100
    )

    btn_si.top = 100
    btn_si.left = 50

    btn_no.top = 100
    btn_no.left = 200

    stack = ft.Stack(
        controls=[btn_si, btn_no],
        width=400,
        height=220
    )

    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    "¿Quieres ir por un café conmigo?",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                ),
                stack,
                mensaje
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )


ft.app(
    target=main,
    host="0.0.0.0",
    port=8000
)
