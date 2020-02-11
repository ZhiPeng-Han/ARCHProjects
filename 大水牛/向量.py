#coding=utf-8
import rhinoscriptsyntax as rs
lines = rs.GetObjects("选中直线",rs.filter.curve)
#lines = rs.ObjectsByGroup()
#lines = rs.ObjectsByName(line,True)
if lines:
    for i in lines:
        rs.CurveArrows(i,2)