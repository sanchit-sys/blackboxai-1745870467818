from flask import Flask, render_template, request, send_file
from gtts import gTTS
from moviepy.editor import *
import os
import uuid

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        story = request.form['story']
        if not story.strip():
            return render_template('index.html', error="Please enter a story.")
        
        # Generate audio from story text
        tts = gTTS(text=story, lang='en')
        audio_filename = f"static/audio_{uuid.uuid4()}.mp3"
        tts.save(audio_filename)

        # Create a video clip with text and audio
        clips = []
        # Split story into chunks for slides (simple split by sentences)
        sentences = [s.strip() for s in story.split('.') if s.strip()]
        for sentence in sentences:
            txt_clip = TextClip(sentence, fontsize=40, color='white', size=(1280, 720), bg_color='black', method='caption')
            txt_clip = txt_clip.set_duration(3)
            clips.append(txt_clip)
        video = concatenate_videoclips(clips, method="compose")

        # Add audio to video
        audio_clip = AudioFileClip(audio_filename)
        video = video.set_audio(audio_clip)
        video_filename = f"static/video_{uuid.uuid4()}.mp4"
        video.write_videofile(video_filename, fps=24)

        # Clean up audio file
        os.remove(audio_filename)

        return send_file(video_filename, as_attachment=True)

    return render_template('index.html')

if __name__ == '__main__':
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(debug=True)
