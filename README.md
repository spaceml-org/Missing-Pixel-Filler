# Missing Pixel Filler

This is the official code repository for the [**Missing Pixel Filler**](https://arxiv.org/abs/2106.07113) by [SpaceML](http://spaceml.org/).

`missing-pixel-filler` is a python package that, given images that may contain missing data regions (like satellite imagery with swath gaps), returns these images with the regions filled. These regions of missing data are filled using a dynamic method that incorporates randomly chosen, non-null neighboring pixels. The missing data filling algorithms can be changed according to user preferences. 

<img src="https://github.com/spaceml-org/Missing-Pixel-Filler/blob/main/images/swath.png" width="900">

The command-line tool is intended to obscure regions of null or missing data from machine learning pattern-recognition algorithms. However, this package can be used to fill in an image's missing data or a given RGB value in the image for any purpose. 

More information on our work with this package can be found [on Arxiv](https://arxiv.org/abs/2106.07113), or [![Colab Demo](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1GYyXAA_EbUveTeDgwy-wMHj1LXIdXdcy?usp=sharing)

## Usage

#### Installation

This package can be installed by typing the following into your command line:

`pip install git+https://github.com/spaceml-org/Missing-Pixel-Filler.git#egg=missing_pixel_filler`

#### Functions

*Filling Method 1*

`fill_swath_with_random_rgb(img)` - Selects pixel values from a random Gaussian distribution to fill missing pixel values.

*Filling Method 2*

`fill_swath_with_random_pixel_from_image_new(img)` - Fills swath gap with random pixel from non-missing portion of data. 

|-- `get_random_pixel_from_image(x_arr, y_arr)` - Selects other pixel values from non-missing portions of the image.

*Filling Method 3*

`fill_swath_with_neighboring_pixel(img)` - Fills "dynamic" system to fill swath, with nearest pixels having higher probability of selection. 

|-- `get_neighboring_pixel()` - Selects pixel pixel values from non-missing portions of the image to fill missing pixel values with probability inversely proportional to distance. 

#### Arguments

The function arguments are as follows:

`img` - numpy array of input image in utf8 form.

`color ` - Optional parameter - color of missing data to fill in (0 - black, 256 - white). Default is black.

`current_window_size` - for adaptive nearest neighbors method (method 3), radius for selecting neighbor pixels. Default is 10 pixels. 

## Example

Below are some examples with missing data regions filled by our python function (filling method 3). The function call is as follows:

`fill_swath_with_neighboring_pixel(img)`.

Image results: 

**Pre-fill:**
![beachImagesPreFill](https://github.com/spaceml-org/Missing-Pixel-Filler/blob/main/images/beachImagesPreFill.png)

**Post-fill:**
![beachImagesPostFill](https://github.com/spaceml-org/Missing-Pixel-Filler/blob/main/images/beachImagesPostFill.png)

## FAQs

#### What type of images can be used with the python package?

Our package works best if less than 25% of the image data is missing. This package was originally developed to fill missing data from NASA WorldView, in which an image containing 10% to 25% of the total image is still considered for training data. 

#### How does missing-pixel-filler recognize "missing data"?

By default, our code recognizes "missing data" as [0,0,0] RGB, i.e. black, pixels. However, the user has the option to change what RGB values are recognized as "missing data" using the `color` parameter to the functions. 

#### How has missing-pixel-filler been used?

Our code was created as a part of research done under SpaceML and alongside NASA's Impact Team. Our goal was to reduce the effects of swath gaps found in NASA Terra and Aqua satellite images in unsupervised machine learning, as missing data may pose a notable pattern that incorrectly attracts the attention of unsupervised models. More information on our work can be found [here](https://drive.google.com/file/d/18LSWDsXX9PdDLoYNuzKGLzKUZEuGzAo_/view?usp=sharing).

## Citation

If `missing-pixel-filler` is useful in your research, please consider citing

```
@article{caochen2020swathgaps,
  title={Reducing Effects of Swath Gaps in Unsupervised Machine Learning},
  author={Chen, Sarah and Cao, Esther and Koul, Anirudh and Ganju, Siddha and Praveen, Satyarth and Kasam, Meher Anand},
  journal={Committee on Space Research Machine Learning for Space Sciences Workshop},
  year={2021}
}
```
