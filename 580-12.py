#python3
#works with netflow result file captured with 580-01.py
#if gap is over 1,000 , if std is over 1,000
#there is home router

# i = interface port number

import numpy, math

for i in range(1,49):
    #print ("i= ", i)

    f = open("netflow.txt", 'r')
    lines = f.readlines()
    f.close()

    length = len (lines)
    #print ("LEN= ", length)

    j = 0
    #j = line number

    port = []

    k = 0
    #k = list number of port

    for line in lines:
        j = j + 1

        if j > 11 and j < (length-1):
            data = line.split(",")
            #print ("J= ", j)

            interface = data[2]
            #print ("interafce= ", interface)
            inter = interface.split("/")
            #print (inter[0], inter[1], inter[2])

            if data[3] == "6\n" and inter[2] == str(i):
                #print (data[0], data[1], data[2], data[3])
                portno = int (data[1])
                #print ("port no type = ", type(portno))
                #print ("port no = ", portno)
                port.insert(k,portno)
                k = k + 1

    portlen = len(port)
    port.sort()

    if portlen > 0:
        max = port[portlen - 1]
        min = port[0]
        avg = math.ceil( numpy.mean(port) )
        var = math.ceil( numpy.var(port) )
        std = math.ceil( numpy.std(port) )

        print ("### interface= G1/0/", i, "tcp port numbers= ", portlen, "gap= ", max-min, "max= ", max, "min =", min, "avg= ", avg, "var= ", var, "std= ", std, "tcp ports are= ", port)

