# Broken Display Simulator

Simulates broken display.

![Broken Display Simulator](https://raw.githubusercontent.com/34j/broken-display-simulator/main/docs/_static/example.png)

## Installation

Install this via pip (or your favourite package manager):

```shell
pip install broken-display-simulator
```

## Usage

The `bdsim` command below will cause annoying vertical lines to appear on the screen.

```shell
bdsim
```

Color and orientation/type can also be specified.

```shell
bdsim horizontal green
```

```shell
bdsim dot red -x 100 -y 100
```

```shell
> bdsim -h
Usage: bdsim [OPTIONS] [[vertical|horizontal|dot|v|h|d]] [COLOR]

Options:
  -h, --help       Show this message and exit.
  -x, --x INTEGER  X coordinate
  -y, --y INTEGER  Y coordinate
```
