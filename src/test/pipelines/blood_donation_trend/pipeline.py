"""
This is a boilerplate pipeline 'blood_donation_trend'
generated using Kedro 0.19.1
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import raw_data_csv, visualisation_scatter_plot,visualisation_bar_plot

...


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=raw_data_csv,
                inputs="daily_donation_csv_raw",
                outputs="daily_donation_processed",
                name="raw_data_scatter_ingestion",
            ),
            node(
                func=visualisation_scatter_plot,
                inputs="daily_donation_processed",
                outputs="trend_scatter_plot",
                name="trend_scatter_plot",
            ),
            node(
                func=visualisation_bar_plot,
                inputs="daily_donation_processed",
                outputs="trend_bar_plot",
                name="trend_bar_plot",
            )
        ]
    )