#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 14:52:19 2020

Module for measuring player velocities, smoothed using a Savitzky-Golay filter, with Metrica tracking data.

Data can be found at: https://github.com/metrica-sports/sample-data

@author: Laurie Shaw (@EightyFivePoint)

"""
import numpy as np
import scipy.signal as signal

def calc_player_velocities(team, filter_='Savitzky-Golay', window=7, polyorder=1, maxspeed = 10):
    # Get the player ids
    player_ids = np.unique( [ c[:-2] for c in team.columns if c[:4] in ['Home','Away'] ] )

    # Calculate the timestep from one frame to the next. Should always be 0.04 within the same half
    dt = team['Time [s]'].diff()
    # index of first frame in second half
    second_half_idx = team.Period.idxmax(2)
    # estimate velocities for players in team
    for player in player_ids: # cycle through players individually
        # difference player positions in timestep dt to get unsmoothed estimate of velicity
        vx = team[player+"_x"].diff() / dt
        vy = team[player+"_y"].diff() / dt
        
        # calculate first half velocity
        vx.loc[:second_half_idx] = signal.savgol_filter(vx.loc[:second_half_idx],window_length=window,polyorder=polyorder)
        vy.loc[:second_half_idx] = signal.savgol_filter(vy.loc[:second_half_idx],window_length=window,polyorder=polyorder)
        
        # calculate second half velocity
        vx.loc[second_half_idx:] = signal.savgol_filter(vx.loc[second_half_idx:],window_length=window,polyorder=polyorder)
        vy.loc[second_half_idx:] = signal.savgol_filter(vy.loc[second_half_idx:],window_length=window,polyorder=polyorder)
        
        # put player speed in x,y direction, and total speed back in the data frame
        team[player + "_vx"] = vx
        team[player + "_vy"] = vy
        team[player + "_speed"] = np.sqrt( vx**2 + vy**2 )

        #still need to implement a maxspeed cut-off
    return team