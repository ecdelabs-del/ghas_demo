import os 

# Vulnerability: Directly using user-controlled input to execute a command.
command = input("Enter a command to execute: ")
os.system(command)
