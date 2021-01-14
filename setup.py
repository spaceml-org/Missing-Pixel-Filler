from setuptools import setup, find_packages 

long_description = '''Python package used to fill an image's missing data gaps. \ 
    Specifically useful for obscuring image patterns in a machine learning context.''' 

setup(
    name ='image_data_filler', 
    version ='0.0.1', 
    author ='Sarah Chen, Esther Cao', 
    author_email ='sarah.chen6@gmail.com, esthercao888@gmail.com', 
    url ='https://github.com/spaceml-org/empty-image-filler', 
    description ='downloading tool to fill missing data gaps', 
    long_description = long_description, 
    long_description_content_type ="text/markdown",  
    packages = find_packages(), 
    classifiers =( 
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent", 
    ), 
    keywords ='empty_image_data_filler empty_image_filler image_data_filler empty_swath_filler data_filler swath_filler image_filler filler image data swath empty', 
    install_requires = ["Keras-Preprocessing==1.1.2", "numpy==1.19.4", "tensorflow==2.4.0"]
    extras_require = {"dev": ["pytest >= 3.7", ], }
)
