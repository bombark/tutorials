# Microhttpd Example

- function main: creates a HttpServer and after only waits.

- class HttpServer: the server is executing on other thread and waits for new
	requisitions. The requisitions are called of tasks and for each task, the
	function callback_conn_start is executed;

- class HttpTask: the task has the connection and obtain the GET or POST
	parameters; 


# Compile

```
mkdir build; cd build
cmake ..
make
```

## Requisitos

```
sudo apt install libmicrohttpd-dev
```
