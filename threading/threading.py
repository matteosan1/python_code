    import threading

    class MyThread ( threading.Thread ):

       def run ( self ):

          print 'Insert some thread stuff here.'
          print 'It'll be executed...yeah....'
          print 'There's not much to it.'

    import threading

    class MyThread ( threading.thread ):

       def run ( self ):

          print 'You called my start method, yeah.'
          print 'Were you expecting something amazing?'

    MyThread().start()

    import threading

    theVar = 1

    class MyThread ( threading.Thread ):

       def run ( self ):

          global theVar
          print 'This is thread ' + str ( theVar ) + ' speaking.'
          print 'Hello and good bye.'
          theVar = theVar + 1

    for x in xrange ( 20 ):
       MyThread().start()





    import pickle
    import socket
    import threading

    # We'll pickle a list of numbers:
    someList = [ 1, 2, 7, 9, 0 ]
    pickledList = pickle.dumps ( someList )

    # Our thread class:
    class ClientThread ( threading.Thread ):

       # Override Thread's __init__ method to accept the parameters needed:
       def __init__ ( self, channel, details ):

          self.channel = channel
          self.details = details
          threading.Thread.__init__ ( self )

       def run ( self ):

          print 'Received connection:', self.details [ 0 ]
          self.channel.send ( pickledList )
          for x in xrange ( 10 ):
             print self.channel.recv ( 1024 )
          self.channel.close()
          print 'Closed connection:', self.details [ 0 ]

    # Set up the server:
    server = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
    server.bind ( ( '', 2727 ) )
    server.listen ( 5 )

    # Have the server serve "forever":
    while True:
       channel, details = server.accept()
       ClientThread ( channel, details ).start()


    import pickle
    import socket

    # Connect to the server:
    client = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
    client.connect ( ( 'localhost', 2727 ) )

    # Retrieve and unpickle the list object:
    print pickle.loads ( client.recv ( 1024 ) )

    # Send some messages:
    for x in xrange ( 10 ):
       client.send ( 'Hey. ' + str ( x ) + '\n' )

    # Close the connection
    client.close()


    import pickle
    import socket
    import threading

    # Here's our thread:
    class ConnectionThread ( threading.Thread ):

       def run ( self ):

          # Connect to the server:
          client = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
          client.connect ( ( 'localhost', 2727 ) )

          # Retrieve and unpickle the list object:
          print pickle.loads ( client.recv ( 1024 ) )

          # Send some messages:
          for x in xrange ( 10 ):
             client.send ( 'Hey. ' + str ( x ) + '\n' )

          # Close the connection
          client.close()

    # Let's spawn a few threads:
    for x in xrange ( 5 ):
       ConnectionThread().start()

    import pickle
    import Queue
    import socket
    import threading

    # We'll pickle a list of numbers, yet again:
    someList = [ 1, 2, 7, 9, 0 ]
    pickledList = pickle.dumps ( someList )

    # A revised version of our thread class:
    class ClientThread ( threading.Thread ):

       # Note that we do not override Thread's __init__ method.
       # The Queue module makes this not necessary.

       def run ( self ):

          # Have our thread serve "forever":
          while True:

             # Get a client out of the queue
             client = clientPool.get()

             # Check if we actually have an actual client in the client variable:
             if client != None:

                print 'Received connection:', client [ 1 ] [ 0 ]
                client [ 0 ].send ( pickledList )
                for x in xrange ( 10 ):
                   print client [ 0 ].recv ( 1024 )
                client [ 0 ].close()
                print 'Closed connection:', client [ 1 ] [ 0 ]

    # Create our Queue:
    clientPool = Queue.Queue ( 0 )

    # Start two threads:
    for x in xrange ( 2 ):
       ClientThread().start()

    # Set up the server:
    server = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
    server.bind ( ( '', 2727 ) )
    server.listen ( 5 )

    # Have the server serve "forever":
    while True:
       clientPool.put ( server.accept() )


    import threading

    class TestThread ( threading.Thread ):

       def run ( self ):

          print 'Hello, my name is', self.getName()

    cazaril = TestThread()
    cazaril.setName ( 'Cazaril' )
    cazaril.start()

    ista = TestThread()
    ista.setName ( 'Ista' )
    ista.start()

    TestThread().start()

    import threading
    import time

    class TestThread ( threading.Thread ):

       def run ( self ):

          print 'Patient: Doctor, am I going to die?'

    class AnotherThread ( TestThread ):

       def run ( self ):

          TestThread.run( self )
          time.sleep ( 10 )

    dying = TestThread()
    dying.start()
    if dying.isAlive():
       print 'Doctor: No.'
    else:
       print 'Doctor: Next!'

    living = AnotherThread()
    living.start()
    if living.isAlive():
       print 'Doctor: No.'
    else:
       print 'Doctor: Next!'

    import threading
    import time

    class ThreadOne ( threading.Thread ):

       def run ( self ):

          print 'Thread', self.getName(), 'started.'
          time.sleep ( 5 )
          print 'Thread', self.getName(), 'ended.'

    class ThreadTwo ( threading.Thread ):

       def run ( self ):

          print 'Thread', self.getName(), 'started.'
          thingOne.join()
          print 'Thread', self.getName(), 'ended.'

    thingOne = ThreadOne()
    thingOne.start()
    thingTwo = ThreadTwo()
    thingTwo.start()

    import threading
    import time

    class DaemonThread ( threading.Thread ):

       def run ( self ):

          self.setDaemon ( True )
          time.sleep ( 10 )

    DaemonThread().start()
    print 'Leaving.'


    import thread

    def thread( stuff ):
       print "I'm a real boy!"
       print stuff

    thread.start_new_thread ( thread, ( 'Argument' ) )

