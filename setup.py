from setuptools import setup, find_packages
setup(
    name="numpy_ringbuffer",
    version="0.1",
    py_modules=['numpy_ringbuffer'],

    install_requires=["numpy"],

    author="Eric Wieser",
    author_email="wieser.eric+numpy@gmail.com",
    description="Ring buffer implementation for numpy",
    license="MIT",
    keywords="hello world example examples",
    url="https://github.com/eric-wieser/raven-client",
    download_url="https://github.com/eric-wieser/raven-client/tarball/0.6",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5"
    ]
)
