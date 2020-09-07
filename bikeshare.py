import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Choose a city you would like the data from(chicago, new york city, washington)): ")
        city = city.lower()

        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Incorrect input. Please try again.")

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Choose which month you would like the data from or type 'all'.): ")
        month = month.lower()

        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print("Incorrect input. Please try again.")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Choose which day you would like the data from or type 'all'.): ")
        day = day.lower()

        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print("Incorrect input. Please try again.")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    #Load data frame columns needed
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name
    df['hour'] = df['Start Time'].dt.hour

    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("Most common month: {} \n".format(df['month'].mode()[0]))

    # display the most common day of week
    print("Most common day: {} \n".format(df['day_of_week'].mode()[0]))

    # display the most common start hour
    print("Most common start hour: {} \n".format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Most common start station: {} \n".format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print("Most common end station: {} \n".format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    df['combination_station'] = df['Start Station'] + " to " + df['End Station']
    print("Most frequent combination of start station and end station trip: {} \n".format(df['combination_station'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time: {} \n".format(df['Trip Duration'].sum()))

    # display mean travel time
    print("Travel time mean: {} \n".format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    city = city

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # display counts of user types
    print("Count of user types: \n {} \n".format(df['User Type'].value_counts()))
    
    if city != 'washington':
        # display counts of gender
        print("Count of gender: \n {} \n".format(df['Gender'].value_counts()))

        # display earliest, most recent, and most common year of birth
        print("Earliest year of birth: {} \n".format(df['Birth Year'].min()))
        print("Most recent year of birth: {} \n".format(df['Birth Year'].max()))
        print("Most common year of birth: {} \n".format(df['Birth Year'].mode()[0]))

    else:
        print("No gender or year of birth stats for Washington. Sorry. \n")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        x = 0

        while True:
            five_rows = input('Break up raw data into 5 rows? yes or no? \n')
            
            if five_rows.lower() == 'yes':
                print(df.head(x))
                x = x+5
            else:
                break

        restart = input('\n Would you like to restart? Enter yes or no. \n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
