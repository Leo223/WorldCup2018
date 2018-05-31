import setuptools

setuptools.setup(
    name="fifa_wc",
    version="0.0.1",
    url="https://github.com/borntyping/cookiecutter-pypackage-minimal",

    author="aterc jcamb jpiza",
    author_email="japizarro@datiobd.com",

    description="Who will be the winnder of FIFA WC 2018?",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
