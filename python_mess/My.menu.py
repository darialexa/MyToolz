# ---------------------------------------------------
# Daria's custom stuff here
# Version: 1.0.4
# Last Updated: Mar27, 2023
# ---------------------------------------------------

# ADJUSTED KNOB DEFAULTS ----------------------------

# ROTO AND PAINT CLIP SET TO NO_CLIP---------------------------
# nuke.knobDefault('Roto.cliptype', "none")
# nuke.knobDefault('RotoPaint.cliptype', "none")

nuke.knobDefault('Dot.label', '[knob name]')

# MOTION BLUR SHUTTER CENTERED ----------------------
nuke.knobDefault('Tracker4.shutteroffset', "centered")
nuke.knobDefault('TimeBlur.shutteroffset', "centered")
nuke.knobDefault('Transform.shutteroffset', "centered")
nuke.knobDefault('TransformMasked.shutteroffset', "centered")
nuke.knobDefault('CornerPin2D.shutteroffset', "centered")
nuke.knobDefault('MotionBlur2D.shutteroffset', "centered")
nuke.knobDefault('MotionBlur3D.shutteroffset', "centered")
nuke.knobDefault('ScanlineRender.shutteroffset', "centered")
nuke.knobDefault('Card3D.shutteroffset', "centered")

# This one is set up, but changes back to "single frame" once Clone or Paint stroke is created :(
# nuke.knobDefault('RotoPaint.lifetime_type', "all frames")
# nuke.addOnUserCreate(lambda:nuke.thisNode()['lifetime_type'].setValue("all frames"), nodeClass='RotoPaint')

# Set dynamic label on Tracker to display the value of the "transform" and "reference_frame" knobs
nuke.knobDefault('Tracker4.label', "Motion: [value transform]\nRef Frame: [value reference_frame]")

# Any time a Tracker node is created, set the "reference_frame" knob to the value of the current frame
nuke.addOnUserCreate(lambda:nuke.thisNode()['reference_frame'].setValue(nuke.frame()), nodeClass='Tracker4')

# Any time a FrameHold node is created, set the "first frame" knob to the value of the current frame
nuke.addOnUserCreate(lambda:nuke.thisNode()['firstFrame'].setValue(nuke.frame()), nodeClass='FrameHold')

# Set Kronos's timing to "frame"
nuke.knobDefault('Kronos.timing2', "Frame")

# Set Blur to "5"
nuke.knobDefault('Blur.size', "5")

# Set Defocus to anamorphic
nuke.knobDefault('Defocus.ratio', "0.5")


# CUSTOM MENUS -------------------------------------
utilitiesMenu = nuke.menu('Nuke').addMenu('Darias')
utilitiesMenu.addCommand('Autocrop', 'nukescripts.autocrop()')

myGizmosMenu = nuke.menu('Nodes').addMenu('myGizmos', icon="/mnt/SharedProfiles/dalexander@fatbelly.local/.nuke/Icons/Daria.png")
myGizmosMenu.addCommand('bm_MatteCheck', 'nuke.createNode("bm_MatteCheck")', icon="bm_MatteCheck_icon.png")
myGizmosMenu.addCommand('V_Multilabeler', 'nuke.createNode("V_Multilabeler")', icon="V_Multilabeler.png")
myGizmosMenu.addCommand('Florian', 'nuke.createNode("Florian")')

# V_Multilabeler definitions
# toolbar = nuke.menu('Nodes')
# VMenu = toolbar.addMenu('V!ctor', icon='V_Victor.png')
# VMenu.addCommand('V_Multilabeler', 'nuke.createNode("V_Multilabeler")', icon='V_Multilabeler.png')


# END OF DARIAS STUFF THANKS FOR WATCHING-----------

