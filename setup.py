"""Setup  project name project."""
import os
import shutil

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

if os.path.isdir(".pytest_cache") and os.path.exists(".pytest_cache"):
    print("Found $$$$ dir, clearning...")
    shutil.rmtree(".pytest_cache")

setuptools.setup(
    name="image_downloader",
    version="1.0.0",
    description="Download images from google search",
    long_description=long_description,
    long_description_content_type="text/markdown"
)
