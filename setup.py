from setuptools import setup, find_packages 

# with open('requirements.txt') as f:
#    requirements = f.readlines() 

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
    # entry_points ={ 
    #     'console_scripts': [ 
    #         'gdl = GIBSDownloader.gibs_downloader:main'
    #     ] 
    # }, 
    # classifiers =( 
    #     "Programming Language :: Python :: 3", 
    #     "Operating System :: OS Independent", 
    # ), 
    # keywords ='GIBS gdl satellite python package GIBSDownloader', 
    # install_requires = requirements, 
    zip_safe = False
)
