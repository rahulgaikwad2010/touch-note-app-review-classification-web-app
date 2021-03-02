# -*- coding: utf-8 -*-

"""
Created on 02-March-2021
@author: Rahul Gaikwad
"""

import configparser
import os


class CommonOperations:
    """
    This class is used to perform common operations in CPA framework.
    """

    def __init__(self, pobj_logger):
        """
        Description
        -----------
        Constructor of CommonOperations, used to initialize class level objects.
        """
        try:
            self.gobj_logger = pobj_logger
        except Exception as e:

            self.gobj_logger.info('some Exception occurred while creating object of CommonOperations class')
            raise e

    def read_allconfigproperties(self,
                                 pdict_sections_dict_of_configurations,
                                 pstr_config_file_path):
        """
        Description
        -----------
        This method is used to read all config properties,
        """

        lstr_log_info = ''

        try:
            lstr_log_info = \
                'Method Input: \n\tpdict_sections_dict_of_configurations: ' \
                + str(pdict_sections_dict_of_configurations) \
                + '\n\tpstr_config_file_path: ' + pstr_config_file_path \
                + '\n\tpstr_execution_environment_variable_name: '

            ldict_configurations = \
                self.read_configprops_from_configfile(pdict_sections_dict_of_configurations,
                                                      pstr_config_file_path)

            lstr_log_info = lstr_log_info + '\n method output: ' \
                            + str(ldict_configurations)

            self.gobj_logger.info(lstr_log_info)

            return ldict_configurations
        except Exception as e:

            self.gobj_logger.info(lstr_log_info)
            raise e

    def read_configprops_from_configfile(self,
                                         pdict_sections_dict_of_configurations,
                                         pstr_config_file_path):
        """
        Description
        -----------
        Check config file path and read config file
        checking if a section is present then iterate on property_dictonary and
        fill all property values against their keys inside ldict_configurations using
        read_configprop(pstr_section_name, pobj_config_parser, pstr_property)
        """

        ldict_configurations = {}
        lstr_log_info = ''

        try:
            lstr_log_info = 'Method Input: \n\tpdict_configurations: ' \
                            + str(pdict_sections_dict_of_configurations) \
                            + '\n\tpstr_config_file_path: ' + pstr_config_file_path

            lbol_config_file_exists = \
                os.path.exists(pstr_config_file_path)

            if lbol_config_file_exists:
                lobj_config_parser = configparser.ConfigParser()
                lobj_config_parser.read(pstr_config_file_path)

                # ===============================================================
                # find all sections mentioned in input dictionary(i.e. keys)
                # are present in config file or not
                # ===============================================================

                if all(lobj_section_name
                       in lobj_config_parser.sections()
                       for lobj_section_name in
                       pdict_sections_dict_of_configurations.keys()):
                    for lstr_section_name in \
                            pdict_sections_dict_of_configurations.keys():

                        ldict_properties = \
                            pdict_sections_dict_of_configurations[lstr_section_name]

                        if ldict_properties:
                            for lstr_property in \
                                    ldict_properties.keys():
                                lstr_property_value = \
                                    self.read_configprop(lstr_section_name,
                                                         lobj_config_parser,
                                                         lstr_property)

                                ldict_configurations[lstr_property] = \
                                    lstr_property_value
                        else:
                            lstr_log_info = lstr_log_info \
                                            + '''Eror: 
                                            \t check input variable pdict_sections_dict_of_configuration.''' \
                                            + 'No properties are mentioned against key:' \
                                            + lstr_section_name
            else:

                lstr_log_info = lstr_log_info \
                                + '\nError: config file does not exists.'

            return ldict_configurations
        except Exception as e:

            self.gobj_logger.info(lstr_log_info)
            raise e

    def read_configprop(
            self,
            pstr_section_name,
            pobj_config_parser,
            pstr_property,
    ):
        """
        Description
        -----------
        checking if a value is present in given section.
        """

        lstr_log_info = ''

        try:
            lstr_log_info = 'Method Input: \n\tpstr_section_name: ' \
                            + pstr_section_name + '\n\tpstr_property: ' \
                            + pstr_property

            lbol_has_property = \
                pobj_config_parser.has_option(pstr_section_name,
                                              pstr_property)

            if lbol_has_property:
                lstr_property_value = \
                    pobj_config_parser[pstr_section_name][pstr_property]

                if lstr_property_value:
                    return str(lstr_property_value)
                else:
                    lstr_log_info = lstr_log_info \
                                    + '\nError: Property: [' + pstr_property \
                                    + '] is empty in properties file'
            else:
                lstr_log_info = lstr_log_info + '\nError: Property: [' \
                                + pstr_property + '] is not found' \
                                + ' in section: [' + pstr_section_name \
                                + '] in properties file'
        except Exception as e:

            self.gobj_logger.info(lstr_log_info)
            raise e
