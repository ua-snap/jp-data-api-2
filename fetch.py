from catalog import data_catalog


def fetch_data_from_coverage(service_category, args):

    # geospatial service category
    # get geom_type, category, source, loc, and optional args
    if service_category == "geospatial":
        geom_type = args.get("geom_type")
        category = args.get("category")
        source = args.get("source")
        loc = args.get("loc")
        # TODO: include optional args

        # get coverage ID from catalog
        return data_catalog[service_category]["geom_type"][geom_type]["category"][
            category
        ]["source"][source]["metadata"]["coverage_id"]

    # get vars, source, loc, and optional args
    vars = args.get("vars").split(",")
    source = args.get("source")
    loc = args.get("loc")
    # TODO: include optional args

    # get coverage IDs from catalog
    coverage_ids = []
    for var in vars:
        coverage_ids.append(
            data_catalog[service_category]["variables"][var]["source"][source][
                "metadata"
            ]["coverage_id"]
        )
    return coverage_ids
