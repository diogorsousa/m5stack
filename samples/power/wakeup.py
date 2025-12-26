import os, sys, io
import M5
from M5 import *



labelText = None
rectReset = None
label0 = None
title0 = None


x1 = None
x2 = None
y1 = None
y2 = None
previousTouchCount = None

# Describe this function...
def checkTouchedArea(x1, x2, y1, y2):
  global previousTouchCount, labelText, rectReset, label0, title0
  if (M5.Touch.getX()) >= x1 and (M5.Touch.getX()) <= x2 and (M5.Touch.getY()) >= y1 and (M5.Touch.getY()) <= y2:
    return True
  return False

# Describe this function...
def hasTouched():
  global x1, x2, y1, y2, previousTouchCount, labelText, rectReset, label0, title0
  if (M5.Touch.getCount()) > 0:
    previousTouchCount = 1
  elif previousTouchCount == 1:
    previousTouchCount = 0
    if previousTouchCount == 0:
      return True
  return False


def setup():
  global labelText, rectReset, label0, title0, previousTouchCount, x1, x2, y1, y2

  M5.begin()
  Widgets.fillScreen(0xeeeeee)
  labelText = Widgets.Label("Off", 213, 341, 1.0, 0x000000, 0xeeeeee, Widgets.FONTS.DejaVu72)
  rectReset = Widgets.Rectangle(21, 673, 495, 112, 0x555555, 0xffffff)
  label0 = Widgets.Label("Turn off for 10s", 110, 708, 1.0, 0x000000, 0xffffff, Widgets.FONTS.DejaVu40)
  title0 = Widgets.Title("Deep sleep test", 8, 0xffffff, 0x000000, Widgets.FONTS.DejaVu40)



def loop():
  global labelText, rectReset, label0, title0, previousTouchCount, x1, x2, y1, y2
  M5.update()
  labelText.setText(str('On'))
  if hasTouched():
    if checkTouchedArea(21, 516, 673, 785):
      labelText.setText(str('Off'))
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
