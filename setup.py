from setuptools import setup, find_packages

setup(
    name='poscar-visualizer',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple tool to visualize VASP POSCAR files using py3dmol.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your-username/poscar-visualizer-project', # Link to your repo
    packages=find_packages(),
    install_requires=[
        'py3dmol',
        'ase',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)