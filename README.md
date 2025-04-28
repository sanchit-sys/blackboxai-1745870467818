
Built by https://www.blackbox.ai

---

```markdown
# Story Video Generator

## Project Overview
The Story Video Generator is a web application built with Flask that allows users to input a story and receive a video summarizing the story with text slides and audio narration. This project leverages the Google Text-to-Speech (gTTS) library for audio generation and MoviePy for video creation.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/story-video-generator.git
   cd story-video-generator
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Flask application:**
   ```bash
   python app.py
   ```

2. **Open your web browser and navigate to:**
   ```
   http://127.0.0.1:5000/
   ```

3. **Enter your story in the text area and submit the form.**
   The application will generate a video and automatically prompt you to download it.

## Features
- Input a story through a user-friendly web interface.
- Automatically splits the story into sentences for video slides.
- Generates an audio narration of the story using Google's Text-to-Speech service.
- Creates and provides a video file containing the text slides and audio narration.
- Automatically cleans up temporary audio files after video generation.

## Dependencies
The following dependencies are required to run the application, which can be found in `requirements.txt`:
- `Flask`: A simple web framework for Python.
- `gTTS`: Google Text-to-Speech for generating audio from text.
- `moviepy`: A Python module for video editing and generation.

## Project Structure
```
.
├── app.py                  # Main application file
├── static                  # Directory for storing generated static files (audio and video)
│   └── audio_*.mp3        # Temporary audio files created during video generation
│   └── video_*.mp4        # Generated video files
└── templates               # Directory for HTML templates
    └── index.html         # The main HTML file for the user interface
```

## Contributing
Contributions are welcome! If you wish to contribute to this project, please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. Please see the [LICENSE](LICENSE) file for more details.
```