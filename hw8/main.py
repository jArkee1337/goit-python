from datetime import datetime, timedelta

delta = timedelta(weeks=1)
today = datetime.now()

users_list = [{"name": "Vladimir", "birthday": datetime(year=1997, month=3, day=11)},
              {"name": "Igor", "birthday": datetime(year=1997, month=2, day=4)},
              {"name": "Ivan", "birthday": datetime(year=1997, month=2, day=5)},
              {"name": "Andrey", "birthday": datetime(year=1997, month=2, day=6)},
              {"name": "Timofey", "birthday": datetime(year=1997, month=2, day=7)},
              {"name": "Rustam", "birthday": datetime(year=1997, month=2, day=8)},
              {"name": "Amir", "birthday": datetime(year=1997, month=2, day=9)},
              {"name": "Henry", "birthday": datetime(year=1997, month=2, day=10)},
              {"name": "Yaroslav", "birthday": datetime(year=1997, month=2, day=11)}]


def get_birthdays_per_week(users):
    this_year_list = []
    for dictionaries in users_list:
        dictionary = {}

        for key, value in dictionaries.items():

            if key == "name":
                dictionary.update({"name": value})
            elif key == "birthday":
                dictionary.update({"birthday": datetime(year=today.year, month=dictionaries["birthday"].month,
                                                        day=dictionaries["birthday"].day)})
        this_year_list.append(dictionary)

    birthday_people_list = []
    for i in range(0, len(this_year_list)):
        condition = (this_year_list[i]["birthday"] - (today + delta)).days

        if -8 <= condition <= -1:
            birthday_people_list.append(this_year_list[i])
        else:
            continue
    if not birthday_people_list:
        print("There is now birthday on this week")

    days_of_week = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
    for i in range(0, len(birthday_people_list)):
        if birthday_people_list[i]["birthday"].weekday() == 0 or birthday_people_list[i]["birthday"].weekday() == 5 or \
                birthday_people_list[i]["birthday"].weekday() == 6:
            days_of_week["Monday"].append(birthday_people_list[i]["name"])
        elif birthday_people_list[i]["birthday"].weekday() == 1:
            days_of_week["Tuesday"].append(birthday_people_list[i]["name"])
        elif birthday_people_list[i]["birthday"].weekday() == 2:
            days_of_week["Wednesday"].append(birthday_people_list[i]["name"])
        elif birthday_people_list[i]["birthday"].weekday() == 3:
            days_of_week["Thursday"].append(birthday_people_list[i]["name"])
        elif birthday_people_list[i]["birthday"].weekday() == 4:
            days_of_week["Friday"].append(birthday_people_list[i]["name"])

    for key, value in days_of_week.items():
        if value:
            print(f"{key}: {','.join(value)}")


get_birthdays_per_week(users_list)
