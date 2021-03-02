# -*- coding: utf-8 -*-

"""
Created on 02-March-2021
@author: Rahul Gaikwad
"""

import statistics


class ModelPredictor:

    def __init__(
            self,
            pobj_logger,
            pdict_configurations,
            pdct_loaded_model_mapping,
    ):
        """
        Params
        -----------
        pobj_logger: Logger object to log info and errors
        pdict_configurations: Dictionary(key-value pair) of configuration
        pdct_loaded_model_mapping: Dictionary of loaded models
        
        Description
        -----------
        Constructor will create all the required variables to predict the text.

        Return
        -----------
        """

        try:

            # ====================================================================================
            # Create logger object as class-level variable
            # ====================================================================================

            self.gobj_logger = pobj_logger
            self.gdct_loaded_model_mapping = pdct_loaded_model_mapping

            # ====================================================================================
            # Assign configuration values to class-level variables
            # ====================================================================================

            self.gstr_default_class = \
                str(pdict_configurations['DefaultClass'])

        except Exception as e:

            self.gobj_logger.error(str(e))
            raise

    def get_prediction(self, pstr_clean_text):
        """
        Params
        -----------
        pstr_clean_text: cleaned form of review

        Description
        -----------
        This method will allow us to implement the instruction 
        to get the prediction from all the ML models.

        Return
        -----------
        ldct_model_name_model_prediction: Dictionary of prediction from all the models
        """

        try:

            ldct_model_name_model_prediction = {}

            # =========================================================================
            # Get supervised models for further prediction
            # =========================================================================

            ldct_supervised_models = \
                self.gdct_loaded_model_mapping['Supervised_models']

            # =========================================================================
            # Make prediction using all models,
            # and create mapping of models and predictions.
            # =========================================================================

            for (lstr_model_name, lobj_pre_build_model) in \
                    ldct_supervised_models.items():
                ldct_model_name_model_prediction[lstr_model_name] = \
                    lobj_pre_build_model.predict([pstr_clean_text])[0]

            # =========================================================================
            # Using above mapping, get max votted result to get final prediction.
            # =========================================================================
            pbol_is_outlier_prediction = False
            lstr_max_voted_prediction = \
                self.get_max_voted_prediction(pbol_is_outlier_prediction, ldct_model_name_model_prediction)

            return lstr_max_voted_prediction

        except Exception as e:

            self.gobj_logger.error(str(e))
            raise

    def get_max_voted_prediction(self,
                                 pbol_is_outlier_prediction, pdct_model_name_model_prediction):
        """
        Params
        -----------
        pdct_model_name_model_prediction: Dictionary of model name and their predictions

        Description
        -----------
        This method will allow us to get max voted predition using statistical mode.

        Return
        -----------
        lstr_max_voted_prediction: Max voted prediction.
        """

        try:
            lstr_max_voted_prediction = ''

            # =========================================================================
            # Create a list of all the predictions
            # =========================================================================

            llst_predictions = [lstr_prediction for (lstr_model_name,
                                                     lstr_prediction) in
                                pdct_model_name_model_prediction.items()]

            # =========================================================================
            # Use statistics mode (ensemble method) to get max voted prediction
            # =========================================================================

            lstr_max_voted_prediction = \
                statistics.mode(llst_predictions)

            return lstr_max_voted_prediction

        except Exception as e:

            self.gobj_logger.error(str(e))
            raise
