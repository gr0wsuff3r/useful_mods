# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 15:48:53 2022

@author: bk19127
"""

from setuptools import setup, find_packages

setup(
      name = "useful_mods",
      version = "1.0.0",
      license = "MIT",
      # license = file: license.txt
      description = "This package provides useful modules.",
      packages = find_packages(),
      include_package_data = True,
      install_requires = [
          "numpy",
          "keras",
          "matplotlib",
          "tk",
          "pyaudio",
          "sounddevice",
          "tensorflow", 
          ]
      )