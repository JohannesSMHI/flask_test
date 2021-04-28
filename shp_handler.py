"""
Created on 2021-03-25 20:33
@author: johannes
"""
import geopandas as gp
from shapely.geometry import Point
import time


class ShapeHandler:
    def __init__(self):
        # start_time = time.time()
        self.shapes = gp.read_file('Havsomr_SVAR_2016_3b_cp1252.shp')
        # self.shapes = gp.read_feather('shapes.feather')
        # print("Timeit:--%.5f sec" % (time.time() - start_time))

    def find_area_for_point(self, lat, lon):
        boolean = self.shapes.contains(Point(float(lon), float(lat)))
        if any(boolean):
            return self.shapes[boolean]._to_geo()

    def get_key_value_for_point(self, lat, lon, key):
        boolean = self.shapes.contains(Point(float(lon), float(lat)))
        if any(boolean):
            return {key: self.shapes.loc[boolean, key].values[0]}

    def get_example(self, obj_id=48):
        boolean = self.shapes['OBJECTID'] == obj_id
        return self.shapes[boolean]._to_geo()

    # def get_area_long_name(self, poly_name):
    #     name = ''
    #     if poly_name:
    #         boolean = self.shapes['POLY_NAMN'].eq(poly_name)
    #         if any(boolean):
    #             name = self.shapes.loc[boolean, 'NAMN'].values[0]
    #     return name


if __name__ == '__main__':
    # shp_path = r'C:\Utveckling\w_sharktoolbox\SharkToolbox\data\shapefiles\SVAR 2016_3b\Havsomr_SVAR_2016_3b_cp1252.shp'
    # shp_path = r'shapes.feather'
    sh = ShapeHandler()
