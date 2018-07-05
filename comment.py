import protocol
from api import API

def read(gall_id, article_no, page=1):
    body = {
        'id': gall_id,
        'no': article_no,
        're_page': page
    }
    res = protocol.get(API['comment']['read'], body)
    return res.json()


def write(session, gall_id, article_no, memo, detail_idx=''):
    body = {
        'mode': 'comment',
        'id': gall_id,
        'no': article_no,
        'comment_memo': memo,
        'detail_idx': detail_idx
    }

    if(session['stype'] == 'C'):
        body['comment_nick'] = session['name']
        body['comment_pw'] = session['password']
        body['mode'] = 'comment_nonmember'
    else:
        body['user_id'] = session['user_id']
    
    res = protocol.post(API['comment']['write'], body)
    return res.json()
