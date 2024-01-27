"""
This is a boilerplate pipeline 'blood_donation_trend'
generated using Kedro 0.19.1
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression


def raw_data_csv(daily_donation_raw: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data for daily_donation_raw.

    Args:
        daily_donation_raw: Raw data.
    Returns:
        Preprocessed data, with `company_rating` converted to a float and
        `iata_approved` converted to boolean.
    """

    daily_donation_raw

    return daily_donation_raw



def visualisation_scatter_plot_1(daily_donation_ingested_processed: pd.DataFrame) -> pd.DataFrame:


    # Assuming daily_donation_ingested_processed is your DataFrame
    # Replace this with your actual DataFrame

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
    daily_donation_ingested_processed['region'] = daily_donation_ingested_processed['hospital'].map(
        hospital_region_mapping)

    # Filter only East Coast, Central, and Borneo regions
    selected_regions = ['East Coast Region', 'Central Region', 'Borneo Region']
    df_filtered = daily_donation_ingested_processed[
        daily_donation_ingested_processed['region'].isin(selected_regions)].copy()

    # Convert the 'date' column to datetime format for proper sorting
    df_filtered['date'] = pd.to_datetime(df_filtered['date']).copy()

    # Extract quarter and year from the 'date' column
    df_filtered['quarter'] = df_filtered['date'].dt.to_period("A").copy()

    # Convert 'quarter' to string
    df_filtered['quarter_str'] = df_filtered['quarter'].astype(str).copy()

    # Group by 'quarter_str' and 'region' and sum the 'daily' column
    df_quarterly_sum = df_filtered.groupby(['quarter_str', 'region'])['daily'].sum().reset_index()

    # Create subplots for each region with increased gap
    fig, axes = plt.subplots(len(selected_regions), 1, figsize=(12, 6 * len(selected_regions)), sharex=True,
                             gridspec_kw={'hspace': 0.1}, facecolor='w')  # Adjust hspace as needed

    # Use seaborn color palette for better color distinction
    region_palette = sns.color_palette("husl", n_colors=len(df_quarterly_sum['region'].unique()))

    for i, region in enumerate(selected_regions):
        region_data = df_quarterly_sum[df_quarterly_sum['region'] == region].copy()

        # Exclude the last data point
        region_data = region_data.iloc[:-1].copy()

        # Plot in the subplot with different color and dashed line
        axes[i].plot(region_data['quarter_str'], region_data['daily'], label=region, color=region_palette[i])

        # Fit a linear regression model to get the trendline
        x = np.arange(len(region_data))
        y = region_data['daily'].values
        model = LinearRegression().fit(x.reshape(-1, 1), y)
        trendline = model.predict(x.reshape(-1, 1))

        # Plot the trendline
        axes[i].plot(region_data['quarter_str'], trendline, linestyle='--', color='black')

        # Label y-axis for each subplot
        axes[i].set_ylabel(f'Sum of Daily Blood Donations')

        # Add title for each subplot and increase title size
        axes[i].set_title(f'Total Annual Blood Donation Trendline - {region}', fontsize=14)

        # Add grid lines
        axes[i].grid(True, linestyle='--', alpha=0.7)

    # Label x-axis for the last subplot
    axes[-1].set_xlabel('Annual-Time-Series', color='black')

    # Adjusting x-axis label rotation and font size
    plt.xticks(rotation=60, ha='right', fontsize=8)

    # Remove the legend
    for ax in axes:
        ax.legend().set_visible(False)

    # Save the plot with tight layout
    # Show the plot
    # Save the plot with tight layout
    plt.savefig('trends_1.png', facecolor='w', bbox_inches='tight')
    return plt


def visualisation_scatter_plot_2(daily_donation_ingested_processed: pd.DataFrame) -> pd.DataFrame:

    # Assuming daily_donation_ingested_processed is your DataFrame
    # Replace this with your actual DataFrame

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
    daily_donation_ingested_processed['region'] = daily_donation_ingested_processed['hospital'].map(
        hospital_region_mapping)

    # Filter only East Coast, Central, and Borneo regions
    selected_regions = ['National Region', 'Northern Region', 'Southern Region']
    df_filtered = daily_donation_ingested_processed[
        daily_donation_ingested_processed['region'].isin(selected_regions)].copy()

    # Convert the 'date' column to datetime format for proper sorting
    df_filtered['date'] = pd.to_datetime(df_filtered['date']).copy()

    # Extract quarter and year from the 'date' column
    df_filtered['quarter'] = df_filtered['date'].dt.to_period("A").copy()

    # Convert 'quarter' to string
    df_filtered['quarter_str'] = df_filtered['quarter'].astype(str).copy()

    # Group by 'quarter_str' and 'region' and sum the 'daily' column
    df_quarterly_sum = df_filtered.groupby(['quarter_str', 'region'])['daily'].sum().reset_index()

    # Create subplots for each region with increased gap
    fig, axes = plt.subplots(len(selected_regions), 1, figsize=(12, 6 * len(selected_regions)), sharex=True,
                             gridspec_kw={'hspace': 0.1}, facecolor='w')  # Adjust hspace as needed

    # Use seaborn color palette for better color distinction
    region_palette = sns.color_palette("husl", n_colors=len(df_quarterly_sum['region'].unique()))

    for i, region in enumerate(selected_regions):
        region_data = df_quarterly_sum[df_quarterly_sum['region'] == region].copy()

        # Exclude the last data point
        region_data = region_data.iloc[:-1].copy()

        # Plot in the subplot with different color and dashed line
        axes[i].plot(region_data['quarter_str'], region_data['daily'], label=region, color=region_palette[i])

        # Fit a linear regression model to get the trendline
        x = np.arange(len(region_data))
        y = region_data['daily'].values
        model = LinearRegression().fit(x.reshape(-1, 1), y)
        trendline = model.predict(x.reshape(-1, 1))

        # Plot the trendline
        axes[i].plot(region_data['quarter_str'], trendline, linestyle='--', color='black')

        # Label y-axis for each subplot
        axes[i].set_ylabel(f'Sum of Daily Blood Donations')

        # Add title for each subplot and increase title size
        axes[i].set_title(f'Total Annual Blood Donation Trendline - {region}', fontsize=14)

        # Add grid lines
        axes[i].grid(True, linestyle='--', alpha=0.7)

    # Label x-axis for the last subplot
    axes[-1].set_xlabel('Annual-Time-Series', color='black')

    # Adjusting x-axis label rotation and font size
    plt.xticks(rotation=60, ha='right', fontsize=8)

    # Remove the legend
    for ax in axes:
        ax.legend().set_visible(False)

    # Save the plot with tight layout
    plt.savefig('trends_2.png', facecolor='w', bbox_inches='tight')
    plt.tight_layout()
    # Show the plot
    return plt

