
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

VERSION = '1.0.4'
DESCRIPTION = 'Pandas DataFrame Application'
LONG_DESCRIPTION = 'A package that allows to open,view,modify and plot pandas DataFrames along with' \
                   'some scikit-learn algo. implementation.'

# Setting up
setup(
    name="PandasDataFrame",
    version=VERSION,
    author="Bogdan Fometescu",
    author_email="<mbogdan.fometescu@gmail.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['selenium', 'bokeh', 'requests','matplotlib', 'pyqt5', 'pandas', 'scikit-learn'],
    keywords=['python', 'dataframe', 'pandas', 'selenium', ],
    url="https://github.com/BogdanMFometescu/PandasDataFrame",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
