import os
from flask import Blueprint, redirect

routes = Blueprint("routes", __name__)

from .about import *
from .data import *
