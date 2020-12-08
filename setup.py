from setuptools import setup

setup(
    name='pygame-board',
    version = '0.0.0',
    description = 'Quickly Qraw Boards in pygame',
    py_modules=["board"],
    package_dir={'' : 'src'},
    install_requires=[
        "pygame == 2.0.0",
    ],
)