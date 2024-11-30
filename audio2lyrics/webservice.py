import logging
import sys
import numpy as np
import ffmpeg
from fastapi import FastAPI, UploadFile, File
from whisper import tokenizer
from core import transcribe
import json

# Logging
def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(
            logging.Formatter(
                '%(name)s [%(asctime)s] [%(levelname)s] %(message)s'
            )
        )
        logger.addHandler(handler)
    return logger

logger = get_logger('whisper-fast-api')

LANGUAGE_CODES = sorted(list(tokenizer.LANGUAGES.keys()))

app = FastAPI()

@app.post("/asr", tags=["Endpoints"])
async def asr(
    file: UploadFile = File(...),
    task: str = None,
    language: str = None
):
    try:
        contents = await file.read()
        audio = load_audio(contents)
        transcription_result = transcribe(audio, task, language)
        transcription_text = transcription_result.get('text', '')
        logger.info(f"Transcription result: {transcription_text}")
    except Exception as e:
        logger.error(f"Error during transcription: {e}")
        return {"error": str(e)}

    return {"transcription": transcription_text}

def load_audio(contents: bytes, sr: int = 16000):
    """
    Load audio data from bytes and convert to mono waveform, resampling as necessary.
    Parameters
    ----------
    contents: bytes
        The content of the audio file.
    sr: int
        The sample rate to resample the audio if necessary.
    Returns
    -------
    A NumPy array containing the audio waveform, in float32 dtype.
    """
    try:
        # Decode audio using ffmpeg
        out, _ = (
            ffmpeg.input('pipe:', threads=0)
            .output(
                'pipe:',
                format='s16le',
                acodec='pcm_s16le',
                ac=1,
                ar=sr
            )
            .run(
                cmd='ffmpeg',
                capture_stdout=True,
                capture_stderr=True,
                input=contents
            )
        )
    except ffmpeg.Error as e:
        logger.error(f"Failed to load audio: {e.stderr.decode()}")
        raise RuntimeError(f"Failed to load audio: {e.stderr.decode()}") from e

    return np.frombuffer(out, np.int16).astype(np.float32) / 32768.0
