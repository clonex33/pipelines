"""
This is a boilerplate pipeline 'blood_donation_trend'
generated using Kedro 0.19.1
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



def _is_true(x: pd.Series) -> pd.Series:
    return x == "t"


def _parse_percentage(x: pd.Series) -> pd.Series:
    x = x.str.replace("%", "")
    x = x.astype(float) / 100
    return x


def _parse_money(x: pd.Series) -> pd.Series:
    x = x.str.replace("$", "").str.replace(",", "")
    x = x.astype(float)
    return x


def raw_data_csv(daily_donation_raw: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data for daily_donation_raw.

    Args:
        daily_donation_raw: Raw data.
    Returns:
        Preprocessed data, with `company_rating` converted to a float and
        `iata_approved` converted to boolean.
    """
    hospital_region_mapping = {
        'Hospital Sultanah Nora Ismail': 'Southern Region',
        'Hospital Sultanah Aminah': 'Southern Region',
        'Hospital Sultanah Bahiyah': 'Northern Region',
        'Hospital Raja Perempuan Zainab II': 'Northern Region',
        'Hospital Melaka': 'Southern Region',
        'Hospital Tuanku Jaafar': 'Southern Region',
        'Hospital Tengku Ampuan Afzan': 'Central Region',
        'Hospital Sultan Haji Ahmad Shah': 'Central Region',
        'Hospital Seberang Jaya': 'Northern Region',
        'Hospital Pulau Pinang': 'Northern Region',
        'Hospital Raja Permaisuri Bainun': 'Northern Region',
        'Hospital Taiping': 'Northern Region',
        'Hospital Seri Manjung': 'Northern Region',
        'Hospital Tengku Ampuan Rahimah': 'Central Region',
        'Hospital Sultanah Nur Zahirah': 'East Coast Region',
        'Hospital Queen Elizabeth II': 'Borneo Region',
        'Hospital Duchess Of Kent': 'Borneo Region',
        'Hospital Tawau': 'Borneo Region',
        'Hospital Umum Sarawak': 'Borneo Region',
        'Hospital Miri': 'Borneo Region',
        'Hospital Sibu': 'Borneo Region',
        'Pusat Darah Negara': 'National Region',  # Adding Pusat Darah Negara to National Region
    }

    # Map hospitals to regions and create a new 'region' column
    daily_donation_raw['region'] = daily_donation_raw['hospital'].map(hospital_region_mapping)
    daily_donation_raw

    return daily_donation_raw


def visualisation(df_donations_facility: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data for shuttles.

    Args:
        shuttles: Raw data.
    Returns:
        Preprocessed data, with `price` converted to a float and `d_check_complete`,
        `moon_clearance_complete` converted to boolean.
    """
    # Assuming df_donations_facility is your Pandas DataFrame
    # Replace this with your actual DataFrame

    # Convert the 'date' column to datetime format for proper sorting
    df_donations_facility['date'] = pd.to_datetime(df_donations_facility['date'])

    # Group by 'date' and 'region' and sum the 'daily' column
    df_daily_sum = df_donations_facility.groupby(['date', 'region'])['daily'].sum().reset_index()

    # Extract quarter and year from the 'date' column
    df_daily_sum['quarter'] = df_daily_sum['date'].dt.to_period("A")

    # Convert 'quarter' to string
    df_daily_sum['quarter_str'] = df_daily_sum['quarter'].astype(str)

    # Group by 'quarter_str' and 'region' and sum the 'daily' column
    df_quarterly_sum = df_daily_sum.groupby(['quarter_str', 'region'])['daily'].sum().reset_index()

    # Line plot with quarterly values on the x-axis
    plt.figure(figsize=(12, 6))

    for region in df_quarterly_sum['region'].unique():
        region_data = df_quarterly_sum[df_quarterly_sum['region'] == region]

        # Exclude the last quarter
        region_data = region_data.iloc[:-1]

        plt.plot(region_data['quarter_str'], region_data['daily'], label=region)

        # Calculate trend line
        x_values = np.arange(len(region_data))
        y_values = region_data['daily']
        slope, intercept = np.polyfit(x_values, y_values, 1)
        trend_line = slope * x_values + intercept
        plt.plot(region_data['quarter_str'], trend_line, linestyle='--', color='black', alpha=0.5)

    # Label x-axis
    plt.xlabel('Yearly', color='black')  # Set the color of x-axis labels to black

    # Label y-axis
    plt.ylabel('Sum of Daily Blood Donations')

    # Display legend with a black border and white text
    legend = plt.legend()
    for text in legend.get_texts():
        text.set_color('black')

    # Add title
    plt.title('Total Yearly Blood Donation Trendline by Region', color='black')

    # Adjusting x-axis label rotation and font size
    plt.xticks(rotation=60, ha='right', fontsize=8)

    # Adjust spacing between x-axis labels and the plot
    plt.tight_layout()

    # Show the plot

    return plt
