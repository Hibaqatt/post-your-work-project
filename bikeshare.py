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
    # Get user input for city, month, and day filters
    print('Hello! Let\'s explore some US bikeshare data!')

    # valid options
    city_list = ['chicago', 'new york city', 'washington']
    month_list = ['all','january', 'february', 'march', 'april', 'may', 'june']
    day_list = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
   


    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs 
    while True:
        city = input("Enter city (Chicago, New York City, Washington): ").lower()
        if city in cities:
            break
        else:
            print("Invalid city, try again.") 
   



    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter month (all, January to June): ").lower()
        if month in months:
            break
        else:
            print("Invalid month, try again.")




    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter day (all, Monday to Sunday): ").lower()
        if day in days:
            break
        else:
            print("Invalid day, try again.")


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
    # Load and filter bikeshare dataset based on user input
    df = pd.read_csv(CITY_DATA[city])

    # ---------------- CONVERT TO DATETIME ----------------
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # ---------------- CREATE NEW COLUMNS ----------------
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # ---------------- FILTER BY MONTH ----------------
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_index = months.index(month) + 1
        df = df[df['month'] == month_index]

    # ---------------- FILTER BY DAY ----------------
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # make sure columns exist
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # display the most common month
    popular_month = df['month'].mode()[0]
    print("Most common month:", popular_month)


    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("Most common day:", popular_day)


    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("Most common start hour:", popular_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Most Common Start Station:", df['Start Station'].mode()[0])


    # display most commonly used end station
    print("Most Common End Station:", df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + " -> " + df['End Station']
    print("Most Frequent Trip:", df['Trip'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total Travel Time:", df['Trip Duration'].sum())


    # display mean travel time
    print("Average Travel Time:", df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("User Types:\n", df['User Type'].value_counts())


    # Display counts of gender
    if 'Gender' in df.columns:
        print("\nGender Counts:\n", df['Gender'].value_counts())
    else:
        print("\nNo Gender data available.")


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("\nEarliest Birth Year:", int(df['Birth Year'].min()))
        print("Most Recent Birth Year:", int(df['Birth Year'].max()))
        print("Most Common Birth Year:", int(df['Birth Year'].mode()[0]))
    else:
        print("\nNo Birth Year data available.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if df.empty:
            print("\nNo data found for the selected filters. Please try again.\n")
            continue

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        show_data = input('\nWould you like to see raw data? Enter yes or no:\n').lower()
        if show_data in ['yes', 'no']:
             break
        else:
            print("Invalid input. Please enter yes or no.")


        start = 0

        while show_data == 'yes':
            print(df.iloc[start:start+5])
            start += 5

            if start >= len(df):
                print("\nNo more data to display.")
                break

            
        while True:
             show_data = input('\nDo you want to see more data? Enter yes or no:\n').lower()
        if show_data in ['yes', 'no']:
             break
        else:
            print("Invalid input. Please enter yes or no.")

        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
