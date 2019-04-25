#coding=utf-8

import sqlite3

def initdb(data):
    conn = sqlite3.connect("C:/Users/Administrator/Downloads/CQA-tuling/酷Q Air/app/moe.min.qa/qav2.db")
    statement = "INSERT INTO qa (priority,type,state,keyword,answer) VALUES(?,?,?,?,?)"
    conn.executemany(statement, data)
    sussess=conn.commit()
    curson = conn.execute("select * from qa")
    conn.commit()
    print (curson)
    rows = curson.fetchall()
    print (rows)
    conn.close()
    return sussess

def deledb(data):
    conn = sqlite3.connect("C:/Users/Administrator/Downloads/CQA-tuling/酷Q Air/app/moe.min.qa/qav2.db")
    statement = "DELETE FROM qa WHERE keyword = ? AND answer = ?"
    conn.executemany(statement, data)
    conn.commit()
    curson = conn.execute("select * from qa")
    conn.commit()
    print (curson)
    conn.close()
