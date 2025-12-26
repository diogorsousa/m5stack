import os, sys, io
import M5
from M5 import *
import time



labelCount = None
rectPlus1 = None
label1 = None
title0 = None


x1 = None
x2 = None
y1 = None
y2 = None
previousTouchCount = None
counter = None

# TODO: apenas na transição para zero do touch count
def checkTouchedArea(x1, x2, y1, y2):
  global previousTouchCount, counter, labelCount, rectPlus1, label1, title0
  if (M5.Touch.getX()) >= x1 and (M5.Touch.getX()) <= x2 and (M5.Touch.getY()) >= y1 and (M5.Touch.getY()) <= y2:
    return True
  return False

# Describe this function...
def hasTouched():
  global x1, x2, y1, y2, previousTouchCount, counter, labelCount, rectPlus1, label1, title0
  if (M5.Touch.getCount()) > 0:
    previousTouchCount = 1
  elif previousTouchCount == 1:
    previousTouchCount = 0
    if previousTouchCount == 0:
      return True
  return False

# Describe this function...
def dosomething():
  global x1, x2, y1, y2, previousTouchCount, counter, labelCount, rectPlus1, label1, title0
  labelCount.setText(str('Off'))
  # E-ink refresh is slow, wait for it.
  time.sleep(2)


def setup():
  global labelCount, rectPlus1, label1, title0, previousTouchCount, counter, x1, x2, y1, y2

  M5.begin()
  Widgets.fillScreen(0xeeeeee)
  labelCount = Widgets.Label("On", 213, 343, 1.0, 0x000000, 0xeeeeee, Widgets.FONTS.DejaVu72)
  rectPlus1 = Widgets.Rectangle(20, 818, 494, 112, 0x555555, 0xffffff)
  label1 = Widgets.Label("timerSleep(10)", 111, 853, 1.0, 0x000000, 0xffffff, Widgets.FONTS.DejaVu40)
  title0 = Widgets.Title("Power Off Test", 8, 0xffffff, 0x000000, Widgets.FONTS.DejaVu40)

  counter = 0


def loop():
  global labelCount, rectPlus1, label1, title0, previousTouchCount, counter, x1, x2, y1, y2
  M5.update()
  if hasTouched():
    # +1
    if checkTouchedArea(21, 514, 818, 930):
      dosomething()
      Power.timerSleep(10)


if __name__ == '__main__':
  try:
    setup()
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")
