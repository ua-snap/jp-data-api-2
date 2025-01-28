from catalog import data_catalog


def validate_required_and_optional_args(service_category, args):
    args = list(args.keys())
    required_args = data_catalog[service_category]["request_parameters"][
        "required"
    ].keys()

    optional_args = data_catalog[service_category]["request_parameters"][
        "optional"
    ].keys()

    if not args:
        return (
            f"No arguments provided! The following arguments are required: {required_args}",
            400,
        )

    for required_arg in required_args:
        if required_arg not in args:
            return f"Missing required argument: {required_arg}", 400

    for arg in args:
        if arg not in required_args and arg not in optional_args:
            return f"Invalid argument: {arg}", 400

    else:
        return None


def validate_args_against_catalog(service_category, args):
    # check that the categorical values for each arg are valid for the service category
    # geospatial service category has different validation requirements
    if service_category == "geospatial":
        geom_type = args.get("geom_type").split(",")
        category = args.get("category").split(",")
        source = args.get("source").split(",")
        loc = args.get("loc")

        # only one geom_type, source, and category is allowed right now
        if len(geom_type) > 1:
            return (
                f"Only one geom_type is allowed. Choose one of {list(data_catalog[service_category]['geom_type'].keys())}",
                400,
            )
        if len(category) > 1:
            return (
                f"Only one category is allowed. Choose one of {list(data_catalog[service_category]['geom_type'][geom_type[0]]['category'].keys())}",
                400,
            )
        if len(source) > 1:
            return (
                f"Only one source is allowed. Choose one of {list(data_catalog[service_category]['geom_type'][geom_type[0]]['category'][category[0]]['source'].keys())}",
                400,
            )

        if geom_type[0] not in data_catalog[service_category]["geom_type"]:
            return (
                f"Invalid geom_type: {geom_type[0]}. Must be one of {list(data_catalog[service_category]['geom_type'].keys())}",
                400,
            )
        if (
            category[0]
            not in data_catalog[service_category]["geom_type"][geom_type[0]]["category"]
        ):
            return (
                f"Invalid category: {category[0]}. Must be one of {list(data_catalog[service_category]['geom_type'][geom_type[0]]['category'].keys())}",
                400,
            )
        if (
            source[0]
            not in data_catalog[service_category]["geom_type"][geom_type[0]][
                "category"
            ][category[0]]["source"]
        ):
            return (
                f"Invalid source: {source[0]}. Must be one of {list(data_catalog[service_category]['geom_type'][geom_type[0]]['category'][category[0]]['source'].keys())}",
                400,
            )

        # TODO: validate loc using bbox for each geom_type and source

        return None

    # non-geospatial service categories should all be identical in terms of validation
    else:
        vars = args.get("vars").split(",")
        source = args.get("source").split(",")
        loc = args.get("loc")

        # only one source is allowed right now
        if len(source) > 1:
            return (
                f"Only one source per request is allowed at this time. Choose one of {list(data_catalog[service_category]['source'].keys())}",
                400,
            )

        # check that the vars are valid for the service category
        for var in vars:
            if var not in data_catalog[service_category]["variables"]:
                return (
                    f"Invalid variable ID: {var}. Must be one of {list(data_catalog[service_category]['variables'].keys())}",
                    400,
                )
        # check that the source is valid for each var
        for var in vars:
            if (
                source[0]
                not in data_catalog[service_category]["variables"][var]["source"]
            ):
                return (
                    f"Invalid source ID: {source[0]}. Must be one of {list(data_catalog[service_category]['variables'][var]['source'].keys())}",
                    400,
                )

        # year range gets validated if it is present
        if args.get("years"):
            years = args.get("years").split(",")
            err = validate_years_arg(service_category, vars, source, years)
            if err:
                return err

        # TODO: validate other optional args for each var and source
        # TODO: validate loc using bbox for each var and source

        return None


def validate_years_arg(service_category, vars, source, years):

    if len(years) != 2:
        return (
            f"Invalid year range: years argument should be in the format YYYY,YYYY, e.g. years=1990,2020",
            400,
        )
    if not years[0].isdigit() or not years[1].isdigit():
        return (
            f"Invalid year range: years argument should be in the format YYYY,YYYY, e.g. years=1990,2020",
            400,
        )
    if len(years[0]) != 4 or len(years[1]) != 4:
        return (
            f"Invalid year range: years argument should be in the format YYYY,YYYY, e.g. years=1990,2020",
            400,
        )
    if int(years[0]) > int(years[1]):
        return (
            f"Invalid year range: start year should be less than end year, e.g. years=1990,2020",
            400,
        )

    # for each variable, use catalog to validate years for the source
    for var in vars:
        source_start_year = data_catalog[service_category]["variables"][var]["source"][
            source
        ]["metadata"]["time"]["start_year"]
        source_end_year = data_catalog[service_category]["variables"][var]["source"][
            source
        ]["metadata"]["time"]["end_year"]
        if int(years[0]) < source_start_year or int(years[1]) > source_end_year:
            return (
                f"Invalid year range for variable {var} and source {source}: data is available for years {source_start_year} - {source_end_year}",
                400,
            )
    else:
        return None
