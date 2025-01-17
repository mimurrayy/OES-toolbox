import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="OES-toolbox",
    version="0.3.3",
    author="Julian Held",
    author_email="j.held@tue.nl",
    license='MIT',
    platforms=['any'],
    description="Tool for low-temperature plasma optical emission spectroscopy.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://oes-toolbox.com",
    packages=setuptools.find_packages(),
    install_requires=[
          'owlspec>=0.2.2', 'moose-spectra>=0.2.0', 'pyqtgraph>=0.13.1', 'PyQt6>=6.5.0',
          'sif-parser>=0.3.0', 'file-read-backwards>=3.0.0', 'matplotlib>=3.7.0'
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8.1',
    package_data={'OES_toolbox': ['ui/main.ui', 'ui/resources.py', 'ui/jh-paper.mplstyle', 'data/mol_spec/*.mod']},
    entry_points = {'gui_scripts': ['OES-toolbox = OES_toolbox:main']}
)
