# -*- coding: utf-8 -*-

"""
Created on 01-March-2021
@author: Rahul Gaikwad
"""

import os

from flask import Flask, request, jsonify, render_template

from TextClassifier.TextClassifier import TextClassifier
from TextClassifier.logger.APILogger import InvalidUsage
from TextClassifier.logger.LoggerError import LoggerError
from TextClassifier.logger.logger import AuditLogger
from TextClassifier.logger.logger import Logger

app = Flask(__name__)
app.config["DEBUG"] = True

IMG_FOLDER = os.path.join('static', 'img')
app.config['IMG_FOLDER'] = IMG_FOLDER

STYLE_FOLDER = os.path.join('static', 'style')
app.config['STYLE'] = STYLE_FOLDER

JS_FOLDER = os.path.join('static', 'js')
app.config['JS'] = JS_FOLDER


@app.route('/')
def homepage():
    img_filename = os.path.join(app.config['IMG_FOLDER'], 'logo.png')
    style_filename = os.path.join(app.config['STYLE'], 'form-validation.css')
    js_filename = os.path.join(app.config['JS'], 'form-validation.js')
    return render_template("index.html", company_logo=img_filename, form_style=style_filename, js_filename=js_filename)


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/', methods=['POST', 'GET'])
def home():
    try:
        ldct_form_data = eval(request.form.get("FormData"))
        if ldct_form_data:
            lstr_prediction = lobj_text_classifier.do_operation(ldct_form_data)
            return jsonify({"success": True, "prediction": lstr_prediction})
        else:
            gobj_logger.error("Input is None", exc_info=True)
            raise
    except Exception:
        gobj_logger.error("Exception Raised", exc_info=True)
        raise InvalidUsage(lobj_text_classifier.gstr_default_class, status_code=410)


if __name__ == '__main__':
    try:

        # ===========================================
        # Create object of a logger
        # ===========================================

        gobj_audit_logger = AuditLogger()
        gobj_monthly_audit_logger = \
            gobj_audit_logger.monthly_audit_logger

        gobj_logger = Logger()
        gobj_logger = gobj_logger.logger

        # =======================================================================
        # Create an empty dictionary to later fill in config values
        # =======================================================================

        gdict_sections_and_dict_of_properties = {}

        gdct_path_properties = {'ModelMappingFilePath': ''}
        gdict_sections_and_dict_of_properties['Path'] = \
            gdct_path_properties

        gdct_ml_properties = {'DefaultClass': ''}
        gdict_sections_and_dict_of_properties['ML'] = \
            gdct_ml_properties

        gdct_nlp_properties = {'StemmerType': '', 'ContractionFilePath': ''}
        gdict_sections_and_dict_of_properties['NLP'] = \
            gdct_nlp_properties

        # create object of TextClassifier

        lobj_text_classifier = \
            TextClassifier(gdict_sections_and_dict_of_properties,
                           gobj_logger, gobj_monthly_audit_logger)

        # calling main method of TextClassifier

        lobj_text_classifier.main()

        app.run(host='0.0.0.0', debug=True, use_reloader=False)

    except LoggerError as logger_error:
        print(logger_error)

    except Exception:
        print("ERROR")
        gobj_logger.error("Exception Raised", exc_info=True)
