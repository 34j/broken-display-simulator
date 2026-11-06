from click.testing import CliRunner

from broken_display_simulator.__main__ import main


def test_main_help() -> None:
    result = CliRunner().invoke(main, ["--help"])

    assert result.exit_code == 0
    assert "Usage: main" in result.output
    assert "X coordinate" in result.output
