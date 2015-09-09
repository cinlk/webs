#!/usr/bin/python3
from www import orm
import asyncio
from www.model import User

def test(loop):
	#yield from orm.create_pool(loop=loop,user='root',password='cloud',database='awesome')
	yield from orm.create_pool(loop=loop,user='root',password='cloud',database='awesome')
	u=User(name='test',email='test@test.com',passwd='test',image='about:blank',admin=True)
	yield from u.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
