from setuptools import setup, find_packages

setup(
    name='mkdocs-strip-toc',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'strip-toc = strip_toc.plugin:StripTocPlugin',
        ]
    }
)