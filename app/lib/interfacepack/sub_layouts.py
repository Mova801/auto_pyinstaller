import PySimpleGUI as sg


def build_image_button(image: str, size: tuple[str, str], color: str, key: str) -> None:
    return sg.Button(
        image_source=image,
        image_size=size,
        key=key,
        border_width=1,
        mouseover_colors=color,
    )


def build_resource_usage_interface(bar_size: tuple[str, str], percenrage_range: int):
    return [
        [
            sg.ProgressBar(
                percenrage_range,
                orientation="h",
                size=(bar_size),
                key="-CBAR-",
                bar_color=("#00ce22", None),
            ),
            sg.Text("CPU: ", key="-CTEXT-"),
        ],
        [
            sg.ProgressBar(
                percenrage_range,
                orientation="h",
                size=(bar_size),
                key="-RBAR-",
                bar_color=("#3A91FB", None),
            ),
            sg.Text("Memory: ", key="-RTEXT-"),
        ],
    ]


def build_title_row_interface(logo: str, image_size: tuple[str, str], title: str) -> list[list]:
    return [
        [
            sg.Image(source=logo, size=image_size, key="-LOGO-"),
            sg.Text(title, font="bold 14", key="-APP_NAME-"),
        ]
    ]

