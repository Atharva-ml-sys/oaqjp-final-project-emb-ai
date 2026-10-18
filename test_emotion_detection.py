
"""Unit tests for the emotion detector."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test emotion detection results and error handling."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy_is_dominant(self, mock_post):
        """Joy should be dominant when its score is highest."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.01,
                        "disgust": 0.02,
                        "fear": 0.03,
                        "joy": 0.90,
                        "sadness": 0.04,
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I am very happy today")

        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["joy"], 0.90)

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_sadness_is_dominant(self, mock_post):
        """Sadness should be dominant when its score is highest."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.01,
                        "disgust": 0.02,
                        "fear": 0.03,
                        "joy": 0.04,
                        "sadness": 0.90,
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I feel very sad")

        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_empty_input(self):
        """Empty input should return no emotion scores."""
        result = emotion_detector("")

        self.assertIsNone(result["dominant_emotion"])
        self.assertIsNone(result["joy"])


if __name__ == "__main__":
    unittest.main()
