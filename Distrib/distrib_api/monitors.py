#coding:GBK
from etcd.client import etcd

def WriteToEtcd(host,dic):
    client = etcd.Client(
        host='192.168.3.13',
        port=4001,
    )
    client.write('/nodes/'+host,dic)


def monitor(host,dic):                      #monitor in client
    client = etcd.Client(
        host='192.168.3.13',
        port=4001,
    )
    while True:
        client.watch('/nodes/'+host,timeout=0)
        status = client.read('/nodes/'+host).value
        if eval(status)['status'] == 'unexecuted':
            print status
            pass
        elif eval(status)['status'] == 'executing':
            pass
        elif eval(status)['status'] == 'executed':
            pass
        elif eval(status)['status'] == 'failed':
            pass
        else:
            break