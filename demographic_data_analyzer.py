import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read the adult census dataset.
    df = pd.read_csv("adult.data.csv")

    # How many people of each race are represented?
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = round(df.loc[df["sex"] == "Male", "age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(
        (df["education"] == "Bachelors").mean() * 100, 1
    )

    # Advanced education includes Bachelor's, Master's, and Doctorate degrees.
    higher_education = df["education"].isin(
        ["Bachelors", "Masters", "Doctorate"]
    )
    lower_education = ~higher_education

    # Percentage of people with and without advanced education earning >50K.
    higher_education_rich = round(
        (df.loc[higher_education, "salary"] == ">50K").mean() * 100, 1
    )
    lower_education_rich = round(
        (df.loc[lower_education, "salary"] == ">50K").mean() * 100, 1
    )

    # Minimum number of hours worked per week.
    min_work_hours = df["hours-per-week"].min()

    # Percentage of minimum-hour workers earning >50K.
    min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = round(
        (min_workers["salary"] == ">50K").mean() * 100, 1
    )

    # Country with the highest percentage of people earning >50K.
    country_total = df["native-country"].value_counts()
    country_rich = (
        df[df["salary"] == ">50K"]["native-country"].value_counts()
    )
    country_percentage = (country_rich / country_total) * 100
    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = round(
        country_percentage.max(), 1
    )

    # Most popular occupation among people earning >50K in India.
    india_rich = df[
        (df["native-country"] == "India") & (df["salary"] == ">50K")
    ]
    top_IN_occupation = india_rich["occupation"].value_counts().idxmax()

    if print_data:
        print("Number of each race:")
        print(race_count)
        print("Average age of men:", average_age_men)
        print(
            "Percentage with Bachelor's degrees:",
            percentage_bachelors,
        )
        print(
            "Percentage with higher education that earn >50K:",
            higher_education_rich,
        )
        print(
            "Percentage without higher education that earn >50K:",
            lower_education_rich,
        )
        print("Minimum work hours:", min_work_hours)
        print(
            "Percentage of rich among those who work the fewest hours:",
            rich_percentage,
        )
        print(
            "Country with highest percentage of rich:",
            highest_earning_country,
        )
        print(
            "Highest percentage of rich people in country:",
            highest_earning_country_percentage,
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }


if __name__ == "__main__":
    calculate_demographic_data()
