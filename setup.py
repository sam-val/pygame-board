from setuptools import setup

with open("README.md", "r") as f:
    description = f.read()

with open("requirements.txt", "r") as f:
        requirements = []
        for line in f:
            requirements.append(line.strip())

setup(
    name='pygame-board',
    version = '0.0.0',
    description = 'Quickly Qraw Boards in pygame',
    py_modules=["pygame_board"],
    package_dir={'' : 'src'},
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Topic :: Games/Entertainment",
    ],
    long_description=description,
    long_description_content_type="text/markdown",
    extras_require = {
        "dev": [
            "twine",    
        ],    
    },
)
