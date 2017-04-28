# import modules
import SimpleCV

"""This program capture image from laptop camera.
And then show in a PyGame's window the image.
"""
# call camera function
cam = SimpleCV.Camera()
# get image from cam
img = cam.getImage()
# save image
img.save("/home/marco/SimpleCVExcercise/imgcapcam.png")
# show by pygame
img.show()

