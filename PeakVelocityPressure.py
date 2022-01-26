from math import log


class PeakVelocityPressure(object):
    '''
    Wyznacza wartość szczytowej wartości ciśnienia wiatru
    '''

    def __init__(self, zone, terraincat, above, height):

        self._zone = zone
        self._terraincat = terraincat
        self._above = above
        self._height = height

    def basicwindvelocity(self):

        zoneabove = round(22*(1+0.0006*(self._above - 300)),0)
        tuple_zone = (22, zoneabove, 26)
        if self._zone == 1 or self._zone == 3 and self._above <= 300:
            vb0 = tuple_zone[0]
        elif self._zone == 1 or self._zone ==3 and self._above > 300:
            vb0 = tuple_zone[1]
        elif self._zone == 2:
            vb0 = tuple_zone[2]
        
        cdir = 1.0
        cseason = 1.0
        vb = vb0 * cdir * cseason

        return vb

    def meanwindvelocity(self):

        vb = self.basicwindvelocity()
        tuple_zo = (0.003, 0.01, 0.05, 0.3, 1.0)
        tuple_zmin = (1,1,2,5,10)
        kr = round(0.19 * (tuple_zo[self._terraincat]/0.05)**0.07,3)

        if self._height >= tuple_zmin[self._terraincat] and self._height <= 200:
            cr = round(kr * log(self._height/tuple_zo[self._terraincat]),3)
        elif self._height <= tuple_zmin[self._terraincat]:
            cr = round(kr * log(tuple_zmin[self._terraincat]/tuple_zo[self._terraincat]),3)

        c0 = 1.0
        vm = round(cr * c0 * vb,3)

        return vm

    def exposurefactorcoef(self):
        
        const = self._height/10

        tuple_ce = (3.0*const**0.17, 2.8*const**0.19, 2.3*const**0.24, 1.9*const**0.26, 1.5*const**0.29)
        ce = round(tuple_ce[self._terraincat],3)

        return ce


    
    def peakvelocitypressure(self):
        vb = self.basicwindvelocity()
        ce = self.exposurefactorcoef()
        p = 1.25
        qb = round(0.5 * p * vb**2 * 0.001,3)

        qbf = round(ce * qb,3)

        return qbf 


  
        

if __name__ == '__main__':
    test = PeakVelocityPressure(3,4,300, 20)
    value = test.peakvelocitypressure()
    print (value)
    