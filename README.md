drifter
=========

Profiles of my programs

https://docs.google.com/spreadsheets/d/1h-958Liue0Z5BjmwmUWCyOmO4yN3jycgo79K2mOwyMI/pubhtml 




User can get ocean drifter data from erddap or raw by this program. 

If you want to get drifter data by raw , please modify control file 'getdrifter_ctl.txt' first. 

While you getting data from erddap , remember to modify hard code in process which you are going to run.

Some processes can save drifter data in a file , the others can plot them on pictures or html files.

Make sure to read process direction carefully before you run.

Reference :http://www.nefsc.noaa.gov/drifter/

There are flowcharts in this peckage to explain programs :

<a href="https://github.com/xhx509/drifter/blob/master/get_drifter_erddap.png">get_drifter_erddap.png</a>

<a href="https://github.com/xhx509/drifter/blob/master/get_drifter_erddap_plot">get_drifter_erddap_plot</a>

<a href="https://github.com/xhx509/drifter/blob/master/drifter_sink_flowchart.png">drifter_sink_flowchart.png</a>

<a href="https://github.com/xhx509/drifter/blob/master/drifter_source_flowchart.png">drifter_source_flowchart.png</a>

<a href="https://github.com/xhx509/drifter/blob/master/getdrifter_erddap_survive.png">getdrifter_erddap_survive.png</a>




List of programs:



drifter_est_dist.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; get error distances between estimate data and real drifter data

drifter_est.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; get track of estimated drifter and plot

drifter_sink.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; get real drifter track which start from a specified area

drifter_source.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  get real drifter track which come to a specified area

getdrifter_erddap_map.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  extract real drifter track and plot on google map

get_drifter_erddap_plot.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  extract erddap drifter data and plot it (not on google map)

getdrifter_erddap.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  extract erddap drifter data and save it

get_map_drifter.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  get raw drifter data and plot it on google map

get_raw_drifter.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; get raw drifter data and plot it (not on google map)

getdrifter_erddap_survive.py  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  count one type survive drifters and plot a graph

getdrifter_erddap_survive_more.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  count several types survive drifters and plot a graph
