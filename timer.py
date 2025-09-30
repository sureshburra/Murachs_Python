from datetime import datetime, time


def main():
    print("The Timer Program")
    print()

    _ = input("Press Enter to start...")
    start_time = datetime.now()
    print("Start time:", start_time)
    print()

    _ = input("Press Enter to stop...")
    stop_time = datetime.now()
    print("Stop time: ", stop_time)
    print()

    # Calculate elapsed time
    elapsed_time = stop_time - start_time
    days = elapsed_time.days
    minutes = elapsed_time.seconds // 60
    seconds = elapsed_time.seconds % 60
    microseconds = elapsed_time.microseconds

    # calculate hours and minutes
    hours = minutes // 60
    minutes = minutes % 60

    time_object = time(hours, minutes, seconds, microseconds)

    print("ELAPSED TIME")
    if days > 0:
        print("Days:", days)
    print("Time:", time_object)


if __name__ == "__main__":
    main()
