#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 14:52:19 2020

@author: laurieshaw
"""
import numpy as np
import scipy.signal as signal

def calc_player_velocities(team, filter_='Savitzky-Golay', window=7, polyorder=1, maxspeed = 10):
    player_ids = np.unique( [ c[:-2] for c in team.columns if c[:4] in ['Home','Away'] ] )

    dt = team['Time [s]'].diff()
    second_half_idx = team.Period.idxmax(2)
    # estimate velocities for players in team1
    for player in player_ids: # cycle through players individually
        vx = team[player+"_x"].diff() / dt
        vy = team[player+"_y"].diff() / dt
        
        vx.loc[:second_half_idx] = signal.savgol_filter(vx.loc[:second_half_idx],window_length=window,polyorder=polyorder)
        vy.loc[:second_half_idx] = signal.savgol_filter(vy.loc[:second_half_idx],window_length=window,polyorder=polyorder)
        
        vx.loc[second_half_idx:] = signal.savgol_filter(vx.loc[second_half_idx:],window_length=window,polyorder=polyorder)
        vy.loc[second_half_idx:] = signal.savgol_filter(vy.loc[second_half_idx:],window_length=window,polyorder=polyorder)
        
        team[player + "_vx"] = vx
        team[player + "_vy"] = vy
        team[player + "_speed"] = np.sqrt( vx**2 + vy**2 )

        #dr[np.abs(dr)>maxspeed]=0. # perhaps should be nan, but this would affect surrounding frames
    return team