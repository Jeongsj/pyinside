import protocol
from api import API


def read(gall_id, article_no):
    body = {
        'id': gall_id,
        'no': article_no
    }
    res = protocol.get(API['article']['read'], body)
    return res.json()

def detail(gall_id, article_no):
    body = {
        'id': gall_id,
        'no': article_no
    }
    res = protocol.get(API['article']['detail'], body)
    return res.json()

def images(gall_id, article_no):
    body = {
        'id': gall_id,
        'no': article_no
    }
    res = protocol.get(API['article']['images'], body)
    return res.json()

def write(session, gall_id, subject, memo):
    body = {
        'mode': 'write',
        'id': gall_id,
        'subject': subject,
    }

    if (type(memo) is str):
        body['memo_block[0]'] = memo
    else:
        print('memo type is not str!')

    if(session['stype'] == 'C'):
        body['comment_nick'] = session['name']
        body['comment_pw'] = session['password']
    else:
        body['user_id'] = session['user_id']

    res = protocol.post(API['article']['write'], body)
    return res.json()

def search(gall_id, context, page=1):
    body = {
        'id': gall_id,
        'page': page,
        's_type': 'memo',
        'serVal': context
    }
    res = protocol.get(API['article']['search'], body)
    return res.json()
