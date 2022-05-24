from setuptools import setup

with open('numpy_ringbuffer/__about__.py') as f:
    exec(f.read())

def read_txt_file(filename):
    return open(filename).read()

try:
    # pypandoc < 1.8
    from pypandoc import convert
    read_txt_file = lambda x: convert(x, 'rst')
except:
    pass

try:
    # pypandoc >= 1.8
    from pypandoc import convert_file
    read_txt_file = lambda x: convert_file(x, 'rst')
except:
    pass

setup(
    name="numpy_ringbuffer",
    version=__version__,
    packages=['numpy_ringbuffer'],

    install_requires=["numpy"],

    author="Eric Wieser",
    author_email="wieser.eric+numpy@gmail.com",
    description="Ring buffer implementation for numpy",
    long_description=read_txt_file('README.md'),
    license="MIT",
    keywords=["numpy", "buffer", "ringbuffer", "circular buffer"],
    url="https://github.com/eric-wieser/numpy_ringbuffer",
    download_url="https://github.com/eric-wieser/numpy_ringbuffer/tarball/v"+__version__,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5"
    ]
)
