# NumPy Image Filter

A set of image processing filters (grayscale, blur, edge detection) built entirely from raw NumPy array operations — no built-in filter functions from Pillow or any image processing library.

## Features
- Grayscale conversion using a perceptually-weighted RGB formula
- Box blur using a shift-and-average technique
- Edge detection using shifted-array subtraction

## Usage

Run the script:
python filter.py

This loads demo_image.jpg and produces three output files:
grayscale_output.jpg
blurred_output.jpg
edges_output.jpg

## How each filter works

Grayscale: combines each pixel's R, G, B values into a single brightness value using the formula 0.2989*R + 0.5870*G + 0.1140*B, computed on entire arrays at once via element-wise math (no loops).

Blur: creates four shifted copies of the image (left, right, up, down) using np.roll, then averages them together with the original. Each output pixel becomes the average of itself and its four immediate neighbors.

Edge detection: subtracts a shifted version of the image from the original to find sharp brightness changes between neighboring pixels. Combines horizontal and vertical differences using absolute value, producing a map where edges appear bright and flat areas appear black.

## What I learned
- Images as NumPy arrays: shape conventions (height, width, channels) and what each dimension represents
- Slicing to extract individual color channels
- Vectorized thinking: replacing pixel-by-pixel loops with whole-array operations
- np.roll and how shifting an array lets you access neighboring pixel values without manual indexing
- The difference between averaging (blur) and subtracting (edge detection) as two applications of the same shifting technique
- Converting between float arrays (for math) and uint8 arrays (for valid image data) using .astype()