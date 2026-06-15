import time

import pandas as pd

import numpy as np


def run_pandas_pipeline(path):

    results = {}

    total_start = time.time()

    # LECTURA

    start = time.time()

    df = pd.read_csv(path)

    df["pickup_datetime"] = pd.to_datetime(
        df["pickup_datetime"]
    )

    df["dropoff_datetime"] = pd.to_datetime(
        df["dropoff_datetime"]
    )

    results["read_time"] = (

        time.time()

        -

        start

    )

    # FEATURE ENGINEERING

    start = time.time()

    upper = (

        df[
            "trip_duration"
        ]

        .quantile(
            0.99
        )

    )

    df = df[

        (
            df[
                "trip_duration"
            ]

            >= 60

        )

        &

        (
            df[
                "trip_duration"
            ]

            <= upper

        )

        &

        (
            df[
                "passenger_count"
            ]

            >= 1

        )

        &

        (
            df[
                "passenger_count"
            ]

            <= 6

        )

    ]

    df["pickup_hour"] = (

        df[
            "pickup_datetime"
        ]

        .dt.hour

    )

    df["pickup_day"] = (

        df[
            "pickup_datetime"
        ]

        .dt.dayofweek

    )

    df["pickup_month"] = (

        df[
            "pickup_datetime"
        ]

        .dt.month

    )

    df["trip_distance"] = np.sqrt(

        (

            df[
                "pickup_longitude"
            ]

            -

            df[
                "dropoff_longitude"
            ]

        )**2

        +

        (

            df[
                "pickup_latitude"
            ]

            -

            df[
                "dropoff_latitude"
            ]

        )**2

    )

    results["feature_time"] = (

        time.time()

        -

        start

    )

    # FILTRO

    start = time.time()

    filtered = (

        df[
            df[
                "trip_duration"
            ]

            > 300

        ]

    )

    results["filter_time"] = (

        time.time()

        -

        start

    )

    # GROUP BY

    start = time.time()

    filtered.groupby(

        "vendor_id"

    )[

        "trip_duration"

    ].mean()

    results["aggregation_time"] = (

        time.time()

        -

        start

    )

    # JOIN

    start = time.time()

    stats = (

        filtered

        .groupby(

            "vendor_id"

        )

        [

            "trip_duration"

        ]

        .mean()

        .reset_index()

    )

    filtered.merge(

        stats,

        on="vendor_id"

    )

    results["join_time"] = (

        time.time()

        -

        start

    )

    results["total_time"] = (

        time.time()

        -

        total_start

    )

    return results