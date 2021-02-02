"""
write_schedule.py

used to write a zoom scedule to schedule.json.


By: Calacuda | MIT Licence | epoch Feb 2, 2021
"""


import json
# from os import getcwd
# from os.path import join


FILE_NAME = "schedule.json"
# FILE_PATH = join(getcwd(), FILE_NAME)
AFERMATIVE = {"y", "yes"}
NEGATIVE = {"n", "no"}


def answer_binary(prompt):
    """
    only allows answers in the sets, AFERMATIVE and NEGATIVE.
    """
    answer = input(prompt).lower()
    while (answer not in AFERMATIVE) and (answer not in NEGATIVE):
        print(f"your anser must be answer must be any of '{AFERMATIVE}'"
              f" if yes, or '{NEGATIVE}' if no.")
        answer = input(prompt).lower()
    return answer


def get_meeting() -> tuple:
    """
    returns a dict containing the time and zoom link.
    """
    return {"time": input("what time is this meeting? [hh:mm] > "),
            "link": input("what is the zoom link? > ")}


def get_meetings(day) -> list:
    """
    returns a list of tuples of meeting times and the zoom link to the meeting
    """
    meetings = []
    more_meetings = "y"
    while more_meetings in AFERMATIVE:
        meetings.append(get_meeting())
        prompt = f"would you like to add another meeting for {day}?  [y/n] > "
        more_meetings = answer_binary(prompt)
        if more_meetings in NEGATIVE:
            break
    return meetings


def main():
    schedule = {"monday": [], "tuesday": [], "wednesday": [], "thursday": [],
                "friday": [], "saturday": [], "sunday": []}
    for day in schedule.keys():
        prompt = f"Do you have a zoom meeting on {day.capitalize()}?  [y/n] > "
        add_meeting = answer_binary(prompt)
        if add_meeting in AFERMATIVE:
            schedule[day] = get_meetings(day.capitalize())
        print()
    with open(FILE_NAME, 'w') as schedule_file:
        schedule_file.write(json.dumps(schedule))
    return 0


if __name__ == "__main__":
    main()
