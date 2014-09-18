from twisted.protocols.policies import LimitTotalConnectionsFactory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor, task

class Chat(LineReceiver):
    def __init__(self, users):
        self.users = users
        self.name = None
        self.state = "GETNAME"

        def connectionMade(self):
            self.sendLine("What's your name ?")
            
        def connectionLost(self):
            if self.users.has_key(self.name):
                del self.users[self.name]

        def lineReceived(self, line):
            if self.state == "GETNAME":
                self.handle_GETNAME(line)
            else:
                self.handle_CHAT(line)

        def handle_GETNAME(self, name):
            if self.users.has_key(name):
                self.sendLine("Name taken, please choose another.")
                return
            self.sendLine("Welcome, %s!" %(name,))
            self.name = name
            self.users[name] = self
            self.state = "CHAT"

        def handle_CHAT(self, message):
            message = "<%s> %s" % (self.name, message)
            for name, protocol in self.users.iteritems():
                if protocol != self:
                    protocol.sendLine(message)

class ChatFactory(LimitTotalConnectionsFactory):
    protocol = ChatProtocol
    # aggiungere logging info

    def __init__(self):
        self.users = {}
        self.connectionLimit = 17
        self.overflowProtocolo = None
        self.lc = task.LoopingCall(self.carriera)
        self.lc.start(3600)
        
    def carriera(self):
        print "Avanti carriera."
        pass

    def buildProtocolo(self, addr):
        return Chat(self.users)

reactor.listenTCP(8123, ChatFactory())
reactor.run()

