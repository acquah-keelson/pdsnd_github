import time

import numpy as np
import pandas as pd

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
MONTHS_WITH_ALL = [
    'january', 'february', 'march', 'april', 'may', 'june', 'all'
]

DAYS_WITH_ALL = [
    'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
    'sunday', 'all'
]

CITIES = [k for k in CITY_DATA]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.


    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by,
        or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply
        no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    # TO DO: get user input for month (all, january, february, ... , june)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    start_time = time.time()
    while True:
        city = input('\nWould you like to see data for chicago, new york city,\
 washington).\n').lower()

        if city not in CITIES:
            print("The only cities available now are 'chicago', \
'new york city', 'washington'")
            continue

        month = input(
            '\n Which month in the first 6 months of the year are you\
interested in ? (january, february, ... june or all)').lower()

        if month not in MONTHS_WITH_ALL:
            print("Month can only be one of the following ...")
            continue

        day = input(
            '\n Which day of the week are you interested in? (monday, tuesday, wednesday,thursday, ... sunday)'
        ).lower()

        day = day.lower()
        if day not in DAYS_WITH_ALL:
            print("Month can only be one of the following ...")
            continue
        break

    print('\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month
    and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no
        month filter
        (str) day - name of the day of week to filter by, or "all" to apply
        no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = MONTHS
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("\n Most popular month", df['month'].mode()[0])
    # TO DO: display the most common day of week

    print("\n Most popular day of the week", df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour

    print("\n Most popular hour", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("\n Most used start station ", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("\n Most used End station ", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station
    # and end station trip

    df['End And Start Station'] = df['Start Station'] + ',' + df['End Station']
    print("\n Most frequent combination of start station and end station",
          df['End And Start Station'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df["duration"] = df['End Time'] - df['Start Time']
    df['duration'] = df['duration'] / np.timedelta64(1, 'h')
    # TO DO: display mean travel time

    print("\n Total travel time in hours", df["duration"].sum())

    print("\n Average travel time in hours", df["duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Displaying user counts")
    print(df["User Type"].value_counts())

    # TO DO: Display counts of gender
    try:
        print('\n* Gender Counts?\n')

        print(df['Gender'].value_counts())
    except:
        print('No data available for gender')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('\n* Earliest, most recent and most common year of birth')
        earliest = np.min(df['Birth Year'])
        print("\n earliest year of birth is " + str(earliest) + "\n")
        latest = np.max(df['Birth Year'])
        print("latest year of birth is " + str(latest) + "\n")
        most_frequent = df['Birth Year'].mode()[0]
        print("Most frequent year of birth is " + str(most_frequent) + "\n")
    except:
        print('No data available for birth date')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_raw_data(df):
    """
    Display the raw data used to compute the stats

    Input:
        the dataframe

    Returns:
        None
  """
    row_index = 0
    yes_or_no = input(
        "\n Would you like to see the raw data? Type 'yes' or 'no' \n").lower(
    )

    while True:
        if yes_or_no == 'yes':
            print(df[row_index:row_index + 5])
            row_index = row_index + 5
        else:
            break

        yes_or_no = input("\nWould like to see 5 more rows ?\n").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_raw_data(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
