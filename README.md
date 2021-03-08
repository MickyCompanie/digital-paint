# digital-paint

The goal of this little program is to paint with a webcam and a marker

## How does it work ?

By isolating certain colors of the images that the webcam captures I create a mask that make me able to isolate certains objects (in this case markers). 
Once i "track" the desired object, I just paint circles of a certain color from the top of it in the image that the webcam is returning

To isolate the color that i need specifically i use [this little program](./colorPicker.py)

## tech used
 
 - python
 - openCV
 
## what it look like :

## What i want to improve:

this is obviouslt just a v1 and in the future i would like to improve it like this:

- creating a gui
- make the user able to paint only when he push on a certain key
- make the user able to save its paints