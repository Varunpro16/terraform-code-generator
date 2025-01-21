import subprocess

# Command to execute
command = ["ls", "-l"]

# Run the command
result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Capture and print the output
if result.returncode == 0:
    print("Command Output:")
    print(result.stdout)
else:
    print("Error:")
    print(result.stderr)
