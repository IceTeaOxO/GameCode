# from pynput import keyboard

# def on_press(key):
#     try:
#         # 監聽所有按鍵，這裡只是簡單地印出按下的按鍵
#         print('Key {} pressed.'.format(key.char))
#     except AttributeError:
#         # 如果是特殊按鍵（非字母、數字等），則印出特殊按鍵的名稱
#         print('Special key {} pressed.'.format(key))

# def on_release(key):
#     # 如果按下Esc鍵，則停止監聽
#     if key == keyboard.Key.esc:
#         print('Exiting...')
#         return False

# # 創建鍵盤監聽器
# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()
from pynput import keyboard, mouse
import pyautogui
import time
# 創建滑鼠控制物件

mouse_controller = mouse.Controller()

# 設定滑鼠每次移動的距離（像素）
mouse_move_distance = 15
def on_press(key):
    try:
        if key.char == "'":  # 偵測到 Enter 鍵被按下
            # 在目前滑鼠位置模擬左鍵點擊
            mouse_controller.click(mouse.Button.left)
        if key.char == "\\":  # 偵測到 Enter 鍵被按下
            # 在目前滑鼠位置模擬左鍵點擊
            mouse_controller.click(mouse.Button.right)
        if key.char == 'w':
            # 获取当前鼠标位置
            current_x, current_y = pyautogui.position()
            # 模拟鼠标向上移动
            pyautogui.moveTo(current_x, current_y - mouse_move_distance)
            # 可以添加延迟，以控制移动速度
            # time.sleep(0.1)
        if key.char == 'a':
            current_x, current_y = pyautogui.position()
            pyautogui.moveTo(current_x - mouse_move_distance, current_y)
            # time.sleep(0.1)
        if key.char == 's':
            current_x, current_y = pyautogui.position()
            pyautogui.moveTo(current_x, current_y + mouse_move_distance)
            # time.sleep(0.1)
        if key.char == 'd':
            current_x, current_y = pyautogui.position()
            pyautogui.moveTo(current_x + mouse_move_distance, current_y)
            # time.sleep(0.1)

    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        print('Exiting...')
        return False

# 創建鍵盤監聽器
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


