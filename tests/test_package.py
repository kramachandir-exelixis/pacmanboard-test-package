from pacmanboard_test_package import __version__, greet


def test_greet_uses_default_name():
    assert greet() == "Hello, Pacman Board!"


def test_greet_uses_provided_name():
    assert greet("tester") == "Hello, tester!"


def test_version_is_set():
    assert __version__ == "0.1.0"
