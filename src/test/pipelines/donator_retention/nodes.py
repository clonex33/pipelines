import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
"""
This is a boilerplate pipeline 'donator_retention'
generated using Kedro 0.19.1
"""
def raw_data_parquet(daily_donation_raw: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data for daily_donation_raw.

    Args:
        daily_donation_raw: Raw data.
    Returns:
        Preprocessed data, with `company_rating` converted to a float and
        `iata_approved` converted to boolean.
    """


    return daily_donation_raw


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import zscore

def donator_retention_plot(data_processed: pd.DataFrame) -> None:
    """Preprocesses the data, removes outliers, and creates subplots.

    Args:
        data_processed: Raw data.
    """

    # Convert 'visit_date' column to datetime
    data_processed['visit_date'] = pd.to_datetime(data_processed['visit_date'])

    # Calculate the time difference between consecutive visits for each donor
    data_processed['time_diff'] = data_processed.groupby('donor_id')['visit_date'].diff()

    # Calculate the mean time difference for each donor in days
    mean_time_diff = data_processed.groupby('donor_id')['time_diff'].mean()

    # Drop NaN values before calculating the overall mean time difference
    overall_mean_time_diff = mean_time_diff.dropna().mean()

    # Remove outliers using z-score
    z_scores = zscore(mean_time_diff.dropna().dt.days)  # Convert datetime to numeric values (days)
    non_outliers_mask = (np.abs(z_scores) < 3)  # Adjust the threshold as needed
    mean_time_diff_no_outliers = mean_time_diff.dropna()[non_outliers_mask]

    # Determine how well donors are retained based on the overall mean time difference
    desired_threshold = 60  # Set your desired threshold (in days)
    if overall_mean_time_diff <= pd.Timedelta(days=desired_threshold):
        retention_status = "Blood donors are being retained well."
    else:
        retention_status = "Blood donors need better retention."

    # Create subplots
    fig, axs = plt.subplots(1, 2, figsize=(15, 6))

    # Subplot 1: Distribution of Mean Time Differences without outliers
    axs[0].hist(mean_time_diff_no_outliers.dt.days, bins=20, edgecolor='black')
    axs[0].axvline(x=overall_mean_time_diff.days, color='red', linestyle='--', label='Average')
    axs[0].text(overall_mean_time_diff.days + 2, 0.5, f'   Average: {round(overall_mean_time_diff.days)} days',
                color='red', rotation='vertical')
    axs[0].set_title(f'Distribution of Mean Time Differences')
    axs[0].set_xlabel('Days Between Consecutive Visits')
    axs[0].set_ylabel('Frequency')

    # Add legend
    axs[0].legend()

    # Subplot 2: Distribution of Return Visits
    return_visits = data_processed.groupby('donor_id').size()
    axs[1].hist(return_visits, bins=np.arange(0, 51, 1), edgecolor='black')
    axs[1].set_title('Distribution of Return Visits')
    axs[1].set_xlabel('Number of Return Visits')
    axs[1].set_ylabel('Frequency')
    axs[1].set_xticks(np.arange(0, 35, 5))

    # Add annotations for average return visits and retention status
    axs[1].annotate(f'Average Return Visits: {return_visits.mean():.2f} times', xy=(0.5, 0.9),
                    xycoords='axes fraction', ha='center', fontsize=12, color='red')

    axs[1].annotate(retention_status, xy=(0.5, 0.85), xycoords='axes fraction', ha='center', fontsize=12,
                    color='red')

    # Adjust layout
    plt.tight_layout()

    # Add overall title
    plt.suptitle('Combined Plot: Mean Time Differences and Return Visits (No Outliers)', fontsize=16, y=1.05)

    # Show the plot
    return plt


# Example usage with a sample DataFrame
# donator_retention_plot(your_data_processed_dataframe)



