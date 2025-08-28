POSCAR Visualizer
A simple Python tool to visualize VASP POSCAR files directly within a Jupyter Notebook. This package uses the Atomic Simulation Environment (ASE) to parse the crystal structure and py3dmol for interactive 3D rendering. It automatically assigns unique, visually distinct colors to each atomic species in the structure.

Requirements
Python 3.6+

ase

py3dmol

A Jupyter Notebook environment

Installation
You can install this package directly from GitHub using pip:

pip install git+https://github.com/SohamSavarkar/POSCaR_visualizer_project-.git


(Remember to replace your-username/poscar-visualizer-project with the actual URL of your repository.)

Important Note: Jupyter Environment Required
This tool is designed specifically for use within a Jupyter Notebook or JupyterLab environment. It relies on the JavaScript-based rendering capabilities of py3dmol to display the 3D visualization.

It will not work in a non-graphical environment, such as a standard Python script run from the terminal or on a remote High-Performance Computing (HPC) cluster, as there is no graphical user interface to render the output.

Example Usage
Once installed, you can import and use the POSCARVisualizer class in a Jupyter cell.

# Import the class from the library
from poscar_visualizer import POSCARVisualizer

# Provide the path to your POSCAR file
poscar_filepath = 'path/to/your/POSCAR'

# Create an instance of the visualizer.
# This will print the color library assigned to the atomic species.
vis = POSCARVisualizer(poscar_filepath)

# Display the interactive 3D visualization
vis.show()

This will output the color key followed by an interactive 3D model of your crystal structure.

Acknowledgements & Citation
This tool would not be possible without the excellent work of the developers behind the following libraries. If you use this tool in your research, please consider citing their original papers.

Atomic Simulation Environment (ASE):

Ask Hjorth Larsen, Jens Jørgen Mortensen, Jakob Blomqvist, Ivano E. Castelli, Rune Christensen, Marcin Dułak, Jesper Friis, Michael N. Groves, Bjørk Hammer, C. Hargus, Eric D. Hermes, Paul C. Jennings, Peter Bjerre Jensen, James T. Krogstrup, Thomas Markussen, Kevin S. Miceli, Jakob Schiøtz, Ye-Fei Chen, and Karsten W. Jacobsen. The atomic simulation environment—a Python library for working with atoms. Journal of Physics: Condensed Matter, 9(27):275202, 2017.

py3dmol / 3Dmol.js:

Nicholas Rego and David Koes. 3Dmol.js: molecular visualization with WebGL. Bioinformatics, 31(8):1322–1324, 2015.
