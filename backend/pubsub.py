import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

subscribe_key = 'sub-c-529cf132-5946-11ec-931a-1addb9510060'
publish_key = 'pub-c-f975c365-bcc7-48d9-ac61-5bf6bdf9ea82'

pnconfig = PNConfiguration()
pnconfig.subscribe_key = subscribe_key
pnconfig.publish_key = publish_key
pubnub = PubNub(pnconfig)


CHANNELS = {
    'TEST': 'TEST',
    'BLOCK': 'BLOCK'
}

class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Channel: {message_object.channel} | Message: {message_object.message}')

pubnub.add_listener(Listener())

class PubSub():
    """
    Handles the publish/subscribe layer of the application.
    Provides communication between the nodes of the blockchain network.
    """
    def __init__(self):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(['TEST', 'BLOCK']).execute()
        self.pubnub.add_listener(Listener())

    def publish(self, channel, message):
        """
        Publish the message object to the channel.
        """
        self.pubnub.publish().channel(channel).message(message).sync()

    def broadcast_block(self, block):
        """
        Broadcast a block object to all nodes.
        """
        self.publish(CHANNELS['BLOCK'], block.to_json())

    def broadcast_transaction(self, transaction):
        """
        Broadcast a transaction to all nodes.
        """
        self.publish(CHANNELS['BLOCK'], transaction.to_json())


def main():
    pubsub = PubSub()
    time.sleep(1)
    pubsub.publish(CHANNELS['TEST'], {'foo' : 'bar'})

if __name__ == '__main__':
    main()