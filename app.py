import flet as ft

def main(page: ft.Page):
    page.title = "Rider Tracker"
    page.bgcolor = ft.colors.BLACK
    page.padding = 10
    
    # Definiamo lo stile delle celle
    def create_tile(label, value, is_red=False):
        return ft.Container(
            content=ft.Column([
                ft.Text(label, size=10, color=ft.colors.GREY_500, weight=ft.FontWeight.BOLD),
                ft.Text(value, size=18, color=ft.colors.RED_ACCENT if is_red else ft.colors.CYAN_ACCENT, weight=ft.FontWeight.BOLD),
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            bgcolor="#121212",
            border=ft.border.all(1, "#282828"),
            border_radius=10,
            padding=15,
            expand=True
        )

    # Creiamo la griglia 3x3 rigida
    grid = ft.Column([
        ft.Row([
            create_tile("LORDO", "€0.00"),
            create_tile("NETTO", "€0.00", is_red=True),
            create_tile("ORE", "0.0"),
        ], spacing=5),
        ft.Row([
            create_tile("LITRI", "0.0L"),
            create_tile("KM/L", "0.0"),
            create_tile("BENZINA", "€0.00"),
        ], spacing=5),
        ft.Row([
            create_tile("DISTANZA", "0 KM"),
            create_tile("MEDIA €", "€0.00"),
            create_tile("CONSEGNE", "0"),
        ], spacing=5),
    ], spacing=5)

    page.add(grid)

ft.app(target=main)
