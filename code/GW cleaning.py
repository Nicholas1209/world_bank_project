# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 12:30:44 2024

@author: yengl
"""

import pandas as pd 

# Load Pre-survey
gw_pre = pd.read_excel('C:/Users/yengl/OneDrive/Documents/Greenwheels_pre survey_Pilot.xlsx')

# Find unique phone numbers
unique = gw_pre['phone'].unique()
gw_pre = gw_pre[gw_pre['phone'].isin(unique)]

# Export GW Presurvey
gw_pre.to_excel('gw_pre_filtered.xlsx', index=False)

# GW Data cleaning done on excel.
# Names are corrected to match.

