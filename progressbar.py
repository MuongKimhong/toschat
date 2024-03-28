import subprocess

# Command to execute
command = ["git", "add", "."]

# Execute the command and capture its output
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Wait for the command to complete and capture its output
stdout, stderr = process.communicate()

# Decode the output from bytes to string
stdout_str = stdout.decode("utf-8")
stderr_str = stderr.decode("utf-8")

# Print the output (if any)
if stdout_str:
	print("Standard Output:")
	print(stdout_str)
	print(type(stdout_str))

# Print the error (if any)
if stderr_str:
    print("Standard Error:")
    print(stderr_str)

# Get the exit code of the process
exit_code = process.returncode
print("Exit Code:", exit_code)
