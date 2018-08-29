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

    messages = [rec['kinesis']['data'].encode('utf-8')
                for rec in event['Records']]

    conn.send(nsq.protocol.mpub(topic, messages))
