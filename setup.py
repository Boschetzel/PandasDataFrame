
from setuptools import setup, find_packages


VERSION = '1.0.2'
DESCRIPTION = 'Pandas DataFrame Application'
LONG_DESCRIPTION = 'A package that allows to open,view,modify and plot pandas DataFrames.'

# Setting up
setup(
    name="PandasDataFrame",
    version=VERSION,
    author="Boschetzel (Bogdan Fometescu)",
    author_email="<mbogdan.fometescu@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['selenium', 'bokeh', 'requests','matplotlib','pyqt5'],
    keywords=['python', 'dataframe', 'pandas', 'selenium', ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
