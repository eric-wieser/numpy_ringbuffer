from setuptools import setup

with open('numpy_ringbuffer/__about__.py') as f:
    exec(f.read())

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except (IOError, ImportError):
    print("No")
    long_description = open('README.md').read()

setup(
    name="numpy_ringbuffer",
    version=__version__,
    packages=['numpy_ringbuffer'],

    install_requires=["numpy"],

    author="Eric Wieser",
    author_email="wieser.eric+numpy@gmail.com",
    description="Ring buffer implementation for numpy",
    long_description=long_description,
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
