from setuptools import setup

VERSION = '0.1.0'

setup(
    name='py4web-weasyprint',
    version=VERSION,
    url='https://github.com/misl6/py4web-weasyprint',
    license="BSD",
    author='Mirko Galimberti',
    author_email='me@mirkogalimberti.com',
    description='WeasyPrint component for py4web',
    packages=["py4web_weasy"],
    install_requires=[
        "weasyprint"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Topic :: Printing",
        "Topic :: Database :: Front-Ends",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.6',
)
