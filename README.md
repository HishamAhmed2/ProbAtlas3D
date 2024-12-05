Here’s the updated `README.md` file with proper markdown formatting, including **bold text**, headings, lists, code blocks, and other markdown details:

---

# **ProbAtlas3D**

**ProbAtlas3D** is a Python-based application designed for **3D visualization of probability atlases** for any brain region. The application transforms a probability atlas into a **binary image** and utilizes the **Marching Cubes algorithm** to create a 3D mesh. It features a user-friendly **GUI** for interacting with the visualization, allowing users to customize colors, reset the camera, and switch between different files.

---

## **Features**

- **3D Visualization**: Generate interactive 3D representations of brain structures from probability atlases.
- **GUI Interface**: Provides an intuitive GUI to customize the visualization, such as changing colors, resetting the camera, and selecting files.
- **File Selection**: At startup, a custom dialog box prompts users to select files for the **left** and **right brain structures** (e.g., **left substantia nigra** and **right substantia nigra**).
- **Interactive Controls**: Modify and explore brain structures with ease through the GUI.

---

## **Installation**

Follow these steps to set up and run **ProbAtlas3D**:

### **1. Clone the Repository**
Clone the project to your local machine using the following command:
```bash
git clone https://github.com/<your-username>/ProbAtlas3D.git
cd ProbAtlas3D
```

### **2. Install Dependencies**
Install all necessary dependencies using the `requirements.txt` file:
```bash
pip3 install -r requirements.txt
```

### **3. Run the Application**
Launch the application by running the main script:
```bash
python3 navigator_main.py
```

---

## **File Structure**

Below is the file structure of the **ProbAtlas3D** project, with descriptions of each file:

1. **`Dialogbox.py`**:  
   Handles the custom dialog box that allows users to select the probability atlas files for the **left** and **right brain structures**.

2. **`Loading_and_preprocessing.py`**:  
   Responsible for:
   - Transforming the probability atlas into a **binary image**.
   - Generating a **3D mesh** using the **Marching Cubes algorithm**.

3. **`README.md`**:  
   Contains detailed information about the project, installation instructions, usage guidelines, and more.

4. **`gui.py`**:  
   Includes the implementation of the **Graphical User Interface (GUI)**, which allows users to:
   - Change the color of brain structures.
   - Reset the camera view.
   - Load different files.

5. **`navigator_main.py`**:  
   The main script that initializes and launches the application.

6. **`requirements.txt`**:  
   A list of all Python dependencies required to run the application.

---

## **Usage Instructions**

1. **Run the Application**:  
   After running the main script, a **custom dialog box** will appear. This dialog will prompt you to select two files:  
   - **Left Structure File**: For example, the left substantia nigra.  
   - **Right Structure File**: For example, the right substantia nigra.  

2. **Visualization**:  
   Once the files are loaded, the **3D visualization** of the brain structures will be displayed.

3. **Interactive GUI Features**:  
   - **Change Colors**: Customize the color of the brain structures.  
   - **Reset Camera**: Reset the camera to its default view.  
   - **Load Different Files**: Use the GUI to load different files and visualize other brain regions.

---

## **Requirements**

To successfully run the project, you need the following:

- **Python 3.x**  
- Libraries listed in `requirements.txt`:
  - `numpy`
  - `matplotlib`
  - `vtk`
  - `PyQt6` (or your selected PyQt version)

Install the required libraries with:
```bash
pip3 install -r requirements.txt
```

---

## **Examples**

Here's an example workflow for running the application:

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/ProbAtlas3D.git
   cd ProbAtlas3D
   ```
2. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python3 navigator_main.py
   ```

---

## **License**

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this project as per the license terms.

---

## **Contributing**

Contributions are welcome! If you'd like to contribute:
1. **Fork** the repository.  
2. Create a **branch** for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. **Commit** your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push your changes and create a **Pull Request**.

---

## **Contact**

If you have any questions, suggestions, or feedback, feel free to reach out.  
Thank you for using **ProbAtlas3D**! 🎉

--- 

This version incorporates proper markdown syntax with emphasis on structure, headings, bold text, lists, and code formatting. Let me know if there’s anything else you'd like to tweak!
