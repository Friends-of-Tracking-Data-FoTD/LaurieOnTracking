#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 13:19:08 2020

@author: laurieshaw
"""

import Metrica_IO as mio
import Metrica_Viz as mviz

# set up initial path
DATADIR = '/Users/laurieshaw/Documents/Football/Data/TrackingData/Metrica/sample-data-master/data'
game_id = 2

events = mio.read_event_data(DATADIR,game_id)

# look in variable explorer
# print on screen

events['Type'].value_counts()

# Bit of housekeeping: unit conversion
events = mio.to_metric_coordinates(events)

# by team

home_events = events[events['Team']=='Home']
away_events = events[events['Team']=='Away']

home_events['Type'].value_counts()
away_events['Type'].value_counts()

# by type

shots = events[events['Type']=='SHOT']
home_shots = home_events[home_events.Type=='SHOT']
away_shots = away_events[away_events.Type=='SHOT']

home_shots['Subtype'].value_counts()
away_shots['Subtype'].value_counts()

# which player?
home_shots['From'].value_counts()

# get goals
home_goals = home_shots[home_shots['Subtype'].str.contains('-GOAL')].copy()
away_goals = away_shots[away_shots['Subtype'].str.contains('-GOAL')].copy()

# get minute timings
home_goals['Minute'] = home_goals['Start Time [s]']/60.

# look at first goal - what happened?. Data viewer: short corner.

# plot shots - PLOTTEDR
fig,ax = mviz.plot_pitch()
ax.plot( events.loc[198]['Start X'], events.loc[198]['Start Y'], 'ro' )
ax.annotate("", xy=events.loc[198][['End X','End Y']], xytext=events.loc[198][['Start X','Start Y']], alpha=0.6, arrowprops=dict(arrowstyle="->",color='r'))

# plot passing move in run up to goal
mviz.plot_events( events.loc[190:198], indicators = ['Marker','Arrow'] )

# TRACKING DATA

# READING IN TRACKING DATA
tracking_home = mio.tracking_data(DATADIR,game_id,'Home')
tracking_away = mio.tracking_data(DATADIR,game_id,'Away')

tracking_home.columns

# CONVERT TO PITCH COORDINATES
tracking_home = mio.to_metric_coordinates(tracking_home)
tracking_away = mio.to_metric_coordinates(tracking_away)

# Plot some player trajectories
fig,ax = mviz.plot_pitch()
ax.plot( tracking_home['Home_11_x'].iloc[:1500], tracking_home['Home_11_y'].iloc[:1500], 'r.', MarkerSize=1)
ax.plot( tracking_home['Home_1_x'].iloc[:1500], tracking_home['Home_1_y'].iloc[:1500], 'b.', MarkerSize=1)
ax.plot( tracking_home['Home_2_x'].iloc[:1500], tracking_home['Home_2_y'].iloc[:1500], 'g.', MarkerSize=1)
ax.plot( tracking_home['Home_3_x'].iloc[:1500], tracking_home['Home_3_y'].iloc[:1500], 'k.', MarkerSize=1)
ax.plot( tracking_home['Home_4_x'].iloc[:1500], tracking_home['Home_4_y'].iloc[:1500], 'c.', MarkerSize=1)

# PLOT POSITION AT KICK OFF
fig,ax = mviz.plot_frame( tracking_home.loc[51], tracking_away.loc[51] )

# PLOT POISTIONS AT GOAL
fig,ax = mviz.plot_events( events.loc[198:198], indicators = ['Marker','Arrow'], annotate=True )
frame = events.loc[198]['Start Frame']
fig,ax = mviz.plot_frame( tracking_home.loc[frame], tracking_away.loc[frame] )

# END CLASS ONE
