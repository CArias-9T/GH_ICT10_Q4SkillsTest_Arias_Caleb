from pyscript import display, document
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)
import matplotlib.pyplot as plt

plt.figure()
plt.plot([0, 1],[0, 1])
plt.close()

def graph(e):
    document.getElementById('output').innerHTML = ' ' # resets value

    absences = np.array([ # input absences
        int(document.getElementById('absence').value), 
])
    months = np.array([ # input months
        str(document.getElementById('monthselect').value)
])

    topaz_absences_graph = plt.bar(months, absences) # display graph
    plt.show(topaz_absences_graph)
    plt.title("Topaz's Absence's Per Month")
    plt.xlabel("Months")
    plt.ylabel("Absences")
    