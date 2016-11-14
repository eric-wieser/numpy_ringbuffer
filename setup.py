from setuptools import setup, find_packages
setup(
    name="numpy_ringbuffer",
    version="0.1",
    packages=find_packages(),

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=["numpy"],

    # metadata for upload to PyPI
    author="Eric Wieser",
    author_email="wieser.eric+numpy@gmail.com",
    description="Ring buffer implementation for numpy",
    license="PSF",
    keywords="hello world example examples",
    url="https://github.com/eric-wieser/raven-client",
    download_url="https://github.com/eric-wieser/raven-client/tarball/0.6",


    # could also include long_description, download_url, classifiers, etc.
)