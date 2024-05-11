""" Mouse jiggler is a program that simulates the movement of a computer mouse """

# https://medium.com/@jacobnarayan/make-a-mouse-wiggler-program-in-python-in-3-minutes-6f3f0e1d3cba
# https://www.shedloadofcode.com/blog/creating-a-screen-and-mouse-jiggler-with-python

# pyautogui is a cross-platform GUI automation library for Python that can simulate mouse clicks, keyboard presses, and even take screenshots
# https://pyautogui.readthedocs.io/en/latest/index.html


import time
import pyautogui


screen_size = pyautogui.size()

# Move mouse cursor around the square of size "n_pxls"
# with the speed of "duration" seconds
# and interval of "interval" seconds
def move_mouse(n_pxls=100, duration=1, interval=4):
	screen_center = (screen_size[0]/2, screen_size[1]/2)

	pyautogui.moveTo(screen_center[0] - n_pxls/2, screen_center[1] - n_pxls/2, duration) # move cursor to center with specified offset
	pyautogui.move(n_pxls, 0, duration) # move right n_pxls
	pyautogui.move(0, n_pxls, duration) # move down n_pxls
	pyautogui.move(-n_pxls, 0, duration) # move left n_pxls
	pyautogui.move(0, -n_pxls, duration) # move up n_pxls

	time.sleep(interval) # interval in seconds before a new loop

# click mouse
def click_mouse():
	pyautogui.click()

# main function
def jiglle():
	print("Mouse jiggler has been started...")
	print("Press Ctrl+C to quit.")

	try:
		while True:
			move_mouse()
			# click_mouse()
	except KeyboardInterrupt:
		print("Mouse jiggler has been stopped.")


if __name__ == "__main__":
	jiglle()
