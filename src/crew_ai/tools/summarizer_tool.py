"""
This module provides a summarization tool for the BlogAgentBoiler framework.
It uses basic natural language processing techniques to summarize text by extracting
the most important sentences based on word frequencies.

This can be extended or replaced with more advanced summarization models (e.g., using transformers).
"""

# Importing necessary libraries
from crewai_tools import BaseTool  # Inherited base class for tools
from typing import Optional
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import nltk


class TextSummarizeTool(BaseTool):
    """
    TextSummarizeTool is a simple text summarization tool that extracts the most important sentences
    from a given text. It uses sentence tokenization, stopword removal, and frequency distribution
    to score and select sentences for the summary.

    This class can be extended to use more sophisticated models such as transformers, abstractive
    summarizers, or custom algorithms.
    """

    # Name and description for the tool, helpful for agent tool selection
    name: str = "Text Summarization Tool"
    description: str = (
        "Summarizes a given text by extracting the most important sentences."
    )

    def __init__(self):
        """
        Initializes the tool by downloading necessary NLTK data (stopwords, tokenizer).
        This setup ensures that NLTK's pre-trained resources are available for summarization.
        """
        super().__init__()
        nltk.download("punkt", quiet=True)  # Sentence tokenizer
        nltk.download("stopwords", quiet=True)  # Stopword list

    def _run(self, text: str, num_sentences: Optional[int] = 3) -> str:
        """
        Runs the summarization process on the input text, extracting the most important sentences.

        Parameters:
        - text: The input text to be summarized.
        - num_sentences: The number of sentences to return in the summary (default is 3).

        Returns:
        A string containing the summary, which consists of the most relevant sentences in the text.
        """

        # Tokenize the text into sentences
        sentences = sent_tokenize(text)

        # Tokenize words and remove stopwords
        stop_words = set(stopwords.words("english"))
        words = word_tokenize(text.lower())  # Convert to lowercase for uniformity
        filtered_words = [
            word for word in words if word.isalnum() and word not in stop_words
        ]  # Remove stopwords

        # Calculate word frequencies
        word_frequencies = FreqDist(filtered_words)

        # Score sentences based on word frequencies
        sentence_scores = {}
        for i, sentence in enumerate(sentences):
            for word in word_tokenize(sentence.lower()):
                if word in word_frequencies:
                    if i in sentence_scores:
                        sentence_scores[i] += word_frequencies[word]
                    else:
                        sentence_scores[i] = word_frequencies[word]

        # Get the top n sentences with the highest scores
        top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[
            :num_sentences
        ]

        # Combine the top sentences in their original order
        summary = " ".join([sentences[i] for i in sorted(top_sentences)])

        return summary
