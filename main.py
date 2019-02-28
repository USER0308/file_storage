from fdfs_client.client import *

client = Fdfs_client('/etc/fdfs/client.conf')

conn = ConnectionPool(name='tracker',conn_class=Connection,host_tuple=('file.org.com',),port='22122',timeout=60)
tc = Tracker_client(conn)
store_serv = tc.tracker_query_storage_stor_without_group()

store = client.get_storage(store_serv)

conn_client = ConnectionPool(name='storage',conn_class=Connection,host_tuple=('file.org.com',),port='23000',timeout=30)
store_client = Storage_client('file.org.com','23000',30)
store_client.pool = conn_client
ret = store_client.storage_upload_by_filename(tc, store_serv, '/home/ubuntu/background.jpg', None)

print ret