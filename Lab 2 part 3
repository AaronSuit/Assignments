import math

def recalculate_coordinate(val,_as=None):
  """
    Accepts a coordinate as a tuple (degree, minutes, seconds)
    You can give only one of them (e.g. only minutes as a floating point number) and it will be duly
    recalculated into degrees, minutes and seconds.
    Return value can be specified as 'deg', 'min' or 'sec'; default return value is a proper coordinate tuple.
  """
  deg,  min,  sec = val
  # pass outstanding values from right to left
  min = (min or 0) + int(sec) / 60
  sec = sec % 60
  deg = (deg or 0) + int(min) / 60
  min = min % 60
  # pass decimal part from left to right
  dfrac,  dint = math.modf(deg)
  min = min + dfrac * 60
  deg = dint
  mfrac,  mint = math.modf(min)
  sec = sec + mfrac * 60
  min = mint
  if _as:
    sec = sec + min * 60 + deg * 3600
    if _as == 'sec': return sec
    if _as == 'min': return sec / 60
    if _as == 'deg': return sec / 3600
  return deg,  min,  sec
      

def points2distance(slong, slat, elong, elat):
  """
    Calculate distance (in kilometers) between two points given as (long, latt) pairs
    based on Haversine formula (http://en.wikipedia.org/wiki/Haversine_formula).
    slong = Starting Longitude
    slat = Starting Latitude
    elong = ending Longitude
    elat = Ending Latitude
  """
  start = ((slong,0,0),(slat,0,0))
  end = ((elong,0,0),(elat,0,0))
  start_long = math.radians(recalculate_coordinate(start[0],  'deg'))
  start_latt = math.radians(recalculate_coordinate(start[1],  'deg'))
  end_long = math.radians(recalculate_coordinate(end[0],  'deg'))
  end_latt = math.radians(recalculate_coordinate(end[1],  'deg'))
  d_latt = end_latt - start_latt
  d_long = end_long - start_long
  a = math.sin(d_latt/2)**2 + math.cos(start_latt) * math.cos(end_latt) * math.sin(d_long/2)**2
  c = 2 * math.asin(math.sqrt(a))
  return 6371 * c

def distance_formula (x1, y1, x2, y2):
  xdiff = x2 - x1
  ydiff = y2 - y1
  xsquare = xdiff * xdiff
  ysquare = ydiff * ydiff
  distance = (xsquare + ysquare) ** 0.5
  return (distance)



slong = input("Give the X Coordinate of the first point ")
slong = float(slong)
slat = input("Give the Y Coordinate of the first point ")
slat = float(slat)
userInput = "Y"
total = 0
while(userInput.upper() == "Y" or userInput.upper() == "YES"):
    elong = input("Give the X Coordinate of the next point ")
    elong = float(elong)
    elat = input("Give the Y Coordinate of the next point ")
    elat = float(elat)
    currentDistance = points2distance(slong,slat,elong,elat)
    total = total + currentDistance
    print("Total distance of polyline: ", total, "km", "\nLength of current segment:  ",currentDistance, "km" )
    slong = elong
    slat = elat
    userInput = input("Would you like to add another point? (Please Answer as Y or N)")
    if userInput.upper() == "N" or userInput.upper() == "NO":
        print("Have a nice day.")
