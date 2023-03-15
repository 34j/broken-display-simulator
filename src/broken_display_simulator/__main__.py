from __future__ import annotations

import random
from typing import Literal

import click
import PySimpleGUI as sg


def _show(
    type_: Literal["vertical", "horizontal", "dot"],
    x: int = 0,
    y: int = 0,
    color: str = "white",
) -> None:
    width, height = sg.Window.get_screen_size()
    if type_ == "vertical":
        size = (1, height)
    elif type_ == "horizontal":
        size = (width, 1)
    elif type_ == "dot":
        size = (1, 1)
    else:
        raise ValueError(f"Invalid type: {type_}")
    layout = [[sg.Image(background_color=color, size=size, pad=(0, 0))]]
    win = sg.Window(
        "Broken Display Simulator",
        layout,
        no_titlebar=True,
        keep_on_top=True,
        location=(x, y),
        margins=(0, 0),
    )
    while True:
        try:
            event, values = win.read(timeout=0)
            if event in (sg.WIN_CLOSED, "Exit"):
                break
        except Exception:
            break
    win.close()


@click.command()
@click.help_option("-h", "--help")
@click.argument(
    "type_",
    type=click.Choice(["vertical", "horizontal", "dot", "v", "h", "d"]),
    default="vertical",
    required=False,
)
@click.option("-x", "--x", type=int, default=None, help="X coordinate")
@click.option("-y", "--y", type=int, default=None, help="Y coordinate")
@click.argument("color", type=str, default="white", required=False)
def main(
    type_: Literal["vertical", "horizontal", "dot", "v", "h", "d"] = "vertical",
    x: int | None = 0,
    y: int | None = 0,
    color: str = "white",
) -> None:
    # abbreviations
    if type_ == "v":
        type_ = "vertical"
    elif type_ == "h":
        type_ = "horizontal"
    elif type_ == "d":
        type_ = "dot"

    # randomize coordinates
    if x is None:
        if type_ == "vertical":
            x = random.randint(0, sg.Window.get_screen_size()[0])  # nosec
        else:
            x = 0
    if y is None:
        if type_ == "horizontal":
            y = random.randint(0, sg.Window.get_screen_size()[1])  # nosec
        else:
            y = 0

    click.echo(f"Showing window... (type={type_}, x={x}, y={y}, color={color})")

    # show window
    _show(type_, x, y, color)


main()
