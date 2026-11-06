# Broken Display Simulator

<p align="center">
  <a href="https://github.com/34j/broken-display-simulator/actions/workflows/ci.yml?query=branch%3Amain">
    <img src="https://img.shields.io/github/actions/workflow/status/34j/broken-display-simulator/ci.yml?branch=main&label=CI&logo=github&style=flat-square" alt="CI Status" >
  </a>
  <a href="https://broken-display-simulator.readthedocs.io">
    <img src="https://img.shields.io/readthedocs/broken-display-simulator.svg?logo=read-the-docs&logoColor=fff&style=flat-square" alt="Documentation Status">
  </a>
</p>
<p align="center">
  <a href="https://codecov.io/gh/34j/broken-display-simulator">
    <img src="https://img.shields.io/codecov/c/github/34j/broken-display-simulator.svg?logo=codecov&logoColor=fff&style=flat-square" alt="Test coverage percentage">
  </a>
  <a href="https://github.com/astral-sh/uv">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json" alt="uv">
  </a>
  <a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff">
  </a>
  <a href="https://github.com/j178/prek">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/j178/prek/master/docs/assets/badge-v0.json" alt="prek">
  </a>
</p>
<p align="center">
  <a href="https://pypi.org/project/broken-display-simulator/">
    <img src="https://img.shields.io/pypi/v/broken-display-simulator.svg?logo=python&logoColor=fff&style=flat-square" alt="PyPI Version">
  </a>
  <img src="https://img.shields.io/pypi/pyversions/broken-display-simulator.svg?style=flat-square&logo=python&amp;logoColor=fff" alt="Supported Python versions">
  <img src="https://img.shields.io/pypi/l/broken-display-simulator.svg?style=flat-square" alt="License">
</p>

---

**Documentation**: <a href="https://broken-display-simulator.readthedocs.io" target="_blank">https://broken-display-simulator.readthedocs.io </a>

**Source Code**: <a href="https://github.com/34j/broken-display-simulator" target="_blank">https://github.com/34j/broken-display-simulator </a>

---

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
