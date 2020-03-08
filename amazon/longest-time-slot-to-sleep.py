import math
from datetime import datetime
from datetime import timedelta


def solution(S: str) -> int:

    def to_time(t: str) -> datetime:
        return datetime.strptime(t, '%Y-%m-%d %H:%M')

    def fix_timeformat(t: str) -> datetime:
        if t.endswith('24:00'):
            d = t.split()[0]
            return datetime.strptime(d, '%Y-%m-%d') + timedelta(days=1)
        else:
            return to_time(t)

    weekdays = {
        'Mon': '2020-03-02',
        'Tue': '2020-03-03',
        'Wed': '2020-03-04',
        'Thu': '2020-03-05',
        'Fri': '2020-03-06',
        'Sat': '2020-03-07',
        'Sun': '2020-03-08'
    }
    start_of_week = to_time('2020-03-02 00:00')
    end_of_week = to_time('2020-03-09 00:00')

    # break the strings into real time slots
    lines = [[weekdays[l.split()[0]], l.split()[1].split('-')] for l in S.split('\n')]
    meetings = [(l[0] + ' ' + l[1][0], l[0] + ' ' + l[1][1]) for l in lines]

    timeslots = []
    for m in meetings:
        timeslots.append([fix_timeformat(m[0]), fix_timeformat(m[1])])
    meeting_slots = sorted(timeslots)

    # get all start time of sleeping slots
    sleep_start = [ start_of_week ]
    for s in meeting_slots:
        sleep_start.append(s[1])

    sleep_end = []
    for s in meeting_slots:
        sleep_end.append(s[0])
    sleep_end.append(end_of_week)

    sleep_slots = [slot[1] - slot[0] for slot in zip(sleep_start, sleep_end)]

    return max(sleep_slots).seconds // 60
        


if __name__ == '__main__':
    S = """Mon 01:00-23:00
Tue 01:00-23:00
Thu 01:00-23:00
Fri 01:00-23:00
Wed 01:00-24:00
Sat 01:00-23:00
Sun 01:00-21:00"""

    print(solution(S))
