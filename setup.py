from setuptools import setup, find_packages

setup(
    name='jarvis_stt',
    version='0.1',
    author='Monsta',
    author_email='freeai007123@gmail.com',
    description=' A simple speech-to-text application for Jarvis'
)
packages = find_packages(),   
install_requires=[
    'selenium',
    'webdriver-manager'
]