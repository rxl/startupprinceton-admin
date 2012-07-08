#!/usr/bin/python

try:
  from xml.etree import ElementTree
except ImportError:
  from elementtree import ElementTree
import gdata.calendar.data
import gdata.calendar.client
import gdata.acl.data
import atom
import getopt
import sys
import string
import time
import datetime
import re
import pytz

class CalPrinter:
    def __init__(self, email, password):
        self.cal_client = gdata.calendar.client.CalendarClient()
        self.cal_client.ClientLogin(email, password, self.cal_client.source);
    
    def _DateRangeQueryAll(self, start_date='2007-01-01', end_date='2007-07-01', fullInfo = True, opportunitiesOnly = False):
        feed = self.cal_client.GetAllCalendarsFeed()
        for i, a_calendar in zip(xrange(len(feed.entry)), feed.entry):
            if (a_calendar.title.text == "The Princeton Entrepreneurship Club"):
                self._DateRangeQuery(a_calendar, start_date, end_date, fullInfo, opportunitiesOnly)
    
    def _FormatDate(self, eventDate):
        day_names = ["Sun", "Mon", "Tues","Wed", "Thurs", "Fri", "Sat"]
        month_names = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July",
            "Aug", "Sept", "Oct", "Nov", "Dec"]
        local = pytz.timezone('US/Eastern')
        utc = pytz.timezone('UTC')
        fmt = '%Y-%m-%d %H:%M:%S %Z%z'
        e1 = eventDate.replace("T", " ").replace(".000Z", "")
        naive = datetime.datetime.strptime(e1, "%Y-%m-%d %H:%M:%S")
        utc_dt = naive.replace (tzinfo = utc)
        local_dt = utc_dt.astimezone (local)
        am_pm = "am"
        inthours = int(local_dt.hour)
        if inthours < 0:
            inthours += 24
        if inthours > 12:
            inthours -= 12
            am_pm = "pm"
        strminutes = str(local_dt.minute)
        if local_dt.minute < 10:
            strminutes = "0" + str(local_dt.minute)
        return month_names[int(local_dt.month)-1] + " " + str(local_dt.day) + ", " + str(inthours) + ":" + strminutes + am_pm
    
    def _DateRangeQuery(self, calendar, start_date='2007-01-01', end_date='2007-07-01', fullInfo = True, opportunitiesOnly = False):
        query = gdata.calendar.client.CalendarEventQuery(start_min=start_date,
            start_max=end_date, orderby="starttime", sortorder="ascending")
        feed = self.cal_client.GetCalendarEventFeed(uri=calendar.content.src, q=query)
        
        for i, an_event in zip(xrange(len(feed.entry)), feed.entry):
            is_an_opportunity = False
            for a_where in an_event.where:
                if (a_where.value == "nonevent" or a_where.value == "opportunity" or a_where.value == "deadline"):
                    is_an_opportunity = True
            if (is_an_opportunity == opportunitiesOnly):
                titletext = an_event.title.text
                titlelink = ""
                parts = re.split('[()]', an_event.title.text)
                if len(parts) >= 3:
                    titletext = parts[0].strip()
                    titlelink = parts[1].strip()
            
                if (fullInfo is True):
                    # print out the title of the event
                    print "<p>"
                    if (titlelink != ""):
                        print '<a href="%s"><strong>%s</strong></a><br />' % (titlelink, titletext,)
                    else:
                        print '<strong>%s</strong><br />' % (titletext,)

                    # print out the time of the event
                    for a_when in an_event.when:
                        if is_an_opportunity:
                            print '<strong>Deadline: </strong>%s<br />' % (self._FormatDate(a_when.start),)
                        else:
                            print '<strong>When: </strong>%s<br />' % (self._FormatDate(a_when.start),)
                        #print '\t\tStart time: %s' % (a_when.start,)
                        #print '\t\tEnd time:   %s' % (a_when.end,)

                    # print out the location of the event
                    if is_an_opportunity is False:
                        locationPrinted = False
                        for a_where in an_event.where:
                            if (a_where.value != ""):
                                print '<strong>Where: </strong>%s<br />' % (a_where.value,)
                                locationPrinted = True
                        if (locationPrinted is False):
                            print "<strong>Where: </strong>EVENT LOCATION<br />"

                    # print out the description of the event
                    if (an_event.content.text != None):
                        print "%s" % (an_event.content.text,)
                    else:
                        print "EVENT DESCRIPTION"
                    print '</p>'
                else:
                    print "<p>"
                    for a_when in an_event.when:
                        print self._FormatDate(a_when.start)
                    if (titlelink != ""):
                        print ' - <a href="%s"><strong>%s</strong></a><br />' % (titlelink, titletext,)
                    else:
                        print ' - <strong>%s</strong><br />' % (titletext,)
                    print "</p>"
    
    def PrintThisWeeksEvents(self):
        today = datetime.date.today()
        oneWeekFromToday = today + datetime.timedelta(days=7)
        self._DateRangeQueryAll(today, oneWeekFromToday, fullInfo = True)
    
    def PrintNextWeeksEvents(self):
        today = datetime.date.today()
        oneWeekFromToday = today + datetime.timedelta(days=7)
        twoWeeksFromToday = today + datetime.timedelta(days=14)
        self._DateRangeQueryAll(oneWeekFromToday, twoWeeksFromToday, fullInfo = False)
    
    def PrintUpcomingOpportunities(self):
        today = datetime.date.today()
        oneWeekFromToday = today + datetime.timedelta(days=7)
        sixMonthsFromToday = today + datetime.timedelta(days=6*30)
        self._DateRangeQueryAll(today, sixMonthsFromToday, fullInfo = True, opportunitiesOnly = True)

def generateEmail(user, pw):
    print """<p>Hey E-Club,<br /><br />
        We have some announcements for you. Check out more info below.</p>
        <p>Alex Landon and Ryan Shea<br />
        Presidents, The Princeton Entrepreneurship Club</p>
        <h3 class="h3">This Week's Events</h3><hr>"""
    cal = CalPrinter(user, pw)
    delete = False
    cal.PrintThisWeeksEvents()
    print """<h3 class="h3">Upcoming Events</h3><hr>"""
    cal.PrintNextWeeksEvents()
    print """<h3 class="h3">Career Opportunities</h3><hr>"""
    cal.PrintUpcomingOpportunities()

def main():
    # parse command line options
    try:
      opts, args = getopt.getopt(sys.argv[1:], "", ["user=", "pw="])
    except getopt.error, msg:
      print ('python calendarExample.py --user [username] --pw [password] ')
      sys.exit(2)

    user = ''
    pw = ''

    # Process options
    for o, a in opts:
      if o == "--user":
        user = a
      elif o == "--pw":
        pw = a

    if user == '' or pw == '':
      print ('python calendarExample.py --user [username] --pw [password] ')
      sys.exit(2)
    
    generateEmail(user, pw)
    
if __name__ == '__main__':
    main()

