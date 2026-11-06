from __future__ import annotations

import secrets
from typing import Literal

import click
import FreeSimpleGUI as sg


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
            event, _ = win.read(timeout=0)
            if event in {sg.WIN_CLOSED, "Exit"}:
                break
        except Exception:  # noqa: BLE001  # GUI backends can fail while closing.
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
    """Show a broken display line or dot."""
    # abbreviations
    if type_ == "v":
        type_ = "vertical"
    elif type_ == "h":
        type_ = "horizontal"
    elif type_ == "d":
        type_ = "dot"

    # randomize coordinates
    if x is None:
        x = secrets.randbelow(sg.Window.get_screen_size()[0]) if type_ == "vertical" else 0
    if y is None:
        y = secrets.randbelow(sg.Window.get_screen_size()[1]) if type_ == "horizontal" else 0

    click.echo(f"Showing window... (type={type_}, x={x}, y={y}, color={color})")

    # show window
    _show(type_, x, y, color)


if __name__ == "__main__":
    main()
