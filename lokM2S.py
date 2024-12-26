import whisper
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import re

# Initialize a variable for the SRT file path
srt_file_path = None


# Function to load the model and perform transcription
def transcribe_audio():
    global srt_file_path

    # Get selected options
    model_size = model_var.get()
    language = lang_var.get()
    chunk_size = int(chunk_var.get())
    with_punctuation = punctuation_var.get()

    # Update status and progress
    status_label.config(text="Loading model...")
    progress_bar['value'] = 20
    root.update_idletasks()

    # Load Whisper model
    model = whisper.load_model(model_size)

    # Get audio file path
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    if not file_path:
        messagebox.showerror("Error", "No audio file selected!")
        return

    # Ask for SRT file save location
    srt_file_path = filedialog.asksaveasfilename(defaultextension=".srt", filetypes=[("SRT files", "*.srt")])
    if not srt_file_path:
        messagebox.showerror("Error", "No save location selected for SRT file!")
        return

    # Update status and progress
    status_label.config(text="Transcribing audio...")
    progress_bar['value'] = 50
    root.update_idletasks()

    # Transcribe audio
    result = model.transcribe(file_path, language=language)

    # Remove punctuation if option is disabled
    if not with_punctuation:
        for segment in result['segments']:
            segment['text'] = remove_punctuation(segment['text'])

    # Update status and progress
    status_label.config(text="Generating SRT file...")
    progress_bar['value'] = 80
    root.update_idletasks()

    # Generate SRT with specified chunk size
    transcribe_to_srt(result, chunk_size)

    # Update status and progress
    progress_bar['value'] = 100
    status_label.config(text="Transcription complete!")
    messagebox.showinfo("Success", f"SRT file created successfully at:\n{srt_file_path}")


# Function to remove punctuation
def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', text)


# Function to split text into chunks and generate SRT file
def split_into_chunks(text, chunk_size=3):
    words = text.strip().split()
    return [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]


# Function to generate SRT file from transcribed segments
def transcribe_to_srt(result, chunk_size=3):
    global srt_file_path

    srt_content = ""
    count = 1

    for segment in result['segments']:
        start = segment['start']
        end = segment['end']
        text = segment['text']

        chunks = split_into_chunks(text, chunk_size)
        total_duration = end - start
        chunk_duration = total_duration / len(chunks)

        for i, chunk in enumerate(chunks):
            chunk_start = start + i * chunk_duration
            chunk_end = chunk_start + chunk_duration

            start_time = format_timestamp(chunk_start)
            end_time = format_timestamp(chunk_end)

            srt_content += f"{count}\n{start_time} --> {end_time}\n{chunk.strip()}\n\n"
            count += 1

    with open(srt_file_path, "w", encoding="utf-8") as srt_file:
        srt_file.write(srt_content)


# Helper function to format timestamp
def format_timestamp(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    sec = int(seconds % 60)  # Store integer part of seconds separately
    milliseconds = int((seconds - int(seconds)) * 1000)  # Calculate milliseconds using the fractional part
    return f"{hours:02}:{minutes:02}:{sec:02},{milliseconds:03}"


# Set up the Tkinter GUI
root = tk.Tk()
root.title("Audio to SRT Transcription")

# Model size option
tk.Label(root, text="Select Model Size:").grid(row=0, column=0, padx=10, pady=10)
model_var = tk.StringVar(value="medium")
model_options = ["tiny", "base", "small", "medium", "large"]
tk.OptionMenu(root, model_var, *model_options).grid(row=0, column=1, padx=10, pady=10)

# Language option
tk.Label(root, text="Select Language:").grid(row=1, column=0, padx=10, pady=10)
lang_var = tk.StringVar(value="tr")
lang_options = ["tr", "en", "es", "fr", "de", "zh"]
tk.OptionMenu(root, lang_var, *lang_options).grid(row=1, column=1, padx=10, pady=10)

# Chunk size option
tk.Label(root, text="Words per Caption (Chunk Size):").grid(row=2, column=0, padx=10, pady=10)
chunk_var = tk.StringVar(value="2")
tk.Entry(root, textvariable=chunk_var).grid(row=2, column=1, padx=10, pady=10)

# Punctuation option
punctuation_var = tk.BooleanVar(value=False)
tk.Checkbutton(root, text="Include Punctuation", variable=punctuation_var).grid(row=3, column=0, columnspan=2, padx=10,
                                                                                pady=10)

# Progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress_bar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Status label
status_label = tk.Label(root, text="")
status_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Transcribe button
transcribe_button = tk.Button(root, text="Select Audio & Transcribe", command=transcribe_audio)
transcribe_button.grid(row=6, column=0, columnspan=2, padx=10, pady=20)

root.mainloop()
