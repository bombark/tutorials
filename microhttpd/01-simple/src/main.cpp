/*================================  HEADER  ==================================*/

#include <microhttpd.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <dlfcn.h>
#include <iostream>

typedef std::string String;
using namespace std;

/*----------------------------------------------------------------------------*/



/*===============================  HttpTask  =================================*/


struct HttpTask {
	String url;
	struct MHD_Connection* conn;
	struct MHD_PostProcessor* postprocessor;

	HttpTask(struct MHD_Connection* conn, String url){
		this->url = url;
		printf("[REQUEST]: %s\n", url.c_str());
		this->conn = conn;
		postprocessor = NULL;
	}

	~HttpTask(){
		if ( postprocessor ){
			MHD_destroy_post_processor (postprocessor);
			postprocessor = NULL;
		}
	}

	void initPost(){
		this->postprocessor = MHD_create_post_processor (this->conn, 4096, &callback_post, (void*)this);
	}

	void loadPost(const char* data, size_t size){
		MHD_post_process (this->postprocessor, data, size);
	}

	void initloadGet(){
		// MHD_RESPONSE_HEADER_KIND, MHD_HEADER_KIND
		// MHD_COOKIE_KIND, MHD_POSTDATA_KIND, MHD_GET_ARGUMENT_KIND
		// MHD_GET_ARGUMENT_KIND, MHD_FOOTER_KIND
		MHD_get_connection_values (this->conn, MHD_GET_ARGUMENT_KIND, &callback_get, (void*)this);
	}

	int send_answer(int code, String msg){
		struct MHD_Response* response = MHD_create_response_from_buffer (
			msg.size(), (char*)msg.c_str(), MHD_RESPMEM_MUST_COPY
		);
		int ret = MHD_queue_response(conn, MHD_HTTP_OK, response);
		MHD_destroy_response(response);
		return ret;
	}

  private:
	static int callback_get (void *cls, enum MHD_ValueKind kind, const char *key, const char *value){
		HttpTask* self = (HttpTask*) cls;
		printf ("   [params-get]: %s=%s\n", key, value);
		return MHD_YES;
	}

	static int callback_post (
		void *cls, enum MHD_ValueKind kind, const char *key,
		const char *filename, const char *content_type,
		const char *transfer_encoding, const char *data,
		uint64_t off, size_t size
	) {
		HttpTask* self = (HttpTask*) cls;
		printf("   [params-post] %s\n", key);
		return MHD_YES;
	}
};

/*----------------------------------------------------------------------------*/



/*==============================  HttpTasker  ================================*/

struct HttpServer {
	int port;
	struct MHD_Daemon* daemon;

	HttpServer(int port=8080){
		this->port = port;
		this->daemon = MHD_start_daemon(
			MHD_USE_THREAD_PER_CONNECTION, //MHD_USE_SELECT_INTERNALLY
			port, NULL, NULL,
			&callback_conn_start, this,
			MHD_OPTION_CONNECTION_TIMEOUT, (unsigned int) 15,
			MHD_OPTION_NOTIFY_COMPLETED, NULL, NULL,
			MHD_OPTION_END
		);
		printf("[log]: boot server in port %d\n", port);
	}

	~HttpServer(){
		if ( this->daemon )
			MHD_stop_daemon(this->daemon);
	}


  private:
	static int callback_conn_start(
		void* cls,
		struct MHD_Connection* conn,
		const char* url,
		const char* method,
		const char* version,
		const char* upload_data,
		size_t* ptr_upload_data_size,
		void** conn_cls
	) {

		HttpServer* self = (HttpServer*) cls;
		if ( self == NULL ) {
			return MHD_NO;
		}

		// First time
		HttpTask* task = (HttpTask*) *conn_cls;
		if ( task == NULL ) {
			task = new HttpTask(conn, url);
			if ( strcmp (method, "POST") == 0 ){
				task->initPost();
			}
			*conn_cls = task;
			return MHD_YES;
		}

		// Second time
		size_t upload_data_size = *ptr_upload_data_size;
		if ( strcmp (method, "POST") == 0 ) {
			if ( upload_data_size != 0) {
				task->loadPost(upload_data, upload_data_size);
				*ptr_upload_data_size = 0;
				return MHD_YES;
			}
		} else if ( strcmp(method, "GET") == 0 ){
			task->initloadGet();
		} else {
			return MHD_NO;
		}

		int res_code = task->send_answer(MHD_HTTP_OK,"Hello World");
		delete(task);
		return res_code;
	}

};

/*----------------------------------------------------------------------------*/



/*=================================  MAIN  ===================================*/

int main(int argc,char ** argv) {
	HttpServer server(8080);
	while ( true ){
		sleep(1);
	}

	return 0;
}

/*----------------------------------------------------------------------------*/
