from pptx import Presentation
import mahotas as mh

import subprocess
from time import sleep
import tempfile

NR_SLIDES = 3
ADVANCE_SLIDE_KEY = 'J'

def get_screenshot(fname):
    subprocess.check_call(['scrot', '--monitor', '0', fname])
    return fname


def advance_slide():
    subprocess.check_call(['xdotool', 'key', ADVANCE_SLIDE_KEY])


print(f'Creating slides')
print(f'Will simulate pressing {ADVANCE_SLIDE_KEY} to advance slides')
print('Press Ctrl+C to stop')
for i in range(5):
    print(f'Starting in {5-i} seconds')
    sleep(1)

prs = Presentation('empty_16x9.pptx')
blank_slide_layout = prs.slide_layouts[0]

prev = None
while True:
    with tempfile.TemporaryDirectory() as tdir:
        cur = get_screenshot(tdir + 'test.png')
        im = mh.imread(cur)
        if prev is not None:
            if (prev == im).all():
                print('End of presentation detected')
                break
            slide = prs.slides.add_slide(blank_slide_layout)
        else:
            slide = prs.slides[0]
        slide.shapes.add_picture(cur, 0, 0, height=prs.slide_height)
        prev = im

    advance_slide()
    sleep(.5)
prs.save('Snowman.pptx')


