import polars as pl


def engineer_features(df):

    df_ml = df.clone()

    # FILTRADO

    upper = (
        df_ml
        .select(
            pl.col(
                "trip_duration"
            )
            .quantile(
                0.99
            )
        )
        .item()
    )

    df_ml = (

        df_ml

        .filter(
            pl.col(
                "trip_duration"
            ) >= 60
        )

        .filter(
            pl.col(
                "trip_duration"
            ) <= upper
        )

        .filter(
            pl.col(
                "passenger_count"
            ) >= 1
        )

        .filter(
            pl.col(
                "passenger_count"
            ) <= 6
        )

    )

    # MANEJO DE NULOS

    df_ml = df_ml.with_columns(

        pl.col(
            "passenger_count"
        ).fill_null(

            pl.col(
                "passenger_count"
            ).median()

        )

    )

    # FEATURES TEMPORALES

    df_ml = df_ml.with_columns([

        pl.col(
            "pickup_datetime"
        )
        .dt.hour()
        .alias(
            "pickup_hour"
        ),

        pl.col(
            "pickup_datetime"
        )
        .dt.weekday()
        .alias(
            "pickup_day"
        ),

        pl.col(
            "pickup_datetime"
        )
        .dt.month()
        .alias(
            "pickup_month"
        )

    ])

    # DISTANCIA

    df_ml = df_ml.with_columns([

        (

            (

                pl.col(
                    "pickup_longitude"
                )

                -

                pl.col(
                    "dropoff_longitude"
                )

            )

            .pow(2)

            +

            (

                pl.col(
                    "pickup_latitude"
                )

                -

                pl.col(
                    "dropoff_latitude"
                )

            )

            .pow(2)

        )

        .sqrt()

        .alias(
            "trip_distance"
        )

    ])

    # GROUP BY

    vendor_stats = (

        df_ml

        .group_by(
            "vendor_id"
        )

        .agg([

            pl.mean(
                "trip_duration"
            )
            .alias(
                "vendor_avg_duration"
            )

        ])

    )

    # JOIN

    df_ml = (

        df_ml

        .join(

            vendor_stats,

            on="vendor_id",

            how="left"

        )

    )

    # CATEGORICA

    df_ml = df_ml.with_columns([

        pl.when(

            pl.col(
                "store_and_fwd_flag"
            )

            == "Y"

        )

        .then(1)

        .otherwise(0)

        .alias(
            "store_and_fwd_flag"
        )

    ])

    return df_ml