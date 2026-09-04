# day 6 - hirst painting

A Python project that uses the `turtle` graphics library to generate a spot painting in the style of Damien Hirst's spin and spot paintings.

## how to run

```bash
uv run src/main.py
```

## skills

- colorgram-py package for extracting dominant colors from an image
- turtle graphics for drawing grids and shapes
- modular programming with custom modules
- file path operations and image processing

## features

- uses colorgram to extract a palette of dominant colors from a reference image
- paints a beautifully aligned 7x7 grid of colored dots randomly selected from the palette
- dynamic background color detection matching the reference image background
- turtle playground class with multi-sided shape generator, random walk, dashed lines, and spirograph
