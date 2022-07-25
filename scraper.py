import json
import os

if __name__ == '__main__':
    path = '/sdcard/Android/data/com.UNCWMRL.SeaTurtleSimulation/files/Log'
    valid_choice = False
    while not valid_choice:
        device_name = input('Please input a device id: ')
        if os.path.isdir(f'Logs/{device_name}'):
            choice = input('WARNING the device name you entered already exists.\nWould you like to continue? (Y/N): ')
            if 'y' in choice.lower():
                valid_choice = True
            else:
                valid_choice = False
        else:
            valid_choice = True
    if not os.path.isdir('Logs'):
        os.mkdir('Logs')
    os.system(f'adb pull "{path}" "{os.getcwd()}\\Logs\\{device_name}')

