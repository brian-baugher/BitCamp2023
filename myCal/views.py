from django.shortcuts import render
from django.utils.safestring import mark_safe
from calendar import HTMLCalendar
from datetime import date
from .models import Event


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, events):
        events_per_day = events.filter(start_time__day=day)
        d = ''
        for event in events_per_day:
            d += f'<li> {event.get_html_url} </li>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True):
        events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal


def my_Cal_view(request):
    # today's date
    today = date.today()
    # get year and month from URL, or use current year/month
    year = today.year
    month = today.month
    # get all events for the selected month and year
    events = Event.objects.filter(start_time__year=year, start_time__month=month)
    # instantiate calendar
    cal = Calendar(int(year), int(month))
    # render calendar template with calendar table

    events_list = [
        [('', ''), ('', ''), ('', ''), ('1', ""), ('2', ), ('3', ''), ('4', '')],
        [('5', ''), ('6', ''), ('7', ''), ('8', ''), ('9', ''), ('10', 'CS Proj'), ('11', 'English')],
        [('12', ''), ('13', ''), ('14', ''), ('15', ''), ('16', ''), ('17', ''), ('18', '')],
        [('19', ''), ('20', ''), ('21', 'Paper'), ('22', ''), ('23', ''), ('24', ''), ('25', '')],
        [('26', ''), ('27', ''), ('28', ''), ('29', ''), ('30', ''), ('', ''), ('', '')],
    ]

    return render(request, 'myCal.html', {'calendar': mark_safe(cal.formatmonth(withyear=True)), 'events': events_list})
