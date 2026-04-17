import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Unit tests for emotion detection function."""

    def test_joy_emotion(self):
        """Test detection of joy emotion."""
        statement = "I am glad this happened"
        result = emotion_detector(statement)
        self.assertIsNotNone(result)
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger_emotion(self):
        """Test detection of anger emotion."""
        statement = "I am really mad about this"
        result = emotion_detector(statement)
        self.assertIsNotNone(result)
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_emotion(self):
        """Test detection of disgust emotion."""
        statement = "I feel disgusted just hearing about this"
        result = emotion_detector(statement)
        self.assertIsNotNone(result)
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness_emotion(self):
        """Test detection of sadness emotion."""
        statement = "I am so sad about this"
        result = emotion_detector(statement)
        self.assertIsNotNone(result)
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear_emotion(self):
        """Test detection of fear emotion."""
        statement = "I am really afraid that this will happen"
        result = emotion_detector(statement)
        self.assertIsNotNone(result)
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_result_format(self):
        """Test that the result has the correct format."""
        statement = "I am glad this happened"
        result = emotion_detector(statement)
        self.assertIsNotNone(result)

        # Check that all required keys are present
        required_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']
        for key in required_keys:
            self.assertIn(key, result)

        # Check that emotion scores are numeric
        for emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness']:
            self.assertIsInstance(result[emotion], (int, float))

        # Check that dominant_emotion is a string
        self.assertIsInstance(result['dominant_emotion'], str)


if __name__ == '__main__':
    unittest.main()
