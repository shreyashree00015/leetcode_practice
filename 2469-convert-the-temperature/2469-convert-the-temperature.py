class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        c= [celsius+273.15,celsius*1.8+32.00]
        return c