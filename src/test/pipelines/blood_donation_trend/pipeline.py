"""
This is a boilerplate pipeline 'blood_donation_trend'
generated using Kedro 0.19.1
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import raw_data_csv, visualisation_scatter_plot_1,visualisation_scatter_plot_2

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
                func=visualisation_scatter_plot_1,
                inputs="daily_donation_processed",
                outputs=None,
                name="trend_scatter_plot_1",
            ),
            node(
                func=visualisation_scatter_plot_2,
                inputs="daily_donation_processed",
                outputs=None,
                name="trend_scatter_plot_2",
            )
        ]
    )