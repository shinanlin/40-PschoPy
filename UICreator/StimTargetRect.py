import numpy as np
import math
import scipy.io as scio


class StimTargetRect():
    def __init__(self, rectINX, site_point, rect_size, fs, frequency, start_phase, max_amplitude):
        self.rectINX = rectINX
        self.site_point = site_point
        self.rect_size = rect_size
        self.fs = fs
        self.frequency = frequency
        self.start_phase = start_phase
        self.max_amplitude = max_amplitude
        self.form_flag_matrix = np.ones(rect_size, dtype = 'bool')
        self.position = self.covert2psycho()
        
    def cal_brightness(self, frame_no, paradigm):
        
        # for ssvep
        # brightness = 0.5 + 0.5 * math.cos( 2 * math.pi * self.frequency /self.fs * frame_no + self.start_phase )
        
        # for wn
        # else:
        #     brightness=self.stim_each_rect[frame_no-1]

        if paradigm=='wn':
            stim = scio.loadmat('code\\finalstim.mat')['wn']
            stim_this_rect = stim[:,self.rectINX]
            brightness = stim_this_rect[frame_no-1]
        
        elif paradigm == 'ssvep':
            brightness = 0.5 + 0.5 * math.sin( 2 * math.pi * self.frequency /self.fs * frame_no + self.start_phase )
        
        return brightness

    def covert2psycho(self):
        width = self.rect_size/2
        x,y = self.site_point
        x = x-1920/2 + width
        y = y-1080/2 + width

        return [x,y]



# class StimTargetRectwn():
#     def __init__(self, stim_each_rect, site_point, rect_size, fs, max_amplitude):
#         self.stim_each_rect = stim_each_rect
#         self.site_point = site_point
#         self.rect_size = rect_size
#         self.fs = fs
#         self.max_amplitude = max_amplitude
#         self.form_flag_matrix = np.ones(rect_size, dtype = 'bool')
#         self.position = self.covert2psycho()
        
#     def cal_brightness(self, frame_no, paradigm):
        
#         # for ssvep
#         # if paradigm == 'ssvep':
#         #     brightness = 0.5 + 0.5 * math.cos( 2 * math.pi * self.frequency /self.fs * frame_no + self.start_phase )
        
#         # for wn
#         stim = scio.loadmat()
#         brightness=self.stim_each_rect[frame_no-1]
        
#         return brightness

#     def covert2psycho(self):
#         width = self.rect_size/2
#         x,y = self.site_point
#         x = x-1920/2 + width
#         y = y-1080/2 + width

#         return [x,y]
