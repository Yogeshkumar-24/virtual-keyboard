# virtual-keyboard
**Hand Gesture Keyboard using OpenCV and Pygame**

This Python script allows you to control a virtual keyboard using hand gestures captured through your webcam. It utilizes the OpenCV library for computer vision, the Pygame library to create the virtual keyboard, and the pynput library to simulate keyboard input outside the Integrated Development Environment (IDE).

**Requirements:**
- Python (3.x recommended)
- OpenCV (cv2)
- Pygame
- pynput

**Installation:**
Make sure you have Python installed on your system. You can install the required libraries using `pip`:

```bash
pip install opencv-python pygame pynput
```

**How to Use:**
1. Connect a webcam to your computer or use the inbuilt web cam by specifying the parameter as 0.
2. Run the script.
3. A window will open showing your webcam feed with a virtual keyboard overlay.
4. Place your hand in front of the camera.
5. Use your index finger to press the keys on the virtual keyboard.
6. To type a letter, bring your index finger close to the corresponding key and hold it for a moment. The letter will be typed.
7. To type a space, bring your index finger close to the "Space" key and hold it for a moment.
8. To delete the last character, bring your index finger close to the "<---" (Backspace) key and hold it for a moment.
9. You can also open a Notepad and can type using this virtual keyboard. pynput is used for such purpose.
**Note:**
- The keyboard supports uppercase letters and some special characters.
- The script is designed for a resolution of 1280x720, so make sure your webcam supports this resolution or adjust the code accordingly.
- You can modify the `keys` list to customize the virtual keyboard layout.

Enjoy typing with your hand gestures using this interactive virtual keyboard!
