import unittest

from .task_contracts import (
    AudioTranscriptionRequest, EmbeddingRequest, ImageGenerationRequest,
    SpeechSynthesisRequest, VideoGenerationRequest,
)


class MultimodalTaskContractTests(unittest.TestCase):
    def test_embedding_requires_inputs(self):
        with self.assertRaises(ValueError):
            EmbeddingRequest(model="embedding-model", inputs=())

    def test_image_count_is_bounded(self):
        with self.assertRaises(ValueError):
            ImageGenerationRequest(model="image-model", prompt="landscape", count=9)

    def test_speech_requires_text(self):
        with self.assertRaises(ValueError):
            SpeechSynthesisRequest(model="tts-model", text=" ")

    def test_transcription_requires_audio_bytes(self):
        with self.assertRaises(ValueError):
            AudioTranscriptionRequest(model="asr-model", audio=b"", filename="audio.wav", content_type="audio/wav")

    def test_video_duration_must_be_positive(self):
        with self.assertRaises(ValueError):
            VideoGenerationRequest(model="video-model", prompt="city at night", duration_seconds=0)


if __name__ == "__main__":
    unittest.main()
