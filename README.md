# Video Game Sales Analysis Project ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
This project analyses video game sales data to uncover insights about sales trends across different genres, platforms, and regions. It uses data visualisation techniques to explore patterns and distributions in the video game market.

## Features
- **Data Cleaning**: Identifies and removes rows with missing values to ensure accurate analysis.
- **Data Exploration**: Groups data by year, platform, and publisher to calculate average sales.
- **Visualisations**:
    - Count plots to show the frequency of video game genres and platform popularity.
    - Analysis of sales across different regions (NA, EU, JP, Global, and others).
## Getting Started
### Prerequisites
- Python 3.x
- Required libraries: pandas, matplotlib, numpy, seaborn

Install the required libraries using the following command:

pip install pandas matplotlib numpy seaborn

### Installation

1. Clone the repository or download the script:

    git clone https://github.com/whearne/videogame-sales-analysis-python.git

2. Navigate to the project directory:

    cd videogame-sales-analysis-python

3. Place the vgsales.csv dataset in the same directory as the script.

### Usage
1. Open the script (Videogame Analysis.py) in a code editor.

2. Update the file path to the dataset if it is located in a different directory:

    df = pd.read_csv('path/to/vgsales.csv')

3. Run the script:

    python Videogame\ Analysis.py

4. The script will generate:

- Information about the dataset, including column data types and missing values.
- Grouped sales data by year, platform, and publisher.
- Visualisations of genre frequency and platform popularity.
### Visualisations
- **Genre Frequency**: Shows the popularity of different video game genres using a count plot.
- **Platform Popularity**: Visualises the most popular gaming platforms using a horizontal count plot.
- **Regional Sales Analysis**: Provides insights into sales distribution across different regions (Europe, Japan, North America, etc.).

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgements
- The project uses the pandas library for data manipulation and matplotlib and seaborn for data visualisation.
- Data sourced from the vgsales.csv file, which contains sales data for various video games.
