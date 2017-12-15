# module: main.py

# from data_muncher import *

# # global variables
# enrollments = None
# daily_engagement = None
# project_submissions = None

# # read data
# enrollments = read_csv('data/enrollments.csv')
# daily_engagement = read_csv('data/daily_engagement.csv')
# project_submissions = read_csv('data/project_submissions.csv')

# # clean up data
# c_enrollments = clean_enrollments(enrollments)
# c_daily_engagement = clean_engagements(daily_engagement)
# c_project_submissions = clean_submissions(project_submissions)

# udacity_accts = get_udacity_accts(c_enrollments)

# c_enrollments = remove_udacity_accts(c_enrollments, udacity_accts)
# c_daily_engagement = remove_udacity_accts(c_daily_engagement, udacity_accts)
# c_project_submissions = remove_udacity_accts(c_project_submissions, udacity_accts)

# # get quick overview
# enrollments_count = len(c_enrollments)
# daily_engagement_count = len(c_daily_engagement)
# project_submissions_count = len(c_project_submissions)

# unique_enrollments = get_unique_accounts(c_enrollments)
# unique_engagements = get_unique_accounts(c_daily_engagement)
# unique_submissions = get_unique_accounts(c_project_submissions)

# unique_enrollments_count = len(unique_enrollments)
# unique_daily_engagement_count = len(unique_engagements)
# unique_project_submissions_count = len(unique_submissions)

# # show quick overview
# print_overview(c_enrollments, c_daily_engagement, c_project_submissions,
#                enrollments_count, daily_engagement_count, project_submissions_count,
#                unique_enrollments_count, unique_daily_engagement_count, unique_project_submissions_count)

# paid_students = get_paid_students(c_enrollments)
# paid_students_within_one_week = paid_in_week(c_daily_engagement, paid_students)

# print ''

# All of this in Panda
import os
import pandas as pd

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

daily_engagement = pd.read_csv('data/daily_engagement.csv')
print len(daily_engagement['acct'].unique())
