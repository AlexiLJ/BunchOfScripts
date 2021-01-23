import os

def get_temperature():
    """
    Script for measuring RaspberryPi CPU and GPU temperatures
    Run in bash with "watch python3 temp_script.py" 
    """
    GPU = os.popen('vcgencmd measure_temp').readline()[5:-3]
    CPU = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3
    os.system(f'echo CPU temperature: {CPU} ' + u'\xb0' + "C")
    print(f'GPU temperature: {GPU} ' + u'\xb0' + "C")


get_temperature()