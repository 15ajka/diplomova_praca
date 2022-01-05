from shapely.geometry.point import Point
from shapely.geometry import Polygon
from shapely import affinity
import matplotlib.pyplot as plt

circle = Point(0,0).buffer(6.0)
multi = Polygon([(0,0), (1,0), (1,1), (0, 1)])
multi2 = Polygon([(3,3), (4,4), (3,4)])
multi_rot = affinity.rotate(multi, 45, 'center')
x,y = multi.exterior.xy
x2,y2 = multi_rot.exterior.xy
x3,y3 = circle.exterior.xy
x4,y4 = multi2.exterior.xy
print(multi2.intersects(circle))
plt.plot(x,y)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.plot(x4,y4)
plt.show()
