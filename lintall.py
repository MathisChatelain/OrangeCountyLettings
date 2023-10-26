import subprocess


def run_flake8():
    print("Running Flake8...")
    subprocess.run(["flake8", "."], check=False)


def run_black():
    print("Running Black...")
    subprocess.run(["black", "."], check=False)


def run_isort():
    print("Running isort...")
    subprocess.run(["isort", "."], check=False)


if __name__ == "__main__":
    run_flake8()
    run_black()
    run_isort()
