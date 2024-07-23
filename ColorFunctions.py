import winreg
                        #This function colors the player's cells green, and, in theory, it should still blink rarely.
def PColorIN(TextStr):  #Эта функция окрашивает клетку игрока в зелёный цвет и по идее он должен ещё редко мигать

    TextStr = f"\033[5m\033[32m{TextStr}\033[0m"

    return TextStr

#This functions must add a valur with key in Windows Registry at "HKEY_CURRENT_USER\\Console\\" to add the ANSI-CODE in Console (cmd)
#And Leha would remember to delit  the key fail after the finish 
#informention was taken from https://ss64.com/nt/syntax-ansi.html

#Fail Name "VirtualTerminalLevel"
path = winreg.HKEY_CURRENT_USER
console = winreg.CreateKey(path, r"Console\\")
def CreateFail():
    winreg.SetValueEx(console,"VirtualTerminalLevel", 0, winreg.REG_DWORD,0x00000001)

def DeleteFail():
    winreg.DeleteValue(console,"VirtualTerminalLevel")