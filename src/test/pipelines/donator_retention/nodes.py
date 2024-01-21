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

def Average_Number_of_Return_Visits(data_proccesed: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data for daily_donation_raw.

    Args:
        daily_donation_raw: Raw data.
    Returns:
        Preprocessed data, with `company_rating` converted to a float and
        `iata_approved` converted to boolean.
    """

    data_proccesed
    # Assuming you have a DataFrame named data_proccesed with the provided data
    # If not, you can create it using the data you provided

    # Convert 'visit_date' column to datetime
    data_proccesed['visit_date'] = pd.to_datetime(data_proccesed['visit_date'])

    # Calculate the time difference between consecutive visits for each donor
    data_proccesed['time_diff'] = data_proccesed.groupby('donor_id')['visit_date'].diff()

    # Calculate the mean time difference for each donor in days
    mean_time_diff = data_proccesed.groupby('donor_id')['time_diff'].mean()

    # Drop NaN values before calculating the overall mean time difference
    overall_mean_time_diff = mean_time_diff.dropna().mean()
    data_proccesed
    # Display the overall mean time difference
    print(f"Overall Mean Time Difference: {overall_mean_time_diff.days} days")

    # Determine how well donors are retained based on the overall mean time difference
    desired_threshold = 60  # Set your desired threshold (in days)
    if overall_mean_time_diff <= pd.Timedelta(days=desired_threshold):
        retention_status = "Blood donors are being retained well."
    else:
        retention_status = "Blood donors need better retention."

    # Create a plot for overall mean time difference
    plt.figure(figsize=(10, 5))
    mean_time_diff_in_days = mean_time_diff.dropna().dt.days
    mean_time_diff_in_days.plot(kind='hist', bins=20, edgecolor='black', title='Distribution of Mean Time Differences')
    plt.xlabel('Days Between Consecutive Visits')
    plt.ylabel('Frequency')

    # Annotate the plot with the retention status
    plt.annotate(retention_status, xy=(0.5, 0.95), xycoords='axes fraction', ha='center', fontsize=12, color='red')

    return  plt

def Days_Between_Consecutive_Visits_plot(data_proccesed: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data for daily_donation_raw.

    Args:
        daily_donation_raw: Raw data.
    Returns:
        Preprocessed data, with `company_rating` converted to a float and
        `iata_approved` converted to boolean.
    """


    # Assuming you have a DataFrame named data_proccesed with the provided data
    # If not, you can create it using the data you provided

    # Create a plot for the number of return visits
    return_visits = data_proccesed.groupby('donor_id').size()
    plt.figure(figsize=(12, 6))

    # Increase the number of bins for more detailed data
    plt.hist(return_visits, bins=np.arange(0, 51, 1), edgecolor='black')

    plt.title('Distribution of Return Visits')
    plt.xlabel('Number of Return Visits')
    plt.ylabel('Frequency')

    # Set x-axis ticks up to 50 with intervals of 5
    plt.xticks(np.arange(0, 51, 5))

    # Calculate and annotate the average number of return visits
    average_return_visits = return_visits.mean()
    plt.annotate(f'Average Return Visits: {average_return_visits:.2f} times', xy=(0.5, 0.95), xycoords='axes fraction',
                 ha='center', fontsize=12, color='red')



    # Print the average number of return visits
    print(f"Average Number of Return Visits: {average_return_visits:.2f}")

    return  plt