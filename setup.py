#! /bin/env python
"""
setup.py
=========

.. moduleauthor:: Dillon Hicks <hhicks@ittc.ku.edu>

"""
import sys
import os

###################################################################
# 
# Code from  http://wiki.python.org/moin/Distutils/Cookbook
#
###################################################################
    
def is_package(path):
    """
    Determine if the path is a python package.
    """
    return (
        os.path.isdir(path) and
        os.path.isfile(os.path.join(path, '__init__.py'))
        )

def find_packages(path, base="" ):
    """
    Find all python packages in path. 
    """
    packages = {}
    for item in os.listdir(path):
        dir = os.path.join(path, item)
        if is_package( dir ):
            if base:
                module_name = "%(base)s.%(item)s" % vars()
            else:
                module_name = item
            packages[module_name] = dir
            packages.update(find_packages(dir, module_name))
    return packages

###### END Distutils Cookbook Code #######

def run_distutils():
    """
    Executes the distutils setup code.
    """
    
    from distutils.core import setup, Extension

    source_dir = os.getcwd() 
    kwargs = {}

    packages = find_packages('.')
    kwargs['package_dir'] = packages
    kwargs['packages'] = packages.keys()

    kwargs.update(dict(
            name='svgenesis',
            author='Dillon Hicks <hhicks@ittc.ku.edu>',
            description="Tools for creating and manipulating SVG images.",
            version='0.9',
            url='http://www.ittc.ku.edu/kusp',
            scripts=['scripts/intervals2timeline.py',]
            ))
    
    setup(**kwargs)






if __name__ == '__main__':
    run_distutils()


