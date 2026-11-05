import sqlite3
from .common import number,integer,identifier
def run(d):
 rows=d['rows'];updates=d['updates']
 if len(rows)+len(updates)>1000:raise ValueError('rows')
 with sqlite3.connect(':memory:')as c:
  c.executescript('create table stock(id integer primary key,qty integer check(qty>=0));create table audit(id,old_qty,new_qty);create trigger log after update of qty on stock begin insert into audit values(new.id,old.qty,new.qty);end;')
  c.executemany('insert into stock values(?,?)',[(integer(r['id']),integer(r['qty'],0))for r in rows]);c.commit();start=c.total_changes
  c.execute('savepoint trial');events=[];failed=False
  for u in updates:
   try:
    before=c.total_changes;cur=c.execute('update stock set qty=? where id=?',(integer(u['qty']),integer(u['id'])))
    events.append(dict(id=u['id'],direct_rows=cur.rowcount,total_change_delta=c.total_changes-before))
   except sqlite3.IntegrityError:failed=True;break
  attempted=c.total_changes-start
  if failed:c.execute('rollback to trial')
  c.execute('release trial')
  return dict(rolled_back=failed,attempted_change_counter=attempted,events=events,stock=list(c.execute('select *from stock order by id')),audit=list(c.execute('select *from audit order by rowid')))
