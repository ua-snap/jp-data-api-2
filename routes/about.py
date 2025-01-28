import asyncio
import ast
from flask import Blueprint, render_template, request

from catalog import data_catalog
from . import routes


@routes.route("/about/<service_category>/")
def about(service_category):
    # validate service category
    if service_category not in data_catalog.keys():
        return (
            f"Invalid service category ID. Must be one of {list(data_catalog.keys())}",
            400,
        )

    # validate geospatial service category
    # TODO: validate args to allow only 'geom_type' in about endpoint

    if service_category == "geospatial":
        geom_type = None
        if request.args.get("geom_type"):
            geom_type = request.args.get("geom_type").split(",")
            if len(geom_type) > 1:
                return (
                    f"Only one geom_type is allowed. Choose one of {list(data_catalog[service_category]['geom_type'].keys())}",
                    400,
                )
            if geom_type[0] not in data_catalog[service_category]["geom_type"]:
                return (
                    f"Invalid geom_type: {geom_type}. Must be one of {list(data_catalog[service_category]['geom_type'].keys())}",
                    400,
                )
            return data_catalog[service_category]["geom_type"][geom_type[0]]
        if geom_type is None:
            # list categories and sources for each geom_type
            geom_sources = {"geom_type": {}}
            for geom_type in data_catalog[service_category]["geom_type"]:
                for category in data_catalog[service_category]["geom_type"][geom_type]:
                    geom_sources["geom_type"][geom_type] = {
                        "categories": list(
                            data_catalog[service_category]["geom_type"][geom_type][
                                "category"
                            ].keys()
                        )
                    }

            return geom_sources

    # validate non-geospatial service category
    # TODO: validate args to allow only 'vars' in about endpoint

    vars = None
    if request.args.get("vars"):
        vars = request.args.get("vars").split(",")
        for var_id in vars:
            if var_id not in data_catalog[service_category]["variables"]:
                return (
                    f"Invalid variable ID: {var_id}. Must be one of {list(data_catalog[service_category]['variables'].keys())}",
                    400,
                )
        if len(vars) == 1:
            return data_catalog[service_category]["variables"][vars[0]]
        else:
            var_catalog = list(
                map(data_catalog[service_category]["variables"].get, vars)
            )
            return dict(zip(vars, var_catalog))

    if vars is None:
        vars = data_catalog[service_category]["variables"].keys()
        # list sources for each var
        var_sources = {"vars": {}}
        for var in vars:
            var_sources["vars"][var] = {
                "name": data_catalog[service_category]["variables"][var]["name"],
                "sources": list(
                    data_catalog[service_category]["variables"][var]["source"].keys()
                ),
            }
        return var_sources
