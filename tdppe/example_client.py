from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor
import sys

class ExampleClient(LineReceiver):
    end="Bye-bye!"
    def connectionMade(self):
        self.sendLine("Hello, world!")
        self.sendLine("What a fine day it is.")
        self.sendLine(self.end)

    def lineReceived(self, line):
        print "receive:", line
        if line==self.end:
            self.transport.loseConnection()

class ExampleFactory(ClientFactory):
    protocol = ExampleClient

    def clientConnectionFailed(self, connector, reason):
        print 'connection failed:', reason.getErrorMessage()
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print 'connection lost:', reason.getErrorMessage()
        reactor.stop()

def main():
    factory = EchoClientFactory()
    reactor.connectTCP('localhost', 8000, factory)
    reactor.run()

if __name__ == '__main__':
    main()
