"""Unit tests for the sentiment_analysis module.

This module contains tests for the `sentiment_analyzer` function
defined in `sentiment_analysis.py`. It verifies the correctness
of sentiment analysis predictions for positive, negative, and 
neutral inputs.
"""

import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):
    """Unit test class for the SentimentAnalyzer module.

    This class contains test cases for the `sentiment_analyzer` function
    to ensure it correctly identifies the sentiment of text inputs.
    """

    def test_sentiment_analyzer(self):
        """Test the `sentiment_analyzer` function.

        This test evaluates the function's ability to analyze sentiment
        for various types of input:
        - Positive sentiment
        - Negative sentiment
        - Neutral sentiment

        Assertions:
            - For a positive sentence, the function should return a label of 'SENT_POSITIVE'.
            - For a negative sentence, the function should return a label of 'SENT_NEGATIVE'.
            - For a neutral sentence, the function should return a label of 'SENT_NEUTRAL'.
        """
        result_1 = sentiment_analyzer('I love working with Python')
        self.assertEqual(
            result_1['label'], 'SENT_POSITIVE',
            "Expected 'SENT_POSITIVE' for positive input."
        )

        result_2 = sentiment_analyzer('I hate working with Python')
        self.assertEqual(
            result_2['label'], 'SENT_NEGATIVE',
            "Expected 'SENT_NEGATIVE' for negative input."
        )

        result_3 = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(
            result_3['label'], 'SENT_NEUTRAL',
            "Expected 'SENT_NEUTRAL' for neutral input."
        )

if __name__ == '__main__':
    unittest.main()
