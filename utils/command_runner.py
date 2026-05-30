import subprocess

def run_linux_command(command_list: list) -> str:
    """
    Safely executes a predefined Linux command using subprocess.
    """
    try:
        # shell=False security ke liye zaroori hai taake koi extra command inject na kar sakay
        result = subprocess.run(
            command_list, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True, 
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Command failed: {e.stderr.strip()}")
    except FileNotFoundError:
        raise RuntimeError("Command not found. Make sure you are running on a Linux environment.")