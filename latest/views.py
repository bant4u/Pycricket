from django.shortcuts import render_to_response, get_object_or_404, redirect
from latest.models import Game
from latest.forms import NewSportForm


def index(request):
	form=NewSportForm()
	#import pdb
	#pdb.set_trace()
	if request.method=='POST':
		form=NewSportForm(request.POST)
		if form.is_valid():
			form.save()
			print "success"
			return render(request,'latest/error.html',{'error_message':form})
	return render(request,'latest/index.html',{'form':form})

def latest(request):
	form=NewSportForm()
	#import pdb
	#pdb.set_trace()
	if request.method=='POST':
		form=NewSportForm(request.POST)
		if form.is_valid():
			form.save()
			print "success"
			return render(request,'latest/error.html',{'error_message':form})
	return render(request,'latest/success.html',{'form':form})

def game(request):
	from xml.dom import minidom
	import urllib
	url = "http://synd.cricbuzz.com/j2me/1.0/livematches.xml"
	dom = minidom.parse(urllib.urlopen(url))
	#minidom.parse('livematches.xml')
	print dom

	#mATCH nAME
	itemlist = dom.getElementsByTagName('match')


	statelist = dom.getElementsByTagName('state')



	momlist=dom.getElementsByTagName('mom')

	return render_to_response('latest/gamedetails.html', {'itemlist':itemlist,'statelist':statelist,'momlist':momlist})


