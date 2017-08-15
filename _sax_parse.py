# -*- coding: utf-8 -*-
__author__ = 'Edward'
from xml.parsers.expat import ParserCreate
class WeatherSaxHandler(object):
    pass

def parse_weather(xml):
    return {
        'city': 'Beijing',
        'country': 'China',
        'today': {
            'text': 'Partly Cloudy',
            'low': 20,
            'high': 33
        },
        'tomorrow': {
            'text': 'Sunny',
            'low': 21,
            'high': 34
        }
    }
