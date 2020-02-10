from ResolutionType import ResolutionType

class Resolution:

    def __init__(self, quality : tuple) :
        self.quality = quality
        self.tier = self._get_tier()
    
    def get_tier(self) : 
        return self.tier
    
    def get_width(self) :
        return self.quality[ResolutionType.Width]

    def get_height(self) :
        return self.quality(ResolutionType.Height)

    def get_quality(self) -> tuple :
        return self.quality

    def set_quality(self, quality : tuple) :
        self.quality = quality
    
    def _get_tier(self) -> int :
        if self.quality == (1920,1080) :
            return 6
        elif self.quality == (2560,1440) :
            return 7