from boxmaker.box import Box

APP_NAME = "box designer"
APP_VERSION = "2.1.0"
WEBSITE_URL = "http://boxdesigner.connectionlab.org"

def render(file_path,width,height,depth,thickness,
           cut_width,notch_length,draw_bounding_box=False, file_type='pdf'):
    the_box = Box(file_path,width,height,depth,thickness,
           			   cut_width,notch_length,draw_bounding_box, file_type)
    the_box.render()
