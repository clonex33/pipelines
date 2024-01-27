import pandas as pd
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






def donator_retention_plot(data_processed: pd.DataFrame) -> None:


    data_processed['generation'] = pd.cut(data_processed['birth_date'],
    bins=[1900, 1964, 1980, 1996, 2100],labels=['Silent', 'Boomer', 'Gen X', 'Millennial'], right=False)

    generation_counts = data_processed.groupby('generation').size().reset_index(name='count')

    legend_labels = {
        'Silent': '1900-1964',
        'Boomer': '1965-1980',
        'Gen X': '1981-1996',
        'Millennial': '1997&above'
    }

    # Create a bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(generation_counts['generation'], generation_counts['count'],
                  color=['skyblue', 'lightcoral', 'lightgreen', 'lightsalmon'], linewidth=0.7)

    # Add labels and title
    plt.title('Generational Impact: Blood Donation Trends in Malaysia')
    plt.xlabel('Generation')
    plt.ylabel('Total Donations')

    # Set background color for the entire plot
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    # Format y-axis ticks without scientific notation
    ax.ticklabel_format(style='plain', axis='y')

    # Annotate bars with count values
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), ha='center', va='bottom')

    # Add background grid
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Create legends for each age range
    legends = [plt.Line2D([0], [0], marker='o', color='w', label=f'{label}: {legend_labels[label]}',
                          markerfacecolor=color, markersize=10) for label, color in
               zip(generation_counts['generation'], ['skyblue', 'lightcoral', 'lightgreen', 'lightsalmon'])]

    # Add legend
    plt.legend(handles=legends, title='Age Range', loc='upper left')

    # Save the plot
    plt.tight_layout()
    plt.savefig('generation.png')

    return plt





