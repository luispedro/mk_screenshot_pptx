# Make PPTX from anything

This is an abomination, but it works. It actually works very well.

It will take a presentation and screenshot every slide and put it into a PowerPoint presentation, which will literally consist of a single large PNG image per slide.

It is completely agnostic as to what tool you used to originally create the presentation. You can even use it to create a screenshot PowerPoint out of another PowerPoint and avoid any cross-platform issues.

**Limitations**: no video.

## Installation

```bash
conda install python-pptx
conda install mahotas imread
```

You also need to have `scrot` and `xdotool` installed.

It's a Python script that uses the `python-pptx` library to create a PowerPoint presentation and insert the contents of the file into the slides. It will repeatedly press the `J` key to move to the next slide (you can adjust this in the script).


## Usage

```bash
python screenshot_pptx.py
```

You can change some options, namely the _delay_ (how many seconds to wait before changing slides) and the _output file name_ (should be self-explanatory).

```
usage: python screenshot_pptx.py [-h] [--delay SLIDE_DELAY] [-o OUTPUT_NAME]

Create PPTX from any presentation (by screenshotting)

options:
  -h, --help            show this help message and exit
  --delay SLIDE_DELAY
  -o OUTPUT_NAME, --output OUTPUT_NAME
```


## Author

- [Luis Pedro Coelho](https://luispedro.org)
- License: MIT

