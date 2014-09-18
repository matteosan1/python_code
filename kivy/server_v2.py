#!/usr/bin/env python
#
#  threads_and_kivy.py
#  
'''threads_and_kivy.py
Trying to build up a foundation that satisfies the following:
    - has a thread that will implement code that:
        - simulates reads data from a Python socket
        - works on the data
        - puts the data onto a Python Queue
    - has a Kivy mainthread that:
        - via class ShowGUI
            - reads data from the Queue
            - updates a class variable of type StringProperty so it will
                update the label_text property.

'''

from threading import Thread
from Queue import Queue, Empty
import time


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.clock import Clock


kv='''

<ShowGUI>:
    Label:
        text: str(root.label_text)
'''

Builder.load_string(kv)

q = Queue()    


class SimSocket():
    global q

    def __init__(self, queue):
        self.q = queue

    def put_on_queue(self):
        print("<-----..threaded..SimSocket.put_on_queue(): entry")
        for i in range(10):
            print(".....threaded.....SimSocket.put_on_queue(): Loop " + str(i))
            time.sleep(1)#just here to sim occassional data send
            self.some_data = ["SimSocket.put_on_queue(): Data Loop " + str(i)]
            self.q.put(self.some_data)
        print("..threaded..SimSocket.put_on_queue(): thread ends")

class ShowGUI(BoxLayout):
    label_text = StringProperty("Initial - not data")
    global q

    def __init__(self):
        super(ShowGUI, self).__init__()
        print("ShowGUI.__init__() entry")
        Clock.schedule_interval(self.get_from_queue, 1.0)

    def get_from_queue(self, dt):
        print("---------> ShowGUI.get_from_queue() entry")
        try:
            queue_data = q.get(timeout = 5)
            self.label_text = queue_data[0]
            for qd in queue_data:
                print("SimKivy.get_from_queue(): got data from queue: " + qd)
        except Empty:
            print("Error - no data received on queue.")
            print("Unschedule Clock's schedule")
            Clock.unschedule(self.get_from_queue)


class KivyGui(App):
    def build(self):
        return ShowGUI()



def main():

    global q
    ss = SimSocket(q)

    simSocket_thread = Thread(name="simSocket",target=ss.put_on_queue)
    simSocket_thread.start()

    print("Starting KivyGui().run()")

    KivyGui().run()
    return 0

if __name__ == '__main__':
    main()
