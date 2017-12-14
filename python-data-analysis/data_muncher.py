# Module: datamuncher.py

# package imports
import unicodecsv
from datetime import datetime as dt

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')

def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)

# Clean up the data types
def clean_enrollments(enrollments):
    for enrollment in enrollments:
        enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
        enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
        enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
        enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
        enrollment['join_date'] = parse_date(enrollment['join_date'])
    return enrollments

def clean_engagements(daily_engagement):
    for engagement_record in daily_engagement:
        engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
        engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
        engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
        engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
        engagement_record['utc_date'] = parse_date(engagement_record['utc_date'])
        engagement_record['account_key'] = engagement_record['acct']
        del engagement_record['acct']
    return daily_engagement

def clean_submissions(project_submissions):
    for submission in project_submissions:
        submission['completion_date'] = parse_date(submission['completion_date'])
        submission['creation_date'] = parse_date(submission['creation_date'])
    return project_submissions

def funcname(parameter_list):
    pass

def get_unique_accounts(list_of_dicts):
    unique_accts = set()
    for d in list_of_dicts:
        unique_accts.add(d['account_key'])
    return unique_accts

def print_overview(c_enrollments,
                   c_daily_engagement,
                   c_project_submissions,
                   enrollments_count,
                   daily_engagement_count,
                   project_submissions_count,
                   unique_enrollments_count,
                   unique_daily_engagement_count,
                   unique_project_submissions_count):
    print c_enrollments[0]
    print c_daily_engagement[0]
    print c_project_submissions[0]
    print ''
    print 'Enrollment Count: ' + str(enrollments_count)
    print 'Daily Engagement Count: ' + str(daily_engagement_count)
    print 'Project Submission Count: ' + str(project_submissions_count)
    print 'Unique Enrollment Count: ' + str(unique_enrollments_count)
    print 'Unique Daily Engagement Count: ' + str(unique_daily_engagement_count)
    print 'Unique Project Submission Count: ' + str(unique_project_submissions_count)

def get_udacity_accts(enrollments):
    accts = list()
    for e in enrollments:
        if e['is_udacity']:
            accts.append(e['account_key'])
    return accts

def remove_udacity_accts(data, udacity_accts):
    c_data = list()
    for d in data:
        if d['account_key'] not in udacity_accts:
            c_data.append(d)
    return c_data

def get_paid_students(enrollments):
    paid_students = {}
    for e in enrollments:
        append = False
        if e.has_key('days_to_cancel'):
            if e['days_to_cancel'] == None or e['days_to_cancel'] > 7: 
                append = True
        else: 
            append = True
        if append: 
            key = e['account_key']
            date = e['join_date']
            if key not in paid_students or date > paid_students[key]:
                paid_students[key] = date
    return paid_students


def within_one_week(join_date, engagement_date):
    time_delta = engagement_date - join_date
    return time_delta.days < 7

def paid_in_week(daily_engagement, paid_students):
    psow = {}
    for de in daily_engagement:
        key = de['account_key']
        if key in paid_students and within_one_week(paid_students[key], de['utc_date']):
            psow[key] = paid_students[key]

    return psow
