class Provider:
    
    def __init__(self):
        self.msg_queue = []
        self.subscribers = {}
    
    def notify(self, msg):
        self.msg_queue.append(msg)
    
    def subscribe(self, msg, subscriber):
        self.subscribers.setdefault(msg, []).append(subscriber)
    
    def unsubscribe(self, msg, subscriber):
        self.subscribers[msg].remove(subscriber)
        
    def update(self):
        
        for msg in self.msg_queue:
            for sub in self.subscribers.get(msg, []):
                sub.run(msg)
        self.msg_queue = []
        

class Publisher:
    
    def __init__(self, msg_center):
        self.provider = msg_center
    
    def publish(self, msg):
        self.provider.notify(msg)

class Subscriber:
    
    def __init__(self, name, msg_center):
        self.name = name
        self.provider = msg_center
    
    def subscribe(self, msg):
        self.provider.subscribe(msg, self)

    def unsubscribe(self, msg):
        self.provider.unsubscribe(msg, self) 
    
    def run(self, msg):
        print(f'{self.name} got {msg}')
               
msg_center = Provider()

pub = Publisher(msg_center)
pub.publish('cartoon')
pub.publish('movies')
pub.publish('music')
pub.publish('video')

jim = Subscriber('jim', msg_center)
jack = Subscriber('jack', msg_center)
vani = Subscriber('vani', msg_center)

jim.subscribe('cartoon')
jack.subscribe('music')
vani.subscribe('movies')

msg_center.update()

vani.unsubscribe('movies')

msg_center.update()
