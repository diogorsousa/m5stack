# M5Stack Paper S3 Touch Sample Code (UIFlow2)
# A simple counter app with +1, -1 and reset buttons to demonstrate touch functionality.

import os, sys, io
import M5
from M5 import *



labelCount = None
rectPlus1 = None
rectMinus1 = None
rectReset = None
label0 = None
label1 = None
label2 = None
title0 = None


x1 = None
x2 = None
y1 = None
y2 = None
amount = None
counter = None
previousTouchCount = None

def checkTouchedArea(x1, x2, y1, y2):
  global amount, counter, previousTouchCount, labelCount, rectPlus1, rectMinus1, rectReset, label0, label1, label2, title0
  if (M5.Touch.getX()) >= x1 and (M5.Touch.getX()) <= x2 and (M5.Touch.getY()) >= y1 and (M5.Touch.getY()) <= y2:
    return True
  return False

# returns true when a touch is released
def hasTouched():
  global x1, x2, y1, y2, amount, counter, previousTouchCount, labelCount, rectPlus1, rectMinus1, rectReset, label0, label1, label2, title0
  if (M5.Touch.getCount()) > 0:
    previousTouchCount = 1
  elif previousTouchCount == 1:
    previousTouchCount = 0
    if previousTouchCount == 0:
      return True
  return False


def changeCounterBy(amount):
  global x1, x2, y1, y2, counter, previousTouchCount, labelCount, rectPlus1, rectMinus1, rectReset, label0, label1, label2, title0
  counter = (counter if isinstance(counter, (int, float)) else 0) + amount
  labelCount.setText(str(str(counter)))

def resetCounter():
  global x1, x2, y1, y2, amount, counter, previousTouchCount, labelCount, rectPlus1, rectMinus1, rectReset, label0, label1, label2, title0
  counter = 0
  labelCount.setText(str(str(counter)))

def setup():
  global labelCount, rectPlus1, rectMinus1, rectReset, label0, label1, label2, title0, counter, previousTouchCount, amount, x1, x2, y2, y1

  M5.begin()
  Widgets.fillScreen(0xeeeeee)
  labelCount = Widgets.Label("0", 241, 343, 1.0, 0x000000, 0xeeeeee, Widgets.FONTS.DejaVu72)
  rectPlus1 = Widgets.Rectangle(21, 818, 230, 112, 0x555555, 0xffffff)
  rectMinus1 = Widgets.Rectangle(284, 818, 230, 112, 0x555555, 0xffffff)
  rectReset = Widgets.Rectangle(21, 673, 495, 112, 0x555555, 0xffffff)
  label0 = Widgets.Label("Reset", 209, 710, 1.0, 0x000000, 0xffffff, Widgets.FONTS.DejaVu40)
  label1 = Widgets.Label("+1", 101, 855, 1.0, 0x000000, 0xffffff, Widgets.FONTS.DejaVu40)
  label2 = Widgets.Label("-1", 378, 855, 1.0, 0x000000, 0xffffff, Widgets.FONTS.DejaVu40)
  title0 = Widgets.Title("Counter", 8, 0xffffff, 0x000000, Widgets.FONTS.DejaVu40)

  counter = 0


def loop():
  global labelCount, rectPlus1, rectMinus1, rectReset, label0, label1, label2, title0, counter, previousTouchCount, amount, x1, x2, y2, y1
  M5.update()
  if hasTouched():
    if checkTouchedArea(21, 251, 818, 930):
      changeCounterBy(1)
    if checkTouchedArea(284, 514, 818, 930):
      changeCounterBy(-1)
    if checkTouchedArea(21, 516, 673, 785):
      resetCounter()


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
