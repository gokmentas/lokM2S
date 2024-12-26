# MP3 to SRT Transcription App

A simple GUI application to transcribe audio files into SRT subtitle files using OpenAI's Whisper.

---

## 🌟 Features
- Transcribe audio files (`.mp3`) into SRT subtitle format.
- Customize options for model size, language, chunk size, and punctuation.
- User-friendly interface built with Tkinter.

---

## 📥 For Casual Users

### Installation
1. Download the latest release from the **Releases** section of this repository.
2. Extract the downloaded `.zip` file to a folder of your choice.
3. Double-click the `lokM2S.exe` file to launch the application.

---

## 🛠 For Developers

### Prerequisites
- Python 3.9 or later.
- FFmpeg installed and added to your system's PATH.
- Pip for managing Python packages.

### Installation
1. Clone this repository:
   `git clone https://github.com/gokmentas/lokM2S.git`
2. Navigate to the project directory:
   `cd lokM2S`
3. Install the required dependencies:
   `pip install -r requirements.txt`
4. Ensure FFmpeg is installed and added to your PATH. Verify with:
   `ffmpeg -version`

### Building the Application
1. Install PyInstaller:
   `pip install pyinstaller`
2. Use PyInstaller to create a standalone executable:
   `python -m PyInstaller lokM2S.spec`
3. The executable will be created in the `dist` folder as `lokM2S.exe`.

---

### For Developers: Steps to Run or Modify
1. Clone or download the repository.
2. Install all dependencies as described above.
3. Run the app with:
   `python lokM2S.py`
4. Modify settings such as model size, language, or chunk size directly in the `lokM2S.py` script.
5. To create a new build, follow the steps in **Building the Application**.

---

## 📝 Notes
- Whisper model weights will be downloaded on the first run.
- Logs will be displayed in the terminal for debugging.

---

## 💡 Contribution
Feel free to submit issues or open pull requests to improve this application!
