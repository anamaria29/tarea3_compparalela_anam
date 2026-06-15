import time
import polars as pl

from feature_engineering import (
    engineer_features
)


def run_polars_pipeline(path):

    results = {}

    total_start = time.time()

    # LECTURA

    start = time.time()

    df = pl.read_csv(path)

    df = df.with_columns([

        pl.col(
            "pickup_datetime"
        )
        .str.to_datetime(),

        pl.col(
            "dropoff_datetime"
        )
        .str.to_datetime()

    ])

    results["read_time"] = (

        time.time()

        -

        start

    )

    # FEATURE ENGINEERING

    start = time.time()

    df_ml = engineer_features(df)

    results["feature_time"] = (

        time.time()

        -

        start

    )

    # FILTRADO

    start = time.time()

    filtered = (

        df_ml

        .filter(

            pl.col(
                "trip_duration"
            )

            > 300

        )

    )

    results["filter_time"] = (

        time.time()

        -

        start

    )

    # GROUP BY

    start = time.time()

    (

        filtered

        .group_by(
            "vendor_id"
        )

        .agg(

            pl.mean(
                "trip_duration"
            )

        )

    )

    results["aggregation_time"] = (

        time.time()

        -

        start

    )

    # JOIN

    start = time.time()

    stats = (

        filtered

        .group_by(
            "vendor_id"
        )

        .agg(

            pl.mean(
                "trip_duration"
            )

        )

    )

    (

        filtered

        .join(

            stats,

            on="vendor_id",

            how="left"

        )

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