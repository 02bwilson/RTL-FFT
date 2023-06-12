from rtlsdr import RtlSdr

import time


class SDRManager:
    
    def __init__(self) -> None:
        self.sdr_object = None
        
    def createSDRObject(self) -> None:
        """Creates the SDR object and initialize it.
        """
        self.sdr_object = RtlSdr()
        
    def setSDRSettings(self, sample_rate: float, center_freq: float, freq_correction: float, gain: str) -> None:
        """Set the settings for the SDR object.
        Args:
            sample_rate (float): [description]
            center_freq (float): [description]
            freq_correction (float): [description]
            gain (str): [description]
        """
        self.sdr_object.set_sample_rate(sample_rate)
        self.sdr_object.set_center_freq(center_freq)
        #self.sdr_object.set_freq_correction(freq_correction)
        self.sdr_object.set_gain(gain)
    
    def getSamples(self, num_samples: int = 2048):
        """Get a given number of samples from the SDR

        Returns:
            list(complex): [description]
        """
        return self.sdr_object.read_samples(num_samples)
        
    def getSpectrumSamples(self, freq_list: list, num_samples: int):
        """Reads a given number of samples from the spectrum (list of frequencies) and returns a list of them.

        Args:
            freq_list (list): [description]
            num_samples (int, optional): [description]. Defaults to 1024.

        Returns:
            [type]: [description]
        """
        total_samples = []
        for freq in freq_list:
            #self.sdr_object.set_center_freq(freq)
            total_samples += [self.sdr_object.read_samples(num_samples)]
            
        return total_samples
        