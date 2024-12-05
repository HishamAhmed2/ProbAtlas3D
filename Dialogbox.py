import sys
from PyQt6 import QtWidgets

class FileSelectionDialog(QtWidgets.QDialog):
    """A custom dialog for selecting NIfTI files."""
    
    def __init__(self):
        """Initialize the file selection dialog."""
        super().__init__()
        self.setWindowTitle("Upload NIfTI Files")
        
        # Set up the layout and initialize attributes
        self.layout = QtWidgets.QVBoxLayout(self)
        self.file_selection_buttons = []  # Buttons for selecting files
        self.file_paths = []  # List of selected file paths

        # File type labels to be displayed on buttons
        file_labels = ["Structure L", "Structure R"]

        for file_label in file_labels:
            # Create a button for each file type
            button = QtWidgets.QPushButton(f"Choose {file_label}")
            button.clicked.connect(lambda _, file_label=file_label: self.select_file(file_label))

            self.file_selection_buttons.append(button)
            self.layout.addWidget(button)

        # Add an OK button to confirm selection
        self.ok_button = QtWidgets.QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)
        self.layout.addWidget(self.ok_button)

    def select_file(self, file_label):
        """
        Open a file dialog to select NIfTI files and update the button label.

        Parameters:
        - file_label (str): The label for the file type being selected.
        """
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setNameFilter("NIfTI files (*.nii)")
        file_dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFiles)
        file_dialog.setViewMode(QtWidgets.QFileDialog.ViewMode.List)
        file_dialog.setWindowTitle(f"Choose {file_label}")

        if file_dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            file_paths = file_dialog.selectedFiles()
            if file_paths:
                selected_file_path = file_paths[0]
                self.file_paths.append(selected_file_path)

                # Update the corresponding button text
                button_index = self.file_selection_buttons.index(self.sender())
                file_name = selected_file_path.split('/')[-1]  # Extract the file name
                self.file_selection_buttons[button_index].setText(f"{file_label}: {file_name}")
            else:
                print("No file selected.")

