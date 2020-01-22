from cpsc import cpsc_generate
from yins import yins_generate
from franke import franke_generate

if __name__ == '__main__':
    cpsc_generate('calendars/cpsc_events.ics')
    yins_generate('calendars/yins_events.ics')
    franke_generate('calendars/franke_events.ics')

