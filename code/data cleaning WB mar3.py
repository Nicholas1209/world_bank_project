# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 12:58:14 2024

@author: yengl
"""

import pandas as pd 

ice_pre = pd.read_excel('C:/Users/yengl/OneDrive/Documents/ICE Just drivers_Pre survey.xlsx')
ice_daily = pd.read_excel('C:/Users/yengl/OneDrive/Documents/ICE Just drivers_Daily Survey.xlsx')

gw_daily = pd.read_excel('C:/Users/yengl/OneDrive/Documents/Greenwheels_daily survey_Pilot.xlsx')
gw_daily = gw_daily.drop(columns=['_id', '_uuid', '_submission_time', '_validation_status', '_notes', 'status', '_submitted_by', '__version__', '_tags', '_index','_status'])

gw_pre = pd.read_excel('C:/Users/yengl/OneDrive/Documents/World Bank Project/gw_pre_filtered.xlsx')


gw = pd.merge(gw_pre, gw_daily, on= 'name')


gw['Respondent ID'] = (pd.factorize(gw['name'])[0] + 1).astype(str)
gw['Respondent ID'] = 'GW' + gw['Respondent ID']

gw = gw[gw['home_labor'] + gw['leisure'] + gw['sleep'] <= 24]
gw['gross_income'] = gw['salary'] + gw['other_income_1']
gw = gw[gw['time_work']>=0]

ice_daily = ice_daily.drop(columns=['_id', '_uuid', '_submission_time', '_vAli Hassandation_status', '_notes', '_submitted_by', '__version__', '_tags', '_index','_status'])
ice_pre = ice_pre.drop(columns=['_id', '_uuid', '_submission_time', '_validation_status', '_notes', '_submitted_by', '__version__', '_tags', '_index','_status'])

ice = pd.merge(ice_pre, ice_daily, on='Respondent ID', )


ice = ice[ice['loan_length'] >= ice['loan_comp']]
ice = ice[ice['home_labor'] + ice['leisure'] + ice['sleep'] <= 24]
ice['gross_income'] = ice['income_boda'] + ice['income_other_1']
ice = ice[ice['time_work']>=0]

gw.to_excel('gw_filtered.xlsx', index = False)
ice.to_excel('ice_filtered.xlsx', index = False)
