"""
Author: Ben Bornholm
Date: 9-4-16
Description: Produce SVG graphs to vizualize Bro logs
"""
import pygal

def createGraph(entryLst):
    """
    Create a pie chart of all IP addresses
    """
    # pie chart for ip addres
    pieIP_chart = pygal.Pie()
    pieIP_chart.title = 'Number of IP Address'

    ipDict = {}
    for entry in entryLst:
        if entry['id.orig_h'] not in ipDict:
            ipDict[entry['id.orig_h']] = 1
        else:
            ipDict[entry['id.orig_h']] +=1

    for key, value in ipDict.iteritems():
        pieIP_chart.add(key,value)

    pieIP_graph_data = pieIP_chart.render_data_uri()

    """
    Create a pie chart of all DNS queries
    """
    # pie chart for ip addres
    pieQuery_chart = pygal.Pie()
    pieQuery_chart.title = 'Number of DNS Queries'

    ipDict = {}
    for entry in entryLst:
        if entry['query'] == '-':
            continue
        elif entry['query'] not in ipDict:
            ipDict[entry['query']] = 1
        else:
            ipDict[entry['query']] +=1

    for key, value in ipDict.iteritems():
        pieQuery_chart.add(key,value)

    pieQuery_graph_data = pieQuery_chart.render_data_uri()

    #Return the data for the graph
    return pieIP_graph_data, pieQuery_graph_data
