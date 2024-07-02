# Make PPTX from anything

This is an abomination, but it works.

It will take a presentation and screenshot every slide and put it into a PowerPoint presentation, which will literally consist of a single large PNG image per slide.

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

## Author

- [Luis Pedro Coelho](https://luispedro.org)
- License: MIT

