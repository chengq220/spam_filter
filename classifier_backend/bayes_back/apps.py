from django.apps import AppConfig
from .model.BayesClassifier import NaiveBayes


class BayesBackConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bayes_back'

    #initializing the model once
    MODEL = NaiveBayes("~/spam_filter/classifier_backend/bayes_back/weights")
