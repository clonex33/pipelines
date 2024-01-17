"""
This is a boilerplate pipeline 'blood_donation_trend'
generated using Kedro 0.19.1
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import raw_data_csv, visualisation

...


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=raw_data_csv,
                inputs="daily_donation_raw",
                outputs="daily_donation_processed",
                name="raw_data_ingestion",
            ),
            node(
                func=visualisation,
                inputs="daily_donation_processed",
                outputs="yearly_donation_plot",
                name="trend_plot",
            )
        ]
    )