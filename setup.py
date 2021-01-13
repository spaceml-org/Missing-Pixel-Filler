from setuptools import setup, find_packages 

long_description = '''insert \ 
    long \
    description''' 

setup(
    name ='empty_image_filler', 
    version ='0.0.1', 
    author ='Sarah Chen, Esther Cao', 
    author_email ='insert emails', 
    url ='https://github.com/spaceml-org/empty-image-filler', 
    description ='insert description', 
    long_description = long_description, 
    long_description_content_type ="text/markdown",  
    packages = find_packages(), 
    classifiers =( 
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent", 
    ), 
    keywords ='empty_swath_filler emptySwathFiller filler emptySwath swath empty', 
)
