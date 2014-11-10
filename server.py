## this code sets up a simple python server that awaits instructions from
## our Node.js server using Zerorpc

import zerorpc

class rpc(object):
    print "Python server ENGAGE!"

    # receives confirmation from Node server 
    def hello(self, name):
        print "Node greeting request received, response sending..."
        return "This is python. Hello, %s" % name    

    # passes simple data back to Node - takes array of numbers from Node, 
    # squares them, passes them back (for testing purposes only)    
    def processData(self, data):
        print "Node data request received, response sending..."
        return list(map((lambda x: x ** 2), data))

server = zerorpc.Server(rpc())
server.bind("tcp://0.0.0.0:4242")
server.run()