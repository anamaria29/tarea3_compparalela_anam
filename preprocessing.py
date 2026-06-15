import polars as pl

from sklearn.model_selection import train_test_split


def preprocess_data(df):

    df_ml = df.clone()

    # ELIMINAR COLUMNAS

    drop_cols = [

        "id",

        "pickup_datetime",

        "dropoff_datetime"

    ]

    df_ml = (

        df_ml

        .drop(
            drop_cols
        )

    )

    # TARGET

    target = (

        "trip_duration"

    )

    X = (

        df_ml

        .drop(
            target
        )

    )

    y = (

        df_ml

        .select(
            target
        )

        .to_numpy()

        .ravel()

    )

    # A NUMPY

    X = (

        X

        .to_numpy()

    )

    # SPLIT

    (

        X_train,

        X_test,

        y_train,

        y_test

    ) = (

        train_test_split(

            X,

            y,

            test_size=0.2,

            random_state=42

        )

    )

    return (

        X_train,

        X_test,

        y_train,

        y_test

    )