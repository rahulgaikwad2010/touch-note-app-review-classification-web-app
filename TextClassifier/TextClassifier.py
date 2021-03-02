# -*- coding: utf-8 -*-

"""
Created on 01-March-2021
@author: Rahul Gaikwad
"""

import json as js
import pickle
import warnings

from .ModelPredictor.ModelPredictor import ModelPredictor
from .TextPreprocessor.TextPreprocessor import TextPreprocessor
from .common_operations.common_operations import CommonOperations

warnings.filterwarnings('ignore')


class TextClassifier:

    def __init__(
            self,
            pdict_sections_and_dict_of_properties,
            pobj_logger,
            pobj_monthly__audit_logger,
    ):
        try:

            # ===================================================================
            # Create class-variable of logger
            # ===================================================================

            self.gobj_logger = pobj_logger
            self.gobj_monthly_audit_logger = pobj_monthly__audit_logger

            # ===================================================================
            # Read configuration using dedicated method from CommonOperation
            # and fill the dictionary
            # ===================================================================

            self.gobj_common_operations = \
                CommonOperations(self.gobj_logger)
            self.gdict_configurations = \
                self.gobj_common_operations.read_allconfigproperties(pdict_sections_and_dict_of_properties,
                                                                     'config.ini')

            # ===================================================================
            # Assign config values to class-level variables
            # ===================================================================

            self.gstr_model_mapping_file_path = \
                str(self.gdict_configurations['ModelMappingFilePath'])
            self.gdct_model_mapping = \
                js.load(open(self.gstr_model_mapping_file_path, 'r'))
            self.gstr_default_class = \
                str(self.gdict_configurations['DefaultClass'])

        except Exception as e:

            self.gobj_logger.error(str(e))
            raise

    def do_operation(self, pdct_form_data):
        """
        Params
        -----------
        pdct_form_data:
        Form data submitted in front end

        Description
        -----------
        This method will implement the actual algorithm of predicting sentiment
        and logging for further analysis.

        Return
        -----------
        lstr_max_voted_prediction: predicted class
        Ex. positive
        """

        try:

            lstr_cleaned_text = ''

            # ================================================
            # Extract values from form_data dictionary
            # ================================================
            lstr_title = pdct_form_data['title']
            lstr_review = pdct_form_data['review']

            # ================================================
            # Call do_clean_text method to get cleaned data
            # ================================================

            lstr_cleaned_text = self.gobj_text_preprocessor.do_clean_text(lstr_review.strip())

            if lstr_cleaned_text:
                # ================================================
                # Call get_prediction method to all prediction
                # ================================================
                lstr_max_voted_prediction = \
                    self.gobj_model_predictor.get_prediction(lstr_cleaned_text)

            else:
                lstr_max_voted_prediction = self.gstr_default_class

        except Exception as e:

            self.gobj_logger.error(str(e))
            lstr_max_voted_prediction = self.gstr_default_class

        self.gobj_monthly_audit_logger.info(lstr_title + ','
                                            + lstr_review + ','
                                            + lstr_cleaned_text + ','
                                            + lstr_max_voted_prediction)

        return lstr_max_voted_prediction

    def load_model(self, pdct_model_mapping):
        """
        Params
        -----------
        pdct_model_mapping: 
        Ex. {
                "SVM": {
                    "path": ""
                },
                ...
            }

        Description
        -----------
        Method will load all the required model present in the model mapping file.
        So that, prediction can be done on loaded model.

        Return
        -----------
        ldct_loaded_model_mapping:
        Ex. {
                "SVM": object of svm model,
                ...
            }
        """

        try:

            # =========================================================================
            # Create empty dictionaries to fill models in it.
            # =========================================================================

            ldct_loaded_model_mapping = {}
            ldct_supervised_loaded_model_mapping = {}

            # =========================================================================
            # Assign supervised model mapping
            # to separate dictionaries
            # =========================================================================

            ldct_supervised_models = \
                pdct_model_mapping['Supervised_models']

            # =========================================================================
            # Load supervised models into memory and
            # fill it into newly created dictionary
            # =========================================================================

            for (lstr_model_name, ldct_model_meta_data) in \
                    ldct_supervised_models.items():
                ldct_supervised_loaded_model_mapping[lstr_model_name] = \
                    pickle.load(open(ldct_model_meta_data['path'], 'rb'))

            ldct_loaded_model_mapping['Supervised_models'] = \
                ldct_supervised_loaded_model_mapping

            return ldct_loaded_model_mapping

        except Exception as e:
            self.gobj_logger.error('MethodName : load_required_model')
            raise

    def main(self):
        """
        Description
        -----------
        Method will collect all basic common requirements to process the input.
        """

        try:

            # ===================================================================
            # Create TextPreprocessor object
            # ===================================================================

            self.gobj_text_preprocessor = TextPreprocessor(self.gobj_logger,
                                                           self.gdict_configurations)

            # ===================================================================
            # Load required models
            # ===================================================================

            ldct_loaded_model_mapping = \
                self.load_model(self.gdct_model_mapping)

            # ===================================================================
            # Create ModelPredictor object
            # ===================================================================

            self.gobj_model_predictor = ModelPredictor(self.gobj_logger,
                                                       self.gdict_configurations,
                                                       ldct_loaded_model_mapping)

            # ===================================================================
            # Create heading row in Audit Log
            # ===================================================================
            self.gobj_monthly_audit_logger.info('Title,Review,Cleaned Review,Predicton')

        except Exception as e:

            self.gobj_logger.error('MethodName : main')
            raise
