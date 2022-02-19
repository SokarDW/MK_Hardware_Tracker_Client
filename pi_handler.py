from gpiozero import CPUTemperature
import subprocess


class Pi_handler:
    def __init__(self) -> None:
        pass

    def __comandline_return__(command:str):
        subproc = subprocess.Popen(command, shell = True, stdout=subprocess.PIPE)
        return subproc.stdout.read().decode()

    def cpu_temp():
        cpu_temp = CPUTemperature()
        return cpu_temp.temperature
    
    def cpu_temp_alt():
        subproc = subprocess.Popen('vcgencmd measure_temp', shell = True, stdout=subprocess.PIPE) #vcgencmd measure_temp
        return subproc.stdout.read().decode()

    def hostname():
        return Pi_handler.__comandline_return__('hostname')

#print(Pi_handler.cpu_temp())
#print(Pi_handler.cpu_temp_alt())
print(Pi_handler.hostname())