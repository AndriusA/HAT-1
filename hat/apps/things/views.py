from django.shortcuts import render
import matplotlib
matplotlib.use('Agg')
from matplotlib import pylab
from pylab import *
import PIL
import PIL.Image
import StringIO
from django.http import HttpResponse
from django.template import RequestContext, loader
from ..things.models import SensorData

# Create your views here.

def graph(request):
	
	SensorData_list = SensorData.objects.filter(source_description="Downlights read").values('value')
	#SensorData_list = SensorData_list.objects.values('value')
	
	x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
	yTrans = []
	y=[]

	for list in SensorData_list:
	    #for xr in list:
	    yTrans.append(list.values())

	yTrans = [element for tupl in yTrans for element in tupl] 

	for d in range(0,15):
		y.append(yTrans[d])

	plot (x,y, linewidth=2)

	xlabel('Time')
	ylabel('Watts')
	pylab.ylim([0,30])
	title('Downlights')
	grid(True)
	#pylab.show()

	buffer = StringIO.StringIO()
	canvas = pylab.get_current_fig_manager().canvas
	canvas.draw()
	graphIMG = PIL.Image.fromstring("RGB",canvas.get_width_height(),canvas.tostring_rgb())
	graphIMG.save(buffer, "PNG")
	pylab.close()

	return HttpResponse(buffer.getvalue(), mimetype="image/png")


