import MySQLdb
import os

def callDelugeDownlaodOne(item):
    cmdline='deluge-console "connect localhost deluge deluge; add ' + item[2] + '"'
    print cmdline
    os.system(cmdline)

def main():
    try:
        conn = MySQLdb.connect(host='localhost', user='root', passwd='root', db='btlinks')
        cursor = conn.cursor()
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])

    try:
        sqlstring = "select * from newlinks order by id ASC limit 1;"
        cursor.execute(sqlstring)
        item = cursor.fetchone()

        if not "HDCAM".lower() in item[1].lower() or \
           not  "-TS"  in item[1]:
            callDelugeDownlaodOne(item)

        #write this item to downloadedlinks
        sqlstring = "INSERT INTO `downloadedlinks` (`btName`, `bt_link_content`) VALUES ('%s', '%s')"% (item[1], item[2])

        cursor.execute(sqlstring)
        conn.commit()

        #delete thit item at newlinks table
        sqlstring = "delete from `newlinks` where id=%s "% str(item[0])
        cursor.execute(sqlstring)
        conn.commit()
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])

    cursor.close()
    conn.close()

if __name__ == "__main__":
    import commands
    ret = commands.getoutput("ls /var/lib/deluge/Downloads/ | wc -l")
    if int(ret) < 8:
        for i in range(0,8):
            main()
