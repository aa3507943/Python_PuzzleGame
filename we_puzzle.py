# -*- coding: utf-8 -*-
import threading
import random
import pygame
import cv2
import os
import time
import multiTask_test
import tkinter
from tkinter import messagebox


# 初始化
x = 1100
y = 600
pygame.init()
# 窗口標題
pygame.display.set_caption('Play Game - We Puzzle !')
appIcon = pygame.image.load("./src/appIcon.ico")
pygame.display.set_icon(appIcon)
# 窗口大小
s = pygame.display.set_mode((x, y))
#然後進行遊戲初始化，設置標題和遊戲界面的大小。
imageList = os.listdir("./image/")

#音樂處理
music = os.listdir("./music/")
pygame.mixer.init()
pygame.time.delay(1000)
pygame.mixer.music.load("./music/" + music[0])
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)


print(imageList[0])
# image = ["./image/soojin.png", "./image/jiyoon.jpg", "./image/monday.jpg", "./image/soeun.jpg", "./image/jaehee.jpg", "./image/jihan.jpg", "./image/zoa.jpg"]
a = random.randrange(0, len(imageList))
# print(image[a])
image2 = cv2.imread("./image/"+imageList[a])
image2 = cv2.resize(image2, (498, 498))
cv2.imwrite('example.jpg', image2)
# 繪圖地圖
imgMap = [
 [0, 1, 2],
 [3, 4, 5],
 [6, 7, 8]
]
# 判斷勝利的地圖
winMap = [
 [0, 1, 2],
 [3, 4, 5],
 [6, 7, 8]
]
#繪製初始地圖並且設置勝利地圖，這裏使用數組的方式進行處理。


#結束訊息處理

def show_result(time_list):
    tk = tkinter.Tk()
    tk.withdraw()
    messagebox.showinfo("提示", "成功！您花了 " + time_list[0] + time_list[1]  + " 時 " + time_list[2] + time_list[3]  + " 分 " + time_list[4] + time_list[5]  + " 秒 ")

# 遊戲的單擊事件
def click(x, y, map):
    if y - 1 >= 0 and map[y - 1][x] == 8:
        map[y][x], map[y - 1][x] = map[y - 1][x], map[y][x]
    elif y + 1 <= 2 and map[y + 1][x] == 8:
        map[y][x], map[y + 1][x] = map[y + 1][x], map[y][x]
    elif x - 1 >= 0 and map[y][x - 1] == 8:
        map[y][x], map[y][x - 1] = map[y][x - 1], map[y][x]
    elif x + 1 <= 2 and map[y][x + 1] == 8:
        map[y][x], map[y][x + 1] = map[y][x + 1], map[y][x]
#這裏需要設置遊戲的點擊事件，簡單的說就是鼠標點擊圖片進行移動的邏輯，主要的邏輯代碼就是做了if判斷，比較容易理解。

# 打亂地圖
def randMap(map):
    for i in range(1000):
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        click(x, y, map)
#使用隨機數的方式將地圖進行打亂。




# 加載圖片
img = pygame.image.load("example.jpg")
# 隨機地圖
randMap(imgMap)
start_time = time.time()
# 遊戲主循環
while imgMap != winMap:
 # 延時32毫秒,相當於FPS=30
    pygame.time.delay(60)
    font = pygame.font.SysFont('arial', 50)
    time_list = multiTask_test.timer(start_time)
    text = font.render(time_list[0] + time_list[1] + " : " + time_list[2] + time_list[3] + " : " + time_list[4] + time_list[5], True, (255, 255, 255), (255, 192, 203) )
    textRect = text.get_rect()
    textRect.center = (550, 560)

    s.fill((0, 0, 0))
        # 繪圖
    for y in range(3):
        for x in range(3):
                i = imgMap[y][x]
                if i == 8: # 8號圖塊不用繪製
                    continue
                dx = (i % 3) * 166 # 計算繪圖偏移量
                dy = (int(i / 3)) * 166
                s.blit(img, (x * 166 + 50, y * 166 + 30 ), (dx, dy, 166, 166))
                # 畫參考圖片
                s.blit(img, (550, 30))
                s.blit(text, textRect)
            # 刷新界面
                # pygame.display.flip()
    for event in pygame.event.get():
 # 窗口的關閉事件
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            if pygame.mouse.get_pressed() == (1, 0, 0): 
                mx, my = pygame.mouse.get_pos() 
                if mx < 498 and my < 498: 
                    x = int(mx / 166) 
                    y = int(my / 166)
                    click(x, y, imgMap)           
            if imgMap == winMap:
                break
                
    pygame.display.update()   
    

pygame.display.update()
pygame.display.quit()
time_list = multiTask_test.timer(start_time)
show_result(time_list)
    # time_list = multiTask_test.timer(start_time)
    # font = pygame.font.Font("./font/NotoSansTC-Black.otf", 60)
    # text = font.render("成功！您花了 " + str(time_list[0]) + " 時 " + str(time_list[1]) + " 分 " + str(time_list[2]) + " 秒 ", True, (255, 255, 255), (255,182,193))
    # textRect = text.get_rect()
    # textRect.center = (600, 250)
    # s.blit(text, textRect)  


#加載我們的照片，並且將地圖進行隨機打亂。設置遊戲的主循環，獲取鼠標的座標，判斷鼠標是否在操作範圍內，計算鼠標點擊的圖塊，判斷操作是否成功。

 # 背景色填充成綠色
        