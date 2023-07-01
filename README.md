
<h1 align="center">
  Instagramizer
</h1>

<p align="center">
  <strong>A command-line tool to easily process images for Instagram</strong>
</p>

<p align="center">
  <img src="imgs/screenshot.png" alt="Instagramizer Screenshot">
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#before-and-after">Before and After</a> •
  <a href="#todo">TODO</a> •
  <a href="#license">License</a>
</p>

---

## Features

- Batch add color frames to images
- Resize images to 1080x1080 pixels
- Simple and easy-to-use command-line interface

---

## Installation

1. Clone the Instagramizer repository:

   ```shell
   git clone https://github.com/your_username/instagramizer.git
   ```

2. Navigate to the project directory:

   ```shell
   cd instagramizer
   ```

3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

---

## Usage

1. Navigate to the project directory:

   ```shell
   cd instagramizer
   ```

2. Run the Instagramizer program:

   ```shell
   python CUI.py
   ```

3. Use the following keys to navigate through the modes:

   - `↑` and `↓` arrow keys: Scroll through image files in the Import mode.
   - `A`: Activate the Select mode.
   - `I`: Interact with the current mode.
   - `Q`: Quit the program.

4. In the Import mode, use the `↑` and `↓` arrow keys to scroll through image files and select an image to import.

5. In the Select mode, no function is available.

6. In the Export mode, press `I` to start the export process and generate the processed images.

7. The program will display the number of imported images, the selected color, and the export status in the interface.

---

## Before and After

<p align="center">
  <strong>Before</strong>
  <br>
  <img src="imgs/before_image.jpg" alt="Before Image" width="500">
</p>

<p align="center">
  <strong>After</strong>
  <br>
  <img src="imgs/after_image.jpg" alt="After Image" width="500">
</p>

---

## TODO

1. Support responsive terminal size
2. Implement threading for faster export

Feel free to contribute by submitting a pull request to the project repository.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

<p align="center">
  Developed with ❤️ by @WasinUddy
</p>
