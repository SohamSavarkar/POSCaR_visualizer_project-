import py3Dmol
from ase.io import read
import io
import random

class POSCARVisualizer:
    """
    A class to visualize VASP POSCAR files in a Jupyter Notebook using py3dmol.
    It dynamically assigns colors to each atomic species for clear visualization.
    """
    def __init__(self, poscar_filepath):
        """
        Initializes the visualizer with the path to a POSCAR file.

        Args:
            poscar_filepath (str): The path to the POSCAR file.
        """
        self.filepath = poscar_filepath
        self.atoms = self._read_poscar()
        if self.atoms:
            self.color_library = {}
            self.printable_color_library = {}
            self._setup_colors()

    def _read_poscar(self):
        """Reads the POSCAR file using ASE and handles file not found errors."""
        try:
            return read(self.filepath, format='vasp')
        except FileNotFoundError:
            print(f"Error: The file '{self.filepath}' was not found.")
            print("Please make sure the path is correct.")
            return None

    def _setup_colors(self):
        """Sets up the color libraries for visualization and printing."""
        unique_symbols = set(self.atoms.get_chemical_symbols())

        color_palette = [
            '#FFC0CB', '#ADD8E6', '#90EE90', '#FFD700', '#FFA07A',
            '#20B2AA', '#87CEFA', '#778899', '#B0C4DE', '#FFFFE0'
        ]
        color_name_palette = [
            'Pink', 'LightBlue', 'LightGreen', 'Gold', 'LightSalmon',
            'LightSeaGreen', 'LightSkyBlue', 'LightSlateGray', 'LightSteelBlue', 'LightYellow'
        ]

        color_index = 0
        for symbol in sorted(list(unique_symbols)):
            if color_index < len(color_palette):
                hex_color = color_palette[color_index]
                color_name = color_name_palette[color_index]
                self.color_library[symbol] = hex_color
                self.printable_color_library[symbol] = color_name
                color_index += 1
            else:
                random_color = f"#{random.randint(0, 0xFFFFFF):06x}"
                self.color_library[symbol] = random_color
                self.printable_color_library[symbol] = random_color
        
        print("Generated Color Library:")
        print(self.printable_color_library)

    def show(self):
        """Generates and displays the 3D visualization of the structure."""
        if not self.atoms:
            print("Cannot show visualization because the structure was not loaded.")
            return

        view = py3Dmol.view(width=600, height=600)

        xyz_io = io.StringIO()
        self.atoms.write(xyz_io, format='xyz')
        xyz_data = xyz_io.getvalue()

        view.addModel(xyz_data, 'xyz')

        for symbol, color in self.color_library.items():
            style = {'sphere': {'color': color, 'radius': 0.4}, 'stick': {'color': 'lightgray'}}
            view.setStyle({'elem': symbol}, style)

        view.addUnitCell()
        view.zoomTo()
        view.show()

# --- Example Usage ---
if __name__ == '__main__':
    # IMPORTANT: Replace this with the actual path to your POSCAR file.
    poscar_filepath = '/blue/hennig/ssavarkar/Chabazite/LJ_DFT_Parity/Ag/4mr/0/POSCAR'
    
    # Create an instance of the visualizer
    visualizer = POSCARVisualizer(poscar_filepath)
    
    # Show the visualization
    visualizer.show()

