import pyautogui
print(' Ctrl-C para encerrar.')
try:
   while True:
         x, y = pyautogui.position()
         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
         print(positionStr, end='')
         print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('End')

# import pyautogui as pag

# pag.position()
# print('pag.position()')
