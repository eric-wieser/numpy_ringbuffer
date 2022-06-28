from io import open
from setuptools import setup

with open('numpy_ringbuffer/__about__.py', encoding='utf8') as f:
    exec(f.read())

with open('README.md', encoding='utf8') as f:
    long_description = f.read()

setup(
    name="numpy_ringbuffer",
    version=__version__,
    packages=['numpy_ringbuffer'],

    install_requires=["numpy"],

    author="Eric Wieser",
    author_email="wieser.eric+numpy@gmail.com",
    description="Ring buffer implementation for numpy",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    keywords=["numpy", "buffer", "ringbuffer", "circular buffer"],
    url="https://github.com/eric-wieser/numpy_ringbuffer",
    download_url="https://github.com/eric-wieser/numpy_ringbuffer/tarball/v"+__version__,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ]
)
