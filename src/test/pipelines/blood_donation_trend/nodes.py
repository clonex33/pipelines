"""
This is a boilerplate pipeline 'blood_donation_trend'
generated using Kedro 0.19.1
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


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
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    from sklearn.linear_model import LinearRegression

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
    df_filtered = daily_donation_ingested_processed[daily_donation_ingested_processed['region'].isin(selected_regions)]

    # Convert the 'date' column to datetime format for proper sorting
    df_filtered['date'] = pd.to_datetime(df_filtered['date'])

    # Extract quarter and year from the 'date' column
    df_filtered['quarter'] = df_filtered['date'].dt.to_period("A")

    # Convert 'quarter' to string
    df_filtered['quarter_str'] = df_filtered['quarter'].astype(str)

    # Group by 'quarter_str' and 'region' and sum the 'daily' column
    df_quarterly_sum = df_filtered.groupby(['quarter_str', 'region'])['daily'].sum().reset_index()

    # Create subplots for each region with increased gap
    fig, axes = plt.subplots(len(selected_regions), 1, figsize=(12, 6 * len(selected_regions)), sharex=True,
                             gridspec_kw={'hspace':0.15})  # Adjust hspace as needed

    # Use seaborn color palette for better color distinction
    region_palette = sns.color_palette("husl", n_colors=len(df_quarterly_sum['region'].unique()))

    for i, region in enumerate(selected_regions):
        region_data = df_quarterly_sum[df_quarterly_sum['region'] == region]

        # Exclude the last data point
        region_data = region_data.iloc[:-1]

        # Plot in the subplot
        axes[i].plot(region_data['quarter_str'], region_data['daily'], label=region)

        # Fit a linear regression model to get the trendline
        x = np.arange(len(region_data))
        y = region_data['daily'].values
        model = LinearRegression().fit(x.reshape(-1, 1), y)
        trendline = model.predict(x.reshape(-1, 1))

        # Plot the trendline
        axes[i].plot(region_data['quarter_str'], trendline, linestyle='--', color='black', label='Trendline')

        # Label y-axis for each subplot
        axes[i].set_ylabel(f'Sum of Daily Blood Donations')

        # Add title for each subplot and reduce title size
        axes[i].set_title(f'Total Annualy Blood Donation Trendline - {region}', fontsize=10)

    # Label x-axis for the last subplot
    axes[-1].set_xlabel('Quarter', color='black')

    # Adjusting x-axis label rotation and font size
    plt.xticks(rotation=60, ha='right', fontsize=8)

    # Show the legend
    for ax in axes:
        ax.legend()

    # Adjust spacing between x-axis labels and the plot
    plt.tight_layout()

    # Show the plot
    return plt


def visualisation_scatter_plot_2(daily_donation_ingested_processed: pd.DataFrame) -> pd.DataFrame:
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    from sklearn.linear_model import LinearRegression

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
    df_filtered = daily_donation_ingested_processed[daily_donation_ingested_processed['region'].isin(selected_regions)]

    # Convert the 'date' column to datetime format for proper sorting
    df_filtered['date'] = pd.to_datetime(df_filtered['date'])

    # Extract quarter and year from the 'date' column
    df_filtered['quarter'] = df_filtered['date'].dt.to_period("A")

    # Convert 'quarter' to string
    df_filtered['quarter_str'] = df_filtered['quarter'].astype(str)

    # Group by 'quarter_str' and 'region' and sum the 'daily' column
    df_quarterly_sum = df_filtered.groupby(['quarter_str', 'region'])['daily'].sum().reset_index()

    # Create subplots for each region with increased gap
    fig, axes = plt.subplots(len(selected_regions), 1, figsize=(12, 6 * len(selected_regions)), sharex=True,
                             gridspec_kw={'hspace':0.15})  # Adjust hspace as needed

    # Use seaborn color palette for better color distinction
    region_palette = sns.color_palette("husl", n_colors=len(df_quarterly_sum['region'].unique()))

    for i, region in enumerate(selected_regions):
        region_data = df_quarterly_sum[df_quarterly_sum['region'] == region]

        # Exclude the last data point
        region_data = region_data.iloc[:-1]

        # Plot in the subplot
        axes[i].plot(region_data['quarter_str'], region_data['daily'], label=region)

        # Fit a linear regression model to get the trendline
        x = np.arange(len(region_data))
        y = region_data['daily'].values
        model = LinearRegression().fit(x.reshape(-1, 1), y)
        trendline = model.predict(x.reshape(-1, 1))

        # Plot the trendline
        axes[i].plot(region_data['quarter_str'], trendline, linestyle='--', color='black', label='Trendline')

        # Label y-axis for each subplot
        axes[i].set_ylabel(f'Sum of Daily Blood Donations')

        # Add title for each subplot and reduce title size
        axes[i].set_title(f'Total Annualy Blood Donation Trendline - {region}', fontsize=10)

    # Label x-axis for the last subplot
    axes[-1].set_xlabel('Quarter', color='black')

    # Adjusting x-axis label rotation and font size
    plt.xticks(rotation=60, ha='right', fontsize=8)

    # Show the legend
    for ax in axes:
        ax.legend()

    # Adjust spacing between x-axis labels and the plot
    plt.tight_layout()

    # Show the plot
    return plt
# def visualisation_bar_plot(daily_donation_ingested_processed: pd.DataFrame) -> pd.DataFrame:
#     # Assuming df_donations_facility is your Pandas DataFrame
#     # Replace this with your actual DataFrame
#
#     # Convert the 'date' column to datetime format for proper sorting
#     daily_donation_ingested_processed['date'] = pd.to_datetime(daily_donation_ingested_processed['date'])
#
#     # Extract year from the 'date' column
#     daily_donation_ingested_processed['year'] = daily_donation_ingested_processed['date'].dt.year
#
#     # Convert 'year' to string
#     daily_donation_ingested_processed['year_str'] = daily_donation_ingested_processed['year'].astype(str)
#
#     # Group by 'year_str' and sum the 'daily' column
#     df_yearly_sum = daily_donation_ingested_processed.groupby('year_str')['daily'].sum().reset_index()
#
#     # Define a pastel red color manually
#     pastel_red = "#FF9999"
#
#     # Bar plot with yearly values on the x-axis
#     plt.figure(figsize=(12, 6))
#
#     # Plot bar for total yearly donations with pastel red color
#     plt.bar(df_yearly_sum['year_str'], df_yearly_sum['daily'], label='Total blood donors Yearly', color=pastel_red,
#             alpha=0.7)
#
#     # Calculate trend line for total yearly donations
#     x_values_total = np.arange(len(df_yearly_sum['year_str']))
#     slope_total, intercept_total = np.polyfit(x_values_total, df_yearly_sum['daily'], 1)
#     trend_line_total = slope_total * x_values_total + intercept_total
#     plt.plot(df_yearly_sum['year_str'], trend_line_total, linestyle='--', color='black', alpha=0.5)
#
#     # Label x-axis
#     plt.xlabel('Year', color='black')  # Set the color of x-axis labels to black
#
#     # Label y-axis
#     plt.ylabel('Total Yearly Blood Donations')
#
#     # Add title to the plot
#     plt.title('Total Yearly Blood Donations Over Time', color='black')
#
#     # Display legend with a black border and white text
#     legend = plt.legend()
#     for text in legend.get_texts():
#         text.set_color('black')
#
#     # Adjusting x-axis label rotation and font size
#     plt.xticks(rotation=60, ha='right', fontsize=8)
#
#     # Adjust spacing between x-axis labels and the plot
#     plt.tight_layout()
#
#     # Show the plot
#     return plt