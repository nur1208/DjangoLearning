# mport redis

from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import (
    DeleteRowsEvent,
    UpdateRowsEvent,
    WriteRowsEvent,
)
import time
MYSQL_SETTINGS = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "passwd": "password"
}


def main():
    # r = redis.Redis()

    length = 0
    while True:

        stream = BinLogStreamReader(
            connection_settings=MYSQL_SETTINGS,
            only_events=[DeleteRowsEvent, WriteRowsEvent, UpdateRowsEvent],
            server_id=1)


        if(length != 100):
            # length = len(stream)
            for binlogevent in stream:
                prefix = "%s:%s:" % (binlogevent.schema, binlogevent.table)

                print(binlogevent)
                print(prefix)
                for row in binlogevent.rows:
                    time.sleep(10)
                    print(row)    
                    if isinstance(binlogevent, DeleteRowsEvent):
                        vals = row["values"]
                        print("delete")
                        print(vals)
                        print(row)
                        # r.delete(prefix + str(vals["id"]))
                    elif isinstance(binlogevent, UpdateRowsEvent):
                        print("update")
                        vals = row["after_values"]
                        print(row)
                        # r.hmset(prefix + str(vals["id"]), vals)
                    elif isinstance(binlogevent, WriteRowsEvent):
                        print("write")
                        vals = row["values"]
                        print(row)
                        # r.hmset(prefix + str(vals["id"]), vals)
        
        stream.close()


if __name__ == "__main__":
    main()