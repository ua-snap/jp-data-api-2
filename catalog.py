data_catalog = {
    #############################
    "geospatial": {
        "request_parameters": {
            "required": {
                "geom_type": "geometry type (e.g. type=point)",
                "category": "category ID (e.g. category=communities)",
                "source": "source ID (e.g. source=US Census)",
                "loc": "a community or place ID (e.g. loc=AK124), area id (e.g. loc=19080201), or stream ID (e.g. loc=123456789)",
            },
            "optional": {},
        },
        "geom_type": {
            "point": {
                "category": {
                    "communities": {
                        "source": {
                            "US Census": {
                                "metadata": {
                                    "description": "US Census-defined communities",
                                    "bbox": [-180, 50, 180, 90],
                                    "coverage_id": "US_Census_communities_coverage",
                                },
                            },
                            "CAN Census": {
                                "metadata": {
                                    "description": "Census-defined communities in Canada",
                                    "bbox": [-180, 50, 180, 90],
                                    "coverage_id": "CAN_Census_communities_coverage",
                                },
                            },
                        },
                    },
                },
            },
            "polygon": {
                "category": {
                    "watersheds": {
                        "source": {
                            "NHD_HUC6": {
                                "metadata": {
                                    "description": "Level 6 Watershed boundaries from the National Hydrography Dataset",
                                    "bbox": [-180, 50, 180, 90],
                                    "coverage_id": "NHD_HUC6_coverage",
                                },
                            },
                            "NHD_HUC8": {
                                "metadata": {
                                    "description": "Level 8 Watershed boundaries from the National Hydrography Dataset",
                                    "bbox": [-180, 50, 180, 90],
                                    "coverage_id": "NHD_HUC8_coverage",
                                },
                            },
                        },
                    },
                    "protected_areas": {
                        "source": {
                            "NPS": {
                                "metadata": {
                                    "description": "National Park Service boundaries",
                                    "bbox": [-180, 50, 180, 90],
                                    "coverage_id": "NPS_coverage",
                                },
                            },
                        },
                    },
                },
            },
            "line": {
                "category": {
                    "streams": {
                        "source": {
                            "MERIT": {
                                "metadata": {
                                    "description": "Global Rivers dataset from MERIT",
                                    "bbox": [-180, 50, 180, 90],
                                    "coverage_id": "MERIT_coverage",
                                },
                            },
                            "NHD": {
                                "metadata": {
                                    "description": "National Hydrography Dataset",
                                    "bbox": [-180, 50, 180, 90],
                                    "coverage_id": "NHD_coverage",
                                },
                            },
                        },
                    },
                },
            },
        },
    },
    #############################
    "hydrosphere": {
        "request_parameters": {
            "required": {
                "vars": "one or more variable IDs, separated by a comma (e.g. vars=pr,t2)",
                "source": "a source IDs (e.g. source=ERA5)",
                "loc": "a community ID (e.g. loc=AK124) or a lat/lon pair separated by a comma (e.g. loc=64.8,-147.7)",
            },
            "optional": {
                "years": "a range of years separated by a comma (e.g. years=2015,2016)",
            },
        },
        "variables": {
            "pr": {
                "name": "precipitation",
                "source": {
                    "ERA5": {
                        "metadata": {
                            "model": None,
                            "scenario": None,
                            "frequency": ["monthly", "yearly", "decadal"],
                            "time": {
                                "start_year": 1950,
                                "end_year": 2015,
                            },
                            "units": "mm",
                            "bbox": [-180, 50, 180, 90],
                            "coverage_id": "ERA5_pr_coverage",
                        },
                    },
                    "CMIP5": {
                        "metadata": {
                            "model": ["GFDL-ESM2M", "CCSM4", "MIROC5"],
                            "scenario": ["rcp45", "rcp60", "rcp85"],
                            "frequency": ["monthly", "yearly"],
                            "time": {
                                "start_year": 1950,
                                "end_year": 2100,
                            },
                            "units": "mm",
                            "bbox": [-180, 50, 180, 90],
                            "coverage_id": "CMIP5_pr_coverage",
                        },
                    },
                    "CMIP6": {
                        "metadata": {
                            "model": ["GFDL-ESM4", "MIROC6", "NorESM2-LM"],
                            "scenario": ["ssp126", "ssp245", "ssp370", "ssp585"],
                            "frequency": ["monthly", "yearly"],
                            "time": {
                                "start_year": 1950,
                                "end_year": 2100,
                            },
                            "units": "mm",
                            "bbox": [-180, 50, 180, 90],
                            "coverage_id": "CMIP6_pr_coverage",
                        },
                    },
                    "CMIP7": {
                        "metadata": {
                            "model": ["GFDL-ESM-999", "MIROC7"],
                            "scenario": ["a", "b", "c"],
                            "frequency": ["monthly", "yearly"],
                            "time": {
                                "start_year": 1980,
                                "end_year": 2125,
                            },
                            "units": "mm",
                            "bbox": [-180, 50, 180, 90],
                            "coverage_id": "CMIP7_pr_coverage",
                        },
                    },
                },
            },
        },
    },
    #############################
    "atmosphere": {
        "request_parameters": {
            "required": {
                "vars": "one or more variable IDs, separated by a comma (e.g. vars=pr,t2)",
                "source": "a source IDs (e.g. source=ERA5)",
                "loc": "a community ID (e.g. loc=AK124) or a lat/lon pair separated by a comma (e.g. loc=64.8,-147.7)",
            },
            "optional": {
                "years": "a range of years separated by a comma (e.g. years=2015,2016)",
            },
        },
        "variables": {
            "t2": {
                "name": "air temperature at 2m",
                "source": {
                    "ERA5": {
                        "metadata": {
                            "model": None,
                            "scenario": None,
                            "frequency": ["monthly", "yearly", "decadal"],
                            "time": {
                                "start_year": 1950,
                                "end_year": 2015,
                            },
                            "units": "C",
                            "bbox": [-180, 50, 180, 90],
                            "coverage_id": "ERA5_t2_coverage",
                        },
                    },
                    "CMIP5": {
                        "metadata": {
                            "model": ["GFDL-ESM2M", "CCSM4", "MIROC5"],
                            "scenario": ["rcp45", "rcp60", "rcp85"],
                            "frequency": ["monthly", "yearly"],
                            "time": {
                                "start_year": 1950,
                                "end_year": 2100,
                            },
                            "units": "C",
                            "bbox": [-180, 50, 180, 90],
                            "coverage_id": "CMIP5_t2_coverage",
                        },
                    },
                    "CMIP6": {
                        "metadata": {
                            "model": ["GFDL-ESM4", "MIROC6", "NorESM2-LM"],
                            "scenario": ["ssp126", "ssp245", "ssp370", "ssp585"],
                            "frequency": ["monthly", "yearly"],
                            "time": {
                                "start_year": 1950,
                                "end_year": 2100,
                            },
                            "units": "C",
                            "bbox": [-180, 50, 180, 90],
                            "coverage_id": "CMIP6_t2_coverage",
                        },
                    },
                    "CMIP7": {
                        "metadata": {
                            "model": ["GFDL-ESM-999", "MIROC7"],
                            "scenario": ["a", "b", "c"],
                            "frequency": ["monthly", "yearly"],
                            "time": {
                                "start_year": 1980,
                                "end_year": 2125,
                            },
                            "units": "C",
                            "bbox": [-180, 50, 180, 90],
                            "coverage_id": "CMIP7_t2_coverage",
                        },
                    },
                },
            },
            "clt": {
                "name": "cloud cover",
                "source": {
                    "ERA5": {
                        "metadata": {
                            "model": None,
                            "scenario": None,
                            "frequency": ["monthly", "yearly", "decadal"],
                            "time": {
                                "start_year": 1950,
                                "end_year": 2015,
                            },
                            "units": "%",
                            "bbox": [-180, 50, 180, 90],
                            "coverage_id": "ERA5_clt_coverage",
                        },
                    },
                    "CMIP6": {
                        "metadata": {
                            "model": ["GFDL-ESM4", "MIROC6", "NorESM2-LM"],
                            "scenario": ["ssp126", "ssp245", "ssp370", "ssp585"],
                            "frequency": ["monthly", "yearly"],
                            "time": {
                                "start_year": 1950,
                                "end_year": 2100,
                            },
                            "units": "%",
                            "bbox": [-180, 50, 180, 90],
                            "coverage_id": "CMIP6_clt_coverage",
                        },
                    },
                    "CMIP7": {
                        "metadata": {
                            "model": ["GFDL-ESM-999", "MIROC7"],
                            "scenario": ["a", "b", "c"],
                            "frequency": ["monthly", "yearly"],
                            "time": {
                                "start_year": 1980,
                                "end_year": 2125,
                            },
                            "units": "%",
                            "bbox": [-180, 50, 180, 90],
                            "coverage_id": "CMIP7_clt_coverage",
                        },
                    },
                },
            },
        },
    },
}
