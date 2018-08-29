import envparse
import nsq
import nsq.protocol
import nsq.sync

env = envparse.Env(NSQ_TCP_ADDRESS=str, NSQ_TOPIC=str)


def lambda_handler(event, _):
    host, port = env.str('NSQ_TCP_ADDRESS').split(':')
    topic = env.str('NSQ_TOPIC')

    conn = nsq.sync.SyncConn()
    conn.connect(host, port)

    for event in event['Records']:
        msg = nsq.Message(
            event['eventID'],
            event['kinesis']['data'],
            event['kinesis']['approximateArrivalTimestamp'],
            0)

        conn.send(nsq.protocol.pub(topic, msg))
