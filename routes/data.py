import asyncio
import ast
from flask import Blueprint, render_template, request

from catalog import data_catalog
from validation import (
    validate_required_and_optional_args,
    validate_args_against_catalog,
    validate_years_arg,
)
from fetch import fetch_data_from_coverage
from . import routes


@routes.route("/data/<service_category>/")
def get_data(service_category):

    ###### VALIDATION BLOCK ######
    if service_category not in data_catalog.keys():
        return (
            f"Invalid service category ID. Must be one of {list(data_catalog.keys())}",
            400,
        )

    # get all args and check catalog to make sure they are within required + optional lists
    err = validate_required_and_optional_args(service_category, request.args)
    if err:
        return err
    # at this point all required args are present, and any optional args are allowed
    # now we can validate each specific arg against allowable values defined in the catalog
    err = validate_args_against_catalog(service_category, request.args)
    if err:
        return err

    ###### END VALIDATION BLOCK ######

    ###### DATA FETCH BLOCK ######

    # TODO: fetch real data using vars, source, loc + optional args and return JSON
    data = fetch_data_from_coverage(service_category, request.args)
    return (
        "Passed validation! Time to go fetch some data. This request would get data from coverage id(s): "
        + str(data)
    )

    ###### END DATA FETCH BLOCK ######
