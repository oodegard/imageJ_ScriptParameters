from ij import IJ, ImagePlus, WindowManager
from ij.gui import OvalRoi, Roi, WaitForUserDialog, PointRoi, Line
from loci.plugins import BF
from ij.plugin.frame import RoiManager
from ij.plugin import Duplicator

#@ ImagePlus imp
#@ Integer(label = "line_radius") line_radius

def getlineplot(x, y, line_radius):
	imp = IJ.getImage()
	imp.show()
	#y1 = y-1 - line_radius
	#y2 = y+1 + line_radius
	#x1 = x-1 - line_radius
	#x2 = x+1 + line_radius	

	x_values_left =   [imp.getPixel(x, y_)[0] for y_ in range(y-line_radius+1, y+1, 1) ]
	x_values_left = [v for v in reversed(x_values_left)]
	x_values_right =  [imp.getPixel(x, y_)[0] for y_ in range(y+2, y+line_radius+2, 1) ]	
	
	y_values_left =   [imp.getPixel(x_, y)[0] for x_ in range(x-line_radius+1, x+1, 1) ]
	y_values_left = [v for v in reversed(y_values_left)]
	y_values_right =  [imp.getPixel(x_, y)[0] for x_ in range(x+2, x+line_radius+2, 1) ]

	x_left = findMaxima(x_values_left, 0.9, line_radius)
	x_right = findMaxima(x_values_right, 0.9, line_radius)
	y_left = findMaxima(y_values_left, 0.9, line_radius)
	y_right = findMaxima(y_values_right, 0.9, line_radius)

	return [[[line_radius - x_left[0] + 1, line_radius + 1 + x_right[0] + 2 ], [x_left[1], x_right[1]]],[[line_radius - y_left[0] + 1, line_radius + 1 + y_right[0] +2], [y_left[1], y_right[1]]]]
	
	
# Searches for the highest value in the list from the left
# When values are decreasing and value is above threshold (e.g. 90% of max) the maxima is locked
def findMaxima(array, threshold, line_radius):
	print(array)
	local_max = 0
	previous_rel_intensity = 0
	for i, value in enumerate(array):
		print "i", i
		print "value", value
		if(value > local_max): # find local maximum
			local_max = value
			#print "new max"
		
		rel_intensity = float(value-min(array))/float(max(array) - min(array))
		# If maximum value is reached
		if(rel_intensity == 1):
			return [i, array[i]]
		
		# Stop seaching when value goes down, and previous value was above threshold
		if(value < array[max(i-1, 0)] and previous_rel_intensity > threshold):
			#print "value goes down, and previous value was above threshold"
			return [i - 1, array[i-1]]
		previous_rel_intensity = rel_intensity
	return [i, value]
	
# run program
def main(line_radius):
	#imp = IJ.getImage()
	rm = RoiManager.getInstance()
	coords_list = []
	for i, r in enumerate(rm):
		print r, i
		rm.select(i)
		p = r.getPolygon()
		x = p.xpoints[0]
		y = p.ypoints[0]
		z = r.ZPosition
		c = r.TPosition # Fix swapped dimensions
		coords = getlineplot(x, y, line_radius)
		coords_list.append(coords)
		print(coords)
		toOvalRoi(imp, x, y, coords, line_radius)	
		rm.runCommand(imp,"Update");
		#imp2 = Duplicator().run(imp, 1, 1, 1, 1, 31, 31)
		#imp2.show()
		#crasr
	print coords

def toOvalRoi(imp, x, y, coords, line_radius):
	new_x = ((x - line_radius + coords[1][0][0]) + (x - line_radius + coords[1][0][1]))/2
	new_y = ((y - line_radius + coords[0][0][0]) + (y - line_radius + coords[0][0][1]))/2
	x_rad = float(max(coords[1][0]) - min(coords[1][0]))/2
	y_rad = float(max(coords[0][0]) - min(coords[0][0]))/2
	imp.setRoi(OvalRoi(new_x  - x_rad, new_y - y_rad , x_rad*2 , y_rad*2))
	#print new_x	

# Run
# main(line_radius)
imp.show()


