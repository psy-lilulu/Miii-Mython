import LanguageMi
import glob
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

print("Version 0.01")

def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText("Mii!", font='big'),
            int(screen.height / 2 - 4)),
        Cycle(
            screen,
            FigletText("!", font='big'),
            int(screen.height / 2 + 3)),
        Stars(screen, 200)
    ]
    screen.play([Scene(effects, 500)])

while True:
    action = input('to code in Mii - Define(run/create/edit): ')
    if action.lower() == 'run':
       my_files = glob.glob('*.my')
       filename = input('Enter the name of the .my script to run: ')
       if filename in my_files:
           LanguageMi.run_script(filename)
       else:
           print(f'Script {filename} not found.')
    elif action.lower() == 'create':
        filename = input('Enter the name for the new script (will be created if it does not exist): ')
        with open(filename, 'w+') as file:
            print(f'Start writing your script. Write "END" on a new line when you are done.\n')
            while True:
                line = input()
                if line == 'END':
                    break
                file.write(line + '\n')
        print(f'Script {filename} created successfully.')
    elif action.lower() == 'edit':
        my_files = glob.glob('*.my')
        print('Available .my files:', my_files)
        filename = input('Enter the name of the .my script to edit: ')
        if filename in my_files:
            with open(filename, 'a+') as file:
                print(f'Start editing your script. Write "END" on a new line when you are done.\n')
                while True:
                    line = input()
                    if line == 'END':
                        break
                    file.write(line + '\n')
            print(f'Script {filename} edited successfully.')
        else:
            print(f'Script {filename} not found.')
    else:
        print('Invalid action. Please enter "run", "create", or "edit".')
