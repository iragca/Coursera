"""Unit tests for the emotion detection module.

This script contains unit tests for the `emotion_detector` function 
from the `emotion_detection` module. The tests validate the accuracy 
of the emotion detection functionality by comparing its output against 
expected emotion labels for various input texts.
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """Test class for the emotion detection functionality.

    This class contains test cases for the `emotion_detector` function. Each 
    test checks the ability of the function to correctly predict the dominant 
    emotion for a given input text.
    """

    def test_emotion_detector(self):
        """Test the `emotion_detector` function for various emotional inputs.

        This test checks the following scenarios:
        - Input with a joyful emotion should return "joy".
        - Input with an angry emotion should return "anger".
        - Input with a disgusted emotion should return "disgust".
        - Input with a sad emotion should return "sadness".
        - Input with a fearful emotion should return "fear".
        
        The test compares the detected emotion (converted to lowercase) with 
        the expected emotion label.
        """

        # Test case: Joy
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'].lower(), 'joy')

        # Test case: Anger
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'].lower(), 'anger')

        # Test case: Disgust
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotion'].lower(), 'disgust')

        # Test case: Sadness
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'].lower(), 'sadness')

        # Test case: Fear
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant_emotion'].lower(), 'fear')

if __name__ == '__main__':
    unittest.main()
