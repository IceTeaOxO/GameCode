## pip install paddleocr
## pip install pillow
##
import logging
import time
import cv2
from paddleocr import PaddleOCR, draw_ocr
from PIL import ImageGrab
import pyautogui
import numpy as np
import random

# 關閉 PaddleOCR 的 DEBUG 訊息
logging.getLogger("ppocr").setLevel(logging.WARNING)

def show_screen(a,b,width, height):
    while True:
        # 擷取螢幕畫面
        screenshot = ImageGrab.grab(bbox=(a, b, width, height))
        frame_np = np.array(screenshot)
        
        # 顯示畫面
        cv2.imshow("Screen", cv2.cvtColor(frame_np, cv2.COLOR_BGR2RGB))
        
        # 按下 'q' 鍵退出迴圈
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 關閉 OpenCV 視窗
    cv2.destroyAllWindows()

# 顯示螢幕畫面
# show_screen(800,500,1100,700)

def fishing():
    # 初始化 PaddleOCR
    ocr = PaddleOCR(use_angle_cls=True, lang='ch')

    # 設定搜尋的文字
    target_text = "快拉"

    while True:
        # 擷取 Minecraft 畫面
        screenshot = ImageGrab.grab(bbox=(800, 500, 1100, 700))  # 請調整座標以符合你的螢幕解析度
        screenshot_np = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        # 進行文字辨識
        result = ocr.ocr(screenshot_np)
        # 搜尋目標文字
        for line in result:
            try:
                for word_info in line:
                    word = word_info[-1]
                    if target_text in word[0]:
                        pyautogui.click(button='right', clicks=1)
                        # 如果辨識結果有目標文字，執行滑鼠右鍵點擊動作
                        # print(f"找到目標文字: {target_text}")
                        # pyautogui.click(button='right', clicks=1)
            except:
                pass
        # 每秒檢查一次
        time.sleep(0.18+0.1*random.random())
fishing()

