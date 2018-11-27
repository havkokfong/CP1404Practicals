
USERNAME = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole',
'InterpreterInterface', 'StartServer', 'bob']

def main():
    name = str(input("Please enter your name: "))
    if name in USERNAME:
       print("Access granted")
    else:
       print("Access denied")
main()