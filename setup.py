from setuptools import setup

setup(
    name='pygame-board',
    version = '0.0.0',
    description = 'Quickly Qraw Boards in pygame',
    py_modules=["pygame_board"],
    package_dir={'' : 'src'},
    install_requires=[
        "pygame == 2.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8"
        "License :: MIT License",
    ],
)
