# Quickly add an entry to a Daily Note in Obsidian
# Altered from https://github.com/parallelinnovation/Quick-note-entry-for-Obsidian/blob/main/obsidianQuickNoteEntry.py
import datetime
import time

DailyNotesFolder = ""      # Change this to the location of your daily notes folder. (E.g. C:/Users/John/Obsidian/Daily Notes)


def currentDailyNote():
    today = str(datetime.date.today())
    DailyNoteName = (today + ".md")
    monthTitles = {           # used for FOLDER_NAME_CONVENTION = 2
        1: "01-January",
        2: "02-February",
        3: "03-March",
        4: "04-April",
        5: "05-May",
        6: "06-June",
        7: "07-July",
        8: "08-August",
        9: "09-September",
        10: "10-October",
        11: "11-November",
        12: "12-December",
    }
    date = datetime.datetime.strptime(today, "%Y-%m-%d")
    month = monthTitles[date.month]
    # FOLDER NAME CONVENTIONS
    # 1: Path/to/vault/DailyNotesFolder/YYYY-MM-DD
    # 2: Path/to/vault/DailyNotesFolder/YY/MM/YYYY-MM-DD
    FOLDER_NAME_CONVENTION = 1
    DailyNotePath = {
        1: f'{DailyNotesFolder}/{date.year}/{month}/{DailyNoteName}',
        2: f'{DailyNotesFolder}/{DailyNoteName}'
    }
    try:
        return DailyNotePath[FOLDER_NAME_CONVENTION]
    except KeyError:
        print("You have set a folder naming convention which does not exist. See line 29 of the program.")


def getTime():
    currentTime = time.strftime("%H:%M")
    return str(currentTime)


def getEntry():
    print("Enter new entry below. To cancel, type 'exit'")
    entry = input("")
    return entry


def AppendToNote(entry):
    noteFile = open(currentDailyNote(), "a")
    noteFile.write(f'\n- {getTime()}: {entry}')
    noteFile.close()


print(f"Updating the note {currentDailyNote()}")
update = getEntry()
if update != 'exit':
    AppendToNote(update)
