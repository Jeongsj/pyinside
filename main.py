import session
import comment
import article
from pprint import pprint

gall = 'lovelyz'
no = 971119
user = session.login('아이디', '비밀번호')


comment.write(user, gall, no, '댓글내용!!!!!!')
#comment.read(gall, no)
#article.write(user, gall, 'TEST', 'This is content!!!!!!!!!')
#article.read(gall, no)
#article.search(gall, "류수정 사랑행!!!!!!!!!!")

