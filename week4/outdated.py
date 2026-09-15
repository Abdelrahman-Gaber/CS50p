list_of_months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")
        if "/" in date:
            date_backslash = date.split(sep="/")

            if 1 <= int(date_backslash[0]) <= 12 and 1 <= int(date_backslash[1]) <= 31:
                print(f"{date_backslash[-1]}-{date_backslash[0]}-{date_backslash[1]}")

        else:
            date_month = date.split(sep=" ")
            date_month[2] = date_month[2]
            month = int(list_of_months.index(date_month[0].title()) + 1)
            day = int(date_month[1].strip(","))
                                         
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{date_month[-1]}-{month}-{day}")

    except IndexError:
        pass
    except EOFError:
        break
