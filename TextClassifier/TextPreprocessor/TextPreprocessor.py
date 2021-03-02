# -*- coding: utf-8 -*-

"""
Created on 02-March-2021
@author: Rahul Gaikwad
"""

import json as js
import string
import nltk
import wordninja
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
from nltk.tokenize import word_tokenize


class TextPreprocessor:

    def __init__(self, pobj_logger, pdict_configurations):
        """
        Params
        -----------
        pobj_logger: Logger object to log info and errors
        pdict_configurations: Dictionary(key-value pair) of configuration

        Description
        -----------
        Constructor will create all the required variables to clean the raw text.

        Return
        -----------
        """

        try:
            # ==============================================
            # Create logger object as class-level variable
            # ==============================================

            self.gobj_logger = pobj_logger

            # ======================================================================
            # Initialize some variables to preprocess raw text
            # ======================================================================

            self.SENT_DETECTOR = \
                nltk.data.load('tokenizers/punkt/english.pickle')
            self.REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
            self.BAD_SYMBOLS_RE = re.compile('[^09a-z #+_]')
            self.lemmatizer = WordNetLemmatizer()
            self.lstr_punctuations = string.punctuation
            self.llst_stop_words = set(stopwords.words('english'))
            self.lem = WordNetLemmatizer()

            # ====================================================================================
            # Assign configuration values to class-level variables
            # ====================================================================================

            self.gstr_stemmer_type = \
                str(pdict_configurations['StemmerType'])
            if self.gstr_stemmer_type == 'SnowballStemmer':
                self.stemmer = SnowballStemmer('english')
            elif self.gstr_stemmer_type == 'PorterStemmer':
                self.stemmer = PorterStemmer()

            self.gstr_contraction_file_path = \
                str(pdict_configurations['ContractionFilePath'])
            self.contractions = \
                js.load(open(self.gstr_contraction_file_path, 'r'))
        except Exception as e:

            self.gobj_logger.error(str(e))
            raise

    def do_clean_text(self, pstr_raw_lstr):
        """
        Params
        -----------
        pstr_raw_lstr: Raw text of review

        Description
        -----------
        This method will allow us to sequentially implement the 
        operations in order to clean lstr_cleaned_text.

        Return
        -----------
        lstr_cleaned_text: cleaned text
        """

        try:
            # =========================================================================
            # Split words into meaningful words if got joined.
            # Ex. "Easyapptouse" will be "Easy app to use"
            # =========================================================================

            lstr_cleaned_text = ' '.join(wordninja.split(pstr_raw_lstr))

            # =========================================================================
            # Here we expand the word contractions.
            # Ex. "he's" will be "he is / he has"
            # =========================================================================

            for word in lstr_cleaned_text.split():
                if word.lower() in self.contractions:
                    lstr_cleaned_text = lstr_cleaned_text.replace(word,
                                                                  self.contractions[word.lower()])

            # =========================================================================
            # Create tokens.
            # =========================================================================

            llst_cleaned_tokens = word_tokenize(lstr_cleaned_text)

            # =========================================================================
            # Remove stopwords.
            # =========================================================================

            llst_cleaned_tokens = [lstr_token for lstr_token in
                                   llst_cleaned_tokens if lstr_token
                                   not in self.llst_stop_words]

            # =========================================================================
            # Remove punctuations.
            # =========================================================================

            llst_cleaned_tokens_without_punct = []
            for lstr_token in llst_cleaned_tokens:
                index = [lstr_token.find(char) for char in lstr_token
                         if char not in self.lstr_punctuations]
                llst_cleaned_tokens_without_punct.append(''.join([lstr_token[i]
                                                                  for i in index]))

            # =========================================================================
            # Remove numbers.
            # =========================================================================

            llst_cleaned_tokens_without_digit = [x for x in
                                                 llst_cleaned_tokens_without_punct
                                                 if not x.isdigit()]

            # =========================================================================
            # Lemmatization.
            # =========================================================================

            llst_cleaned_tokens_lemm = [self.lem.lemmatize(t, pos='v')
                                        for t in llst_cleaned_tokens_without_digit]

            # =========================================================================
            # Stemming.
            # =========================================================================

            llst_cleaned_tokens_stemmed = [self.stemmer.stem(t)
                                           for t in llst_cleaned_tokens_lemm]

            # =========================================================================
            # Join all cleaned tokens and form a sentence.
            # =========================================================================

            lstr_cleaned_text = ' '.join(llst_cleaned_tokens_stemmed)

            return lstr_cleaned_text.strip()

        except Exception as e:

            self.gobj_logger.error(str(e))
            raise
