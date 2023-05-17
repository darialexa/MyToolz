
import nuke

# ---------------------------------------------------
# ---------------------------------------------------
# DARIA'S CUSTOM STUFF
# Last Updated: May 17, 2023
# ---------------------------------------------------
# ---------------------------------------------------

# ADJUSTED KNOB DEFAULTS ----------------------------

# ROTO AND PAINT CLIP SET TO NO_CLIP-----------------
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


# J_Tracker_Checkboxes v.1.0.0
# Jazlyn Cartaya, 2019

def tracker_checkboxes_tab():
    """This function creates a tab in the Tracker node that
    lets the artist select the amount of T, R, S Tracker
    checkboxes they want to check."""

    node = nuke.thisNode()

    # Create knobs:
    tab = nuke.Tab_Knob('Check Boxes')
    node.addKnob(tab)

    number_of_trackers = nuke.String_Knob('number_of_trackers',
                                          'number of trackers:',
                                          'All'
                                          )
    node.addKnob(number_of_trackers)

    t_boolean_knob = nuke.Boolean_Knob('translate_box', 'translate', True)
    node.addKnob(t_boolean_knob)

    r_boolean_knob = nuke.Boolean_Knob('rotate_box', 'rotate', True)
    node.addKnob(r_boolean_knob)

    s_boolean_knob = nuke.Boolean_Knob('scale_box', 'scale', True)
    node.addKnob(s_boolean_knob)

    pyknob = nuke.PyScript_Knob('check_tracker_boxes',
                                'execute',
                                'tracker_checkboxes()'
                                )
    pyknob.setFlag(nuke.STARTLINE)
    node.addKnob(pyknob)

nuke.addOnCreate(lambda: tracker_checkboxes_tab(), nodeClass='Tracker4')

# Check boxes in 'Tracker' node:


def tracker_checkboxes():
    """This function checks all or x amount of T, R, and S
    checkboxes in the Tracker node."""

    # Variables:
    this_node = nuke.thisNode()
    knob = this_node['tracks']
    num_columns = 31
    col_translate = 6
    col_rotate = 7
    col_scale = 8
    count = 0
    trackers_knob_value = this_node.knob('number_of_trackers').value()
    t_knob_value = this_node.knob('translate_box').value()
    r_knob_value = this_node.knob('rotate_box').value()
    s_knob_value = this_node.knob('scale_box').value()

    # Put toScript in list:
    trackers = []
    script = this_node['tracks'].toScript()
    trackers.append(script)  # add to list

    # Get number of tracks from list:
    for item in trackers:
        total_tracks = item.count('\"track ')

    # Check ALL boxes:
    # Math = (True (1) or False (0), 31 columns * track number (0 to infinity)
    # + Translate (6), Rotate (7), or Scale (8))
    try:
        if trackers_knob_value == 'All':
            while count <= int(total_tracks)-1:

                if all([t_knob_value, r_knob_value, s_knob_value]):
                    knob.setValue(True, num_columns * count + col_translate)
                    knob.setValue(True, num_columns * count + col_rotate)
                    knob.setValue(True, num_columns * count + col_scale)
                elif not any([t_knob_value,
                              r_knob_value,
                              s_knob_value]):
                    knob.setValue(False, num_columns * count + col_translate)
                    knob.setValue(False, num_columns * count + col_rotate)
                    knob.setValue(False, num_columns * count + col_scale)

                if t_knob_value is True:
                    knob.setValue(True, num_columns * count + col_translate)
                elif t_knob_value is False:
                    knob.setValue(False, num_columns * count + col_translate)

                if r_knob_value is True:
                    knob.setValue(True, num_columns * count + col_rotate)
                elif r_knob_value is False:
                    knob.setValue(False, num_columns * count + col_rotate)

                if s_knob_value is True:
                    knob.setValue(True, num_columns * count + col_scale)
                elif s_knob_value is False:
                    knob.setValue(False, num_columns * count + col_scale)
                count += 1

        # Check x number of boxes:
        if trackers_knob_value != 'All':

            for track in range(0, int(total_tracks)):
                knob.setValue(False, num_columns * track + col_translate)
                knob.setValue(False, num_columns * track + col_rotate)
                knob.setValue(False, num_columns * track + col_scale)

            while count <= int(trackers_knob_value)-1:

                if t_knob_value is True:
                    knob.setValue(True, num_columns * count + col_translate)

                if r_knob_value is True:
                    knob.setValue(True, num_columns * count + col_rotate)

                if s_knob_value is True:
                    knob.setValue(True, num_columns * count + col_scale)
                count += 1

    except ValueError:
        nuke.message('The value you entered was not a number.'
                     ' Please enter a number value or "All".')

