"""
This is a boilerplate pipeline 'donator_retention'
generated using Kedro 0.19.1
"""

from kedro.pipeline import Pipeline, pipeline


from kedro.pipeline import Pipeline, node, pipeline

from .nodes import raw_data_parquet,Days_Between_Consecutive_Visits_plot,Average_Number_of_Return_Visits




def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=raw_data_parquet,
                inputs="blood_donators_retention_parquet",
                outputs="data_proccesed",
                name="data_parquet_ingestion",
            ),
            node(
                func=Days_Between_Consecutive_Visits_plot,
                inputs="data_proccesed",
                outputs="consecutive_Visits_plot",
                name="days_between_visit",
            ),
            node(
                func=Average_Number_of_Return_Visits,
                inputs="data_proccesed",
                outputs="number_of_return_visits",
                name="number_of_return",
            )
        ]
    )
