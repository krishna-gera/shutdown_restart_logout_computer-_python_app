## Shutdown, Restart & Logout using Tkinter

This application provides a simple graphical interface to shutdown, restart, or log out of your Windows PC using Tkinter. The application has been designed with a clear and user-friendly interface, allowing for quick access to these system commands.

### Features
- **Shutdown**: Instantly shuts down the PC.
- **Restart**: Instantly restarts the PC.
- **Logout**: Logs out the current user.

### Prerequisites
- Python 3.x
- Tkinter (usually included with Python)

### Installation
1. Ensure you have Python 3.x installed on your system.
2. Tkinter should be included with your Python installation. If not, install it using the package manager:
   ```sh
   pip install tk
   ```

### Usage
1. Run the script in your Python environment:
   ```sh
   python script_name.py
   ```
2. A window will appear with buttons to shutdown, restart, and log out. Click the desired button to perform the corresponding action.

### Customization
- **Window Title and Size**: Modify the title and size of the window by changing the parameters in the `window.geometry()` and `window.title()` methods.
- **Button Colors and Text**: Customize the appearance of the buttons by adjusting the parameters in the `Button` creation lines.

