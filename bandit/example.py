import subprocess

def run_command(user_input):
    # Vulnerable to command injection
    subprocess.call("echo " + user_input, shell=True)

if __name__ == "__main__":
    user_input = input("Please enter a command: ")
    run_command(user_input)

