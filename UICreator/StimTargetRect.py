import numpy as np
import math


class StimTargetRect():
    def __init__(self, site_point, rect_size, fs, frequency, start_phase, max_amplitude):
        self.site_point = site_point
        self.rect_size = rect_size
        self.fs = fs
        self.frequency = frequency
        self.start_phase = start_phase
        self.max_amplitude = max_amplitude
        self.form_flag_matrix = np.ones(rect_size, dtype = 'bool')
        self.position = self.covert2psycho()
        
    def cal_brightness(self, frame_no):
        brightness = 0.5 + 0.5 * math.cos( 2 * math.pi * self.frequency /self.fs * frame_no + self.start_phase )
        return brightness

    def covert2psycho(self):
        width = self.rect_size/2
        x,y = self.site_point
        x = x-1920/2 + width
        y = y-1080/2 + width

        return [x,y]


