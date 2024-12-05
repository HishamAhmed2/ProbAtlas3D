import nibabel as nib
import numpy as np
from stl import mesh
import skimage as si

class BrainStructureVisualizer:
    """A class for visualizing brain structures from NIfTI files."""
    
    def __init__(self):
        """Initialize the BrainStructureVisualizer."""
        pass
    @staticmethod
    def load_and_preprocess_image(nifti_path):
        """
        Load and preprocess a NIfTI file containing a probability map.

        Parameters:
        - nifti_path (str): Path to the NIfTI file.

        Returns:
        - np.ndarray: Binary 3D image after Gaussian smoothing and thresholding.
        """
        # Load the NIfTI file
        nifti_image = nib.load(nifti_path)
        # Extract the image data
        image_data = nifti_image.get_fdata()
        # Apply Gaussian smoothing to reduce noise
        smoothed_data = si.filters.gaussian(image_data, sigma=0.5)
        # Convert to binary mask based on a threshold
        binary_image = np.array(smoothed_data > 0.5)
        return binary_image
    @staticmethod
    def generate_mesh_from_binary(binary_image):
        """
        Generate a 3D mesh from a binary image using the Marching Cubes algorithm.

        Parameters:
        - binary_image (np.ndarray): 3D binary image.

        Returns:
        - mesh.Mesh: 3D mesh object.
        """
        # Extract vertices, faces, normals, and values using Marching Cubes
        vertices, faces, normals, values = si.measure.marching_cubes(binary_image, 0)
        # Create an empty mesh object
        mesh_object = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
        # Populate the mesh with vertices and faces
        for i, face in enumerate(faces):
            mesh_object.vectors[i] = vertices[face]
        return mesh_object
    @staticmethod
    def extract_vertices_from_mesh(binary_image):
        """
        Extract the vertices from a 3D mesh.

        Returns:
        - np.ndarray: Vertices of the mesh.
        """
        mesh = BrainStructureVisualizer.generate_mesh_from_binary(binary_image)
        vertices = mesh.vectors
        return vertices
