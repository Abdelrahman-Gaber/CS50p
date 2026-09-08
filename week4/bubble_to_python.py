from datetime import datetime
from zoneinfo import ZoneInfo

def driver_boost(level_1_start:int, level_1_end:int,
                  level_2_start:int, level_2_end:int,
                    level_1_margin_share:int, level_2_margin_share:int,
                    level_1_max_boost:int, level_2_max_boost:int,
                    jobs_dict:dict):
    '''
        This functions checks the time of the day and according to it returns the minutes for every job in the window.
        Those minutes should then be used to schedule the job for increase by adding the minutes to the current time.
        Formula to boost the price is min((total price - driver price) / margin share, max boost)

        Level 1 and level 2 uses the same formula but might change the margin share and the max boost variables

        level_1_start: Starting hour of the day for level 1 price boosts
        level_1_end: Ending hour of the day for level 1 price boosts
        level_2_start: Starting hour of the day for level 2 price boosts
        level_2_end: Ending hour of the day for level 2 price boosts
        level_1_margin_share: Margin share for level 1 boost formula
        level_2_margin_share: Margin share for level 2 boost formula
        level_1_max_boost: Max boost for level 1 formula
        level_2_max_boost: Max boost for level 2 formula
        jobs_dict: Dictionary containing jobs
    '''
    # I want to get the current hour in UK timezone
    uk_datetime = datetime.now()
    hour = uk_datetime.hour
    curent_date_time_UNIX = int(uk_datetime.timestamp())

    for job in jobs_dict.values():
        if level_1_start == hour:
            job["minutes_to_schedule"] = (job["created_time_UNIX"] + curent_date_time_UNIX) % (level_1_end - level_1_start)
            job["new_driver_price_level_1"] = job['Driver Price'] + min(((job['total price'] - job['Driver Price']) 
                                                                         / level_1_margin_share), level_1_max_boost)

        elif level_2_start == hour:
            job["minutes_to_schedule"] = (job["created_time_UNIX"] + curent_date_time_UNIX) % (level_2_end - level_2_start)
            job["new_driver_price_level_2"] = job['Driver Price'] + min(((job['total price'] - job['Driver Price']) 
                                                                         / level_2_margin_share), level_2_max_boost)
    return jobs_dict


jobs = {
    "JOB_A": {"created_time_UNIX": 1700000000, "Driver Price": 100.0, "total price": 120.0},
    "JOB_B": {"created_time_UNIX": 1700000600, "Driver Price": 80.0,  "total price": 200.0},
    "JOB_C": {"created_time_UNIX": 1700001200, "Driver Price": 90.0,  "total price": 85.0},
    "JOB_D": {"created_time_UNIX": 1700001800, "Driver Price": 50.0,  "total price": 50.0},
    "JOB_E": {"created_time_UNIX": 1700002400, "Driver Price": 120.0, "total price": 132.0},
}

print(driver_boost(19, 21, 2, 5, 3, 3, 15, 20, jobs))

# CAN BE DONE BETTER?
# Create a function to create the price and calculate the minutes delay instead of repeating lines of code
#