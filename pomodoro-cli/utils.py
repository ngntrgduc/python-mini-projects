import subprocess

def clear_console() -> None:
    """Clear the console"""
    try:
        # For Windows
        subprocess.run('cls', shell=True, check=True)
    except subprocess.CalledProcessError:
        # For Unix-like
        subprocess.run('clear', shell=True, check=True)
    except Exception as error:
        print(error)