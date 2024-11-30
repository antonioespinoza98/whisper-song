import logging
import sys
import os
from typing import Union
from threading import Lock
import torch
import whisper

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

logger = get_logger('whisper-core')

model_name = os.getenv("ASR_MODEL", "base")

try:
    if torch.cuda.is_available():
        logger.debug("Running on GPU")
        model = whisper.load_model(model_name).cuda()
    else:
        logger.debug("Running on CPU")
        model = whisper.load_model(model_name)
except Exception as e:
    logger.error(f"Error loading model: {e}")
    sys.exit(1)

model_lock = Lock()

def transcribe(
    audio,
    task: Union[str, None] = None,
    language: Union[str, None] = None,
):
    options_dict = {}
    if task:
        options_dict["task"] = task
    if language:
        options_dict["language"] = language
    with model_lock:
        try:
            result = model.transcribe(audio, **options_dict)
        except Exception as e:
            logger.error(f"Error during transcription: {e}")
            raise e
    return result
