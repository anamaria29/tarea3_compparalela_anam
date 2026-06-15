import time

import pandas as pd

from sklearn.linear_model import LinearRegression

from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor
)

from sklearn.metrics import (
    mean_absolute_error,
    root_mean_squared_error
)


def train_models(

    X_train,
    X_test,
    y_train,
    y_test

):

    models = {

        "Linear Regression":

            LinearRegression(),

        "Random Forest":

            RandomForestRegressor(

                n_estimators=50,
                random_state=42,
                n_jobs=-1

            ),

        "Gradient Boosting":

            GradientBoostingRegressor(

                random_state=42

            )

    }

    results = []

    for name, model in models.items():

        start = time.time()

        model.fit(

            X_train,

            y_train

        )

        train_time = (

            time.time()

            -

            start

        )

        preds = model.predict(

            X_test

        )

        rmse = (

            root_mean_squared_error(

                y_test,

                preds

            )

        )

        mae = (

            mean_absolute_error(

                y_test,

                preds

            )

        )

        results.append([

            name,

            train_time,

            rmse,

            mae

        ])

    return pd.DataFrame(

        results,

        columns=[

            "Model",

            "Training Time",

            "RMSE",

            "MAE"

        ]

    )