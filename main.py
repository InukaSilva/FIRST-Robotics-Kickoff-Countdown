from datetime import datetime, timezone, timedelta


KICKOFF = datetime(2024, 1, 6, 17, tzinfo=timezone.utc)

def countdown(enddate):
    current_time = datetime.utcnow().replace(tzinfo=timezone.utc)
    difference = enddate - current_time
    days, hours = difference.days, difference.seconds//3600
    if days < 0 or hours < 0:
        return 0,0
    else:
        return days, hours

def update_readme(days, hours):
    # <h3 align='center'>Days Until Kickoff</h3>
    # <p3 align='center>___________________</p3>
    out_list = ""
    if days == 0 and hours == 0:
        out_list = [f"<h3 align='center'>Kickoff has been reached!</h3>\n"]
    else:
        out_list = [f"<h3 align='center'>{days} days and {hours} hours until Kickoff!</h3>\n"]
    final_output = []

    with open("README.md", "r") as file:
        final_output = []
        start_pos = 0
        end_pos = 0
        lines = file.readlines()
        for pos, line in enumerate(lines):
            if line == "<!---START-TIMER--->\n":
                start_pos = pos
            elif line == "<!---END-TIMER--->\n":
                end_pos = pos
        # Format everything
        final_output = lines[:start_pos+1] + out_list + lines[end_pos:]

    with open("README.md", "w") as file:
        for line in final_output:
            file.write(line)






days, hours = countdown(KICKOFF)
update_readme(days,hours)