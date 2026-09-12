"""Split input token estimates into capacity-bounded batches."""
from __future__ import annotations
def plan(lengths:list[int],max_items:int,max_tokens:int)->list[list[int]]:
 batches=[];current=[];tokens=0
 for index,length in enumerate(lengths):
  if length>max_tokens:raise ValueError('single item exceeds token capacity')
  if current and (len(current)>=max_items or tokens+length>max_tokens):batches.append(current);current=[];tokens=0
  current.append(index);tokens+=length
 if current:batches.append(current)
 return batches
if __name__=='__main__':
 import json,sys;p=json.load(sys.stdin);print(json.dumps(plan(p['lengths'],p['max_items'],p['max_tokens']),indent=2))
