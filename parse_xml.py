#!/usr/bin/env python

from xml.dom.minidom import parse
import xml.dom.minidom
import pdb

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("data.xml")
collection = DOMTree.documentElement

master_output_list = []
master_output_list_header = []

# Get all the movies in the collection
cycle_list = collection.getElementsByTagName("cycle")
for cycle in cycle_list:
    #pdb.set_trace()
    gc_start_end_output_list_header = []
    gc_start_end_output_list = []
    gc_start_list = cycle.getElementsByTagName("gc-start")

    # Print detail of each movie.
    gc_start_output_list_header = []
    gc_start_output_list = []
    for gc in gc_start_list:
        gc_node_name = gc.nodeName
        for mem in gc.getElementsByTagName("mem"):
            tlist_header = []
            tlist = []

            mem_header = gc_node_name + '_' + mem.getAttribute("type")

            tlist_header.append(mem_header + '_' + 'free')
            if mem.hasAttribute("free"):
                tlist.append(mem.getAttribute("free"))
            else:
                tlist.append("")

            tlist_header.append(mem_header + '_' + 'total')
            if mem.hasAttribute("total"):
                tlist.append(mem.getAttribute("total"))
            else:
                tlist.append("")

            tlist_header.append(mem_header + '_' + 'percent')
            if mem.hasAttribute("percent"):
                tlist.append(mem.getAttribute("percent"))
            else:
                tlist.append("")

            gc_start_output_list_header.append(",".join(tlist_header))
            gc_start_output_list.append(",".join(tlist))

    gc_start_end_output_list_header.append((",".join(gc_start_output_list_header)))
    gc_start_end_output_list.append((",".join(gc_start_output_list)))

    # Get all the movies in the collection
    gc_end_output_list = []
    gc_end_output_list_header = []
    gc_end_list = cycle.getElementsByTagName("gc-end")

    for gc in gc_end_list:
        gc_node_name = gc.nodeName
        for mem in gc.getElementsByTagName("mem"):
            tlist = []
            tlist_header = []

            tlist_header.append(mem_header + '_' + 'free')
            if mem.hasAttribute("free"):
                tlist.append(mem.getAttribute("free"))
            else:
                tlist.append("")

            tlist_header.append(mem_header + '_' + 'total')
            if mem.hasAttribute("total"):
                tlist.append(mem.getAttribute("total"))
            else:
                tlist.append("")

            tlist_header.append(mem_header + '_' + 'percent')
            if mem.hasAttribute("percent"):
                tlist.append(mem.getAttribute("percent"))
            else:
                tlist.append("")

            gc_end_output_list.append(",".join(tlist))
            gc_end_output_list_header.append(",".join(tlist_header))

    gc_start_end_output_list.append((",".join(gc_end_output_list)))
    gc_start_end_output_list_header.append((",".join(gc_end_output_list_header)))

    master_output_list.append(",".join(gc_start_end_output_list))
    master_output_list_header.append(",".join(gc_start_end_output_list_header))

print("%s" %(master_output_list_header[0]))
print("%s" %("\n".join(master_output_list)))
