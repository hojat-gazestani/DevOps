# Slowstart

* slowstart <start_time_in_ms>
* indicates after __how long__ a server which has just come back up will run at __full speed__. 
*  The slowstart __never__ applies when __haproxy starts__
* It only __applies__ when a server has been previously __seen as failed__.

![spike](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/01-concept/05-spikeStreesTest.png)

* application receives a __sudden__ and __extreme increase__ or __decrease in load__.

