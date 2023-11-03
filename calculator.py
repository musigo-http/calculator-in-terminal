import subprocess, os
os.system('clear')
script_shell = "calculator_title.sh"
subprocess.run(["bash", script_shell])
print("\033[91mprint help\033[0m")
infini = 10
while(infini >= 0):
    bjr = input(">>>")
    if(bjr == "exit"):
        os.system("clear")
        break
    if(bjr == "clear"):
        sh = "clear.sh"
        subprocess.run(["bash", sh])
        break
    if(bjr == "help"):
        print("print \033[91mhelp\033[0m for help\nprint \033[91mexit\033[0m for exit\nprint \033[91mclear\033[0m for clear the terminal\n\033[91mgood luck in the calculator! (;\033[0m")
    calcul = eval(bjr)
    print(calcul)