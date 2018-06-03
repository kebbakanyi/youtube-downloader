from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    nmae='Youtube Downloader',
    version='1.0.0',
    author='Kebba Kanyi',
    author_email='kebbakanyi@gmail.com',
    description='Download videos from Youtube',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    packages=find_packages(),
    install_requires=[

    ],

    entry_points={
        'console_scripts': [
            'youtube-downloader = downloader.main'
        ]
    },

    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
