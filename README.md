**Project**: Live-Cam Telugu OCR

- **Description**: A small demo that captures an image from a camera, runs Tesseract OCR (configured for Telugu), and speaks the extracted text. It also includes a simple `decode.html` keyboard-mapping helper.

**Requirements**:
- **Tesseract**: Install Tesseract OCR (Windows installer or platform-specific). Example Windows installer noted in `Main/App.py` comments.
- **Python packages**: `opencv-python`, `pytesseract`, `pyttsx3`.

**Quick Setup (Windows)**:
- **Install Tesseract**: Download and install from Tesseract project or use the referenced installer in `Main/App.py` comments. Ensure the executable is at `C:\Program Files\Tesseract-OCR\tesseract.exe` or update the path in `Main/App.py`.
- **Create / activate Python env**:
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install opencv-python pytesseract pyttsx3
```

**Run the OCR app**:
- Open a PowerShell terminal and activate the virtual env (see above).
- Run the app:
```
python Main\App.py
```
- Notes:
  - The script uses OpenCV to open the camera. By default `cv2.VideoCapture(1)` is set in `Main/App.py`. If you have a single camera, change it to `0`.
  - If Tesseract is in a different path, update `pytesseract.pytesseract.tesseract_cmd` at the top of `Main/App.py`.

**What `decode.html` does**:
- File: `Main\decode.html` — a small browser-based keyboard mapping tool. Type input and click "Get Mapped Output" to see the custom mapping and hear a short speech notification.

**Language Data**:
- Directory: `Telugu Lang Data` contains training/auxiliary files (unicharset, font properties, configs) used for Tesseract training and runtime for Telugu.
- The `tel` subfolder contains `tel.config` and other files used for language-specific configuration.

**Raspberry Pi / Linux**:
- The repository includes a link in `Main\read me.txt` for running Tesseract OCR on Raspberry Pi (useful if you target Pi deployment). Follow that guide for platform-specific Tesseract installation.

**Files of interest**:
- `Main\App.py` : main demo program (capture, OCR, text-to-speech).
- `Main\decode.html` : keyboard mapping helper.
- `Telugu Lang Data/` : Telugu language data and training files.

**Troubleshooting**:
- If no camera opens, try changing the camera index in `Main\App.py` (`cv2.VideoCapture(1)` → `0`).
- If OCR returns empty text, verify Tesseract path and try running `tesseract --version` in a terminal.

**License / Notes**:
- Language data in `Telugu Lang Data` appears to be sourced/organized for Tesseract training (see `Telugu Lang Data\README.md`). Respect the original license of those files where applicable.

**Want me to**:
- Run quick checks, tweak `App.py` camera index, or add a sample `requirements.txt`? Reply which and I will do it.
