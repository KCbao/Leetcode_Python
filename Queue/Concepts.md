## Definition: Queue is a linear data structure which follows FIFO order in which operations performed. 
- customer comes first getting served first

## Stack versus Queue
- Difference lies in removing
- Stack: FIFO / FILO
- Queue: FIFO

## Applcations of queue
- when a resource is shared with multiple users. e.g., CPU scheduling (调度)， Disk scheduling
- when data is transferred asynchronouly b/t two processers (发出的同时没有立马收到) e.g., I/O buffers (a mechanism for temporarily holding data until it's ready to be used)

## Operations in queue
- enqueue: add an item. If full, then overflow
- dequeue: remove an item. If empty, then underflow
- front: get the front item
- rare: get the last item