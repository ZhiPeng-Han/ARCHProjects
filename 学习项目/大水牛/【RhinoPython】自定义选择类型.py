#coding=utf-8

import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino as r

def select_line(rhino_object,geo,geo_index):
    cv = rs.coercecurve(geo)
    return rs.IsLine(cv) and rs.CurveLength(cv)>40

def commond():
    geos = rs.GetObjects("选择直线",rs.filter.curve,True,True,custom_filter=select_line)
    color = rs.GetColor(0)
    if geos and color:
        [rs.ObjectColor(i,color)for i in geos]

if __name__=="__main__":
    commond()