from setuptools import setup, find_packages

setup(
    name='Rufus',
    version='0.1.0',
    packages=['.'],  # Specifies that the current directory should be treated as a package
    install_requires=[
        'playwright', 
        'sentence-transformers',  # Assuming these are your dependencies
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A package for web scraping and data extraction.',
    keywords='web scraping, data extraction, AI',
    url='https://example.com/RufusPackage'
)
