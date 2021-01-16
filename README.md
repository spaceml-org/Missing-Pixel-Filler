# Missing Pixel Filler Filler

Missing-pixel-filler is a python package that, given images that may contain missing data regions, returns these images with the regions filled. These regions of missing data are filled using a dynamic method that incorporates randomly chosen, non-null neighboring pixels.

Our command-line tool is intended to obscure regions of null or missing data from machine learning pattern-recognition algorithms. However, this package can be used to fill in an image's missing data or a given RGB value in the image for any purpose. More information on our work with this package can be found [here](https://drive.google.com/file/d/18LSWDsXX9PdDLoYNuzKGLzKUZEuGzAo_/view?usp=sharing).

## Installation

[in progress]
Clone the directory with this url: https://github.com/spaceml-org/Missing-Pixel-Filler.git

## Usage

Here we explain how to use our package.

#### Functions
`fill_swath_with_random_rgb(img)` - Filling Method 1. Selects pixel values from a random Gaussian distribution to fill missing pixel values.

`fill_swath_with_random_pixel_from_image_new(img)` - Filling Method 2. Fills swath gap with random pixel from non-missing portion of data. 

|-- `get_random_pixel_from_image(x_arr, y_arr)` - Selects other pixel values from non-missing portions of the image.

`fill_swath_with_neighboring_pixel(img)` - Filling Method 3. Fills "dynamic" system to fill swath, with nearest pixels having higher probability of selection. 

|-- `get_neighboring_pixel()` - Selects pixel pixel values from non-missing portions of the image to fill missing pixel values with probability inversely proportional to distance. 

#### Arguments
The function arguments are as follows:
`img` - numpy array of input image in utf8 form.
`color ` - color of missing data to fill in (0 - black, 256 - white). Default is black. (Optional)
`current_window_size` - for adaptive nearest neighbors method (method 3), radius for selecting neighbor pixels. Default is 10 pixels. (Optional)

## Example

Below are some examples with missing data regions filled by our python function (filling method 3). The function call is as follows:
`fill_swath_with_neighboring_pixel(img)`.

Image results: 

**Pre-fill:**
![beachImagesPreFill](beachImagesPreFill.png)

**Post-fill:**
![beachImagesPostFill](beachImagesPostFill.png)

## FAQs
#### What type of images can be used with the python package?

Our package works best if less than 25% of the image data is missing. This package was originally developed to fill missing data from NASA WorldView, in which an image containing 10% to 25% of the total image is still considered for training data. 

#### How does image-data-filler recognize "missing data"?

By default, our code recognizes "missing data" as [0,0,0] RGB, i.e. black, pixels. However, the user has the option to change what RGB values are recognized as "missing data" using the `color` parameter to the functions. 

#### How has image-data-filler been used?

Our code was created as a part of research done under SpaceML and alongside NASA's Impact Team. Our goal was to reduce the effects of swath gaps found in NASA Terra and Aqua satellite images in unsupervised machine learning, as missing data may pose a notable pattern that incorrectly attracts the attention of unsupervised models. More information on our work can be found [here](https://drive.google.com/file/d/18LSWDsXX9PdDLoYNuzKGLzKUZEuGzAo_/view?usp=sharing).

## Citation

If image-data-filler is useful in your research, please consider citing
```
@article{cao2020swathgaps,
  title={Reducing Effects of Swath Gaps in Unsupervised Machine Learning},
  author={Chen, Sarah and Cao, Esther and Koul, Anirudh and Ganju, Siddha and Praveen, Satyarth and Kasam, Meher Anand},
  journal={Committee on Space Research Machine Learning for Space Sciences Workshop},
  year={2021}
}
```
