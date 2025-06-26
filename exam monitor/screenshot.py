from PIL import ImageGrab

def capture_screenshot(output_file):
    img = ImageGrab.grab()
    img.save(output_file)
