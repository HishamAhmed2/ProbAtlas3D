import numpy as np
import vtkplotlib as vpl
from PyQt6 import QtWidgets, QtCore
from Dialogbox import FileSelectionDialog
from Loading_and_preprocessing import BrainStructureVisualizer

class STRviewerUI(QtWidgets.QWidget):
    """
    A graphical user interface for visualizing brain structures from NIfTI files.

    Features:
    - File selection dialog for uploading brain structure data.
    - Visualization of brain structures (left and right).
    - Tools for adjusting visualization (color, camera reset).
    - Ability to save the visualization as an image file.
    """

    def __init__(self):
        """
        Initialize the STRviewerUI interface.
        Sets up the layout, widgets, and default parameters for visualization.
        """
        super().__init__()

        # Lists to hold plotted structures (left and right).
        self.structure_L_plot = []
        self.structure_R_plot = []

        # Main layout for the interface.
        vbox = QtWidgets.QVBoxLayout()
        self.setLayout(vbox)
        self.setWindowTitle('Structure Viewer')

        # Create a vtkplotlib figure for 3D visualization.
        self.figure = vpl.QtFigure()

        # Toolbar for actions (file upload, save, reset, etc.).
        toolbar = QtWidgets.QToolBar("Main Toolbar")
        files_upload = toolbar.addAction("Files")
        files_upload.triggered.connect(self.files_upload_dialog)

        save_action = toolbar.addAction("Save")
        save_action.triggered.connect(self.save_as_image)

        reset_action = toolbar.addAction("Reset Camera Distance")
        reset_action.triggered.connect(self.camera_reset_button)

        # Add color picker action for structure visualization.
        struct_color_action = toolbar.addAction("Choose Structure Color")
        struct_color_action.triggered.connect(self.color_picker)
        self.struct_color = "dark red"  # Default structure color.

        # Checkboxes for toggling visibility of left and right structures.
        self.label_structure = QtWidgets.QLabel("Structure")
        self.checkbox_L_structure = QtWidgets.QCheckBox("Structure L")
        self.checkbox_L_structure.setChecked(False)
        self.checkbox_L_structure.toggled.connect(self.onClickedLstructure)

        self.checkbox_R_structure = QtWidgets.QCheckBox("Structure R")
        self.checkbox_R_structure.setChecked(False)
        self.checkbox_R_structure.toggled.connect(self.onClickedRstructure)

        # Prompt user to upload files at the start.
        self.files_upload_dialog()

        # Layout for structure checkboxes.
        structural_layout = QtWidgets.QVBoxLayout()
        structural_layout.addWidget(self.checkbox_L_structure)
        structural_layout.addWidget(self.checkbox_R_structure)

        checkbox_layout = QtWidgets.QHBoxLayout()
        checkbox_layout.addWidget(self.label_structure)
        checkbox_layout.addLayout(structural_layout)

        # Add widgets to the main layout.
        vbox.addWidget(toolbar)
        vbox.addWidget(self.figure)
        vbox.addLayout(checkbox_layout)

    def files_upload_dialog(self):
        """
        Opens a file selection dialog to upload NIfTI files for left and right structures.
        """
        dialog = FileSelectionDialog()
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            file_paths = dialog.file_paths
            if len(file_paths) == 2:
                # Assign files to respective structures based on button labels.
                for file, button in zip(file_paths, dialog.file_selection_buttons):
                    if "Structure R" in button.text():
                        self.Rmask_name = file
                        self.Rmask = BrainStructureVisualizer.load_and_preprocess_image(self.Rmask_name)
                    elif "Structure L" in button.text():
                        self.Lmask_name = file
                        self.Lmask = BrainStructureVisualizer.load_and_preprocess_image(self.Lmask_name)
            else:
                print("Please select exactly 3 NIfTI files.")

    def camera_reset_button(self):
        """
        Resets the camera distance to the default view in the 3D visualization.
        """
        vpl.reset_camera(self.figure)
        self.figure.update()
    
    def color_picker(self):
        """
        Opens a color picker dialog to select a color for the structure visualization.
        Updates the visualization with the new color.
        """
        color = QtWidgets.QColorDialog.getColor()
        self.struct_color = color
        if self.structure_R_plot:
            self.figure.remove_plot(self.structure_R_plot)
        if self.structure_L_plot:
            self.figure.remove_plot(self.structure_L_plot)
        self.onClickedLstructure()
        self.onClickedRstructure()

    def onClickedRstructure(self):
        """
        Toggles the visibility of the right structure (Structure R) based on the checkbox state.
        """
        if self.checkbox_R_structure.isChecked():
            vertices = BrainStructureVisualizer.extract_vertices_from_mesh(self.Rmask)
            self.structure_R_plot = vpl.plot(vertices, join_ends=True, color=self.struct_color)
            vpl.reset_camera(self.figure)
            self.figure.update()
        elif self.structure_R_plot:
            self.figure.remove_plot(self.structure_R_plot)  # Remove the mesh if exists.
            self.structure_R_plot = []
            self.figure.update()    
    
    def onClickedLstructure(self):
        """
        Toggles the visibility of the left structure (Structure L) based on the checkbox state.
        """
        if self.checkbox_L_structure.isChecked():
            vertices = BrainStructureVisualizer.extract_vertices_from_mesh(self.Lmask)
            self.structure_L_plot = vpl.plot(vertices, join_ends=True, color=self.struct_color)
            vpl.reset_camera(self.figure)
            self.figure.update()
        elif self.structure_L_plot:
            self.figure.remove_plot(self.structure_L_plot)  # Remove the mesh if exists.
            self.structure_L_plot = []
            self.figure.update()



    def save_as_image(self):
        """
        Opens a file dialog to save the current visualization as an image file.
        Supports formats like TIFF, JPG, and PNG.
        """
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setFileMode(QtWidgets.QFileDialog.FileMode.AnyFile)
        file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptMode.AcceptSave)
        file_dialog.setNameFilter("Images (*.tiff *.jpg *.png)")

        if file_dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            file_path = file_dialog.selectedFiles()[0]
            print(file_path)
            vpl.save_fig(file_path, off_screen=True, fig=self.figure)

    def show(self):
        """
        Displays the main interface and the 3D visualization figure.
        """
        super().show()
        self.figure.show()

    def closeEvent(self, event):
        """
        Handles cleanup when the application is closed.
        Ensures proper disposal of resources and the 3D figure.
        """
        self.figure.closeEvent(event)
