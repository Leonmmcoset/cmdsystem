# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

class HTTPChannel(TypedReferenceCount):
    """
    /**
     * A single channel of communication from an HTTPClient.  This is similar to
     * the concept of a 'connection', except that HTTP is technically
     * connectionless; in fact, a channel may represent one unbroken connection or
     * it may transparently close and reopen a new connection with each request.
     *
     * A channel is conceptually a single thread of I/O. One document at a time
     * may be requested using a channel; a new document may (in general) not be
     * requested from the same HTTPChannel until the first document has been fully
     * retrieved.
     */
    """
    def beginConnectTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        begin_connect_to(const HTTPChannel self, const DocumentSpec url)
        
        /**
         * Begins a non-blocking request to establish a direct connection to the
         * server and port indicated by the URL.  No HTTP requests will be issued
         * beyond what is necessary to establish the connection.  When run() has
         * finished, you may call is_connection_ready() to determine if the connection
         * was successfully established.
         *
         * If successful, the connection may then be taken to use for whatever
         * purposes you like by calling get_connection().
         *
         * This establishes a nonblocking I/O socket.  Also see connect_to().
         */
        """
        pass

    def beginGetDocument(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        begin_get_document(const HTTPChannel self, const DocumentSpec url)
        
        /**
         * Begins a non-blocking request to retrieve a given document.  This method
         * will return immediately, even before a connection to the server has
         * necessarily been established; you must then call run() from time to time
         * until the return value of run() is false.  Then you may check is_valid()
         * and get_status_code() to determine the status of your request.
         *
         * If a previous request had been pending, that request is discarded.
         */
        """
        pass

    def beginGetHeader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        begin_get_header(const HTTPChannel self, const DocumentSpec url)
        
        /**
         * Begins a non-blocking request to retrieve a given header.  See
         * begin_get_document() and get_header().
         */
        """
        pass

    def beginGetSubdocument(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        begin_get_subdocument(const HTTPChannel self, const DocumentSpec url, int first_byte, int last_byte)
        
        /**
         * Begins a non-blocking request to retrieve only the specified byte range of
         * the indicated document.  If last_byte is 0, it stands for the last byte of
         * the document.  When a subdocument is requested, get_file_size() and
         * get_bytes_downloaded() will report the number of bytes of the subdocument,
         * not of the complete document.
         */
        """
        pass

    def beginPostForm(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        begin_post_form(const HTTPChannel self, const DocumentSpec url, str body)
        
        /**
         * Posts form data to a particular URL and retrieves the response, all using
         * non-blocking I/O.  See begin_get_document() and post_form().
         *
         * It is important to note that you *must* call run() repeatedly after calling
         * this method until run() returns false, and you may not call any other
         * document posting or retrieving methods using the HTTPChannel object in the
         * interim, or your form data may not get posted.
         */
        """
        pass

    def begin_connect_to(self, const_HTTPChannel_self, const_DocumentSpec_url): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        begin_connect_to(const HTTPChannel self, const DocumentSpec url)
        
        /**
         * Begins a non-blocking request to establish a direct connection to the
         * server and port indicated by the URL.  No HTTP requests will be issued
         * beyond what is necessary to establish the connection.  When run() has
         * finished, you may call is_connection_ready() to determine if the connection
         * was successfully established.
         *
         * If successful, the connection may then be taken to use for whatever
         * purposes you like by calling get_connection().
         *
         * This establishes a nonblocking I/O socket.  Also see connect_to().
         */
        """
        pass

    def begin_get_document(self, const_HTTPChannel_self, const_DocumentSpec_url): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        begin_get_document(const HTTPChannel self, const DocumentSpec url)
        
        /**
         * Begins a non-blocking request to retrieve a given document.  This method
         * will return immediately, even before a connection to the server has
         * necessarily been established; you must then call run() from time to time
         * until the return value of run() is false.  Then you may check is_valid()
         * and get_status_code() to determine the status of your request.
         *
         * If a previous request had been pending, that request is discarded.
         */
        """
        pass

    def begin_get_header(self, const_HTTPChannel_self, const_DocumentSpec_url): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        begin_get_header(const HTTPChannel self, const DocumentSpec url)
        
        /**
         * Begins a non-blocking request to retrieve a given header.  See
         * begin_get_document() and get_header().
         */
        """
        pass

    def begin_get_subdocument(self, const_HTTPChannel_self, const_DocumentSpec_url, int_first_byte, int_last_byte): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        begin_get_subdocument(const HTTPChannel self, const DocumentSpec url, int first_byte, int last_byte)
        
        /**
         * Begins a non-blocking request to retrieve only the specified byte range of
         * the indicated document.  If last_byte is 0, it stands for the last byte of
         * the document.  When a subdocument is requested, get_file_size() and
         * get_bytes_downloaded() will report the number of bytes of the subdocument,
         * not of the complete document.
         */
        """
        pass

    def begin_post_form(self, const_HTTPChannel_self, const_DocumentSpec_url, str_body): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        begin_post_form(const HTTPChannel self, const DocumentSpec url, str body)
        
        /**
         * Posts form data to a particular URL and retrieves the response, all using
         * non-blocking I/O.  See begin_get_document() and post_form().
         *
         * It is important to note that you *must* call run() repeatedly after calling
         * this method until run() returns false, and you may not call any other
         * document posting or retrieving methods using the HTTPChannel object in the
         * interim, or your form data may not get posted.
         */
        """
        pass

    def clearExtraHeaders(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_extra_headers(const HTTPChannel self)
        
        /**
         * Resets the extra headers that were previously added via calls to
         * send_extra_header().
         */
        """
        pass

    def clear_extra_headers(self, const_HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_extra_headers(const HTTPChannel self)
        
        /**
         * Resets the extra headers that were previously added via calls to
         * send_extra_header().
         */
        """
        pass

    def closeReadBody(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        close_read_body(HTTPChannel self, istream stream)
        
        /**
         * Closes a file opened by a previous call to open_read_body().  This really
         * just deletes the istream pointer, but it is recommended to use this
         * interface instead of deleting it explicitly, to help work around compiler
         * issues.
         */
        """
        pass

    def close_read_body(self, HTTPChannel_self, istream_stream): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        close_read_body(HTTPChannel self, istream stream)
        
        /**
         * Closes a file opened by a previous call to open_read_body().  This really
         * just deletes the istream pointer, but it is recommended to use this
         * interface instead of deleting it explicitly, to help work around compiler
         * issues.
         */
        """
        pass

    def connectTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        connect_to(const HTTPChannel self, const DocumentSpec url)
        
        /**
         * Establish a direct connection to the server and port indicated by the URL,
         * but do not issue any HTTP requests.  If successful, the connection may then
         * be taken to use for whatever purposes you like by calling get_connection().
         *
         * This establishes a blocking I/O socket.  Also see begin_connect_to().
         */
        """
        pass

    def connect_to(self, const_HTTPChannel_self, const_DocumentSpec_url): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        connect_to(const HTTPChannel self, const DocumentSpec url)
        
        /**
         * Establish a direct connection to the server and port indicated by the URL,
         * but do not issue any HTTP requests.  If successful, the connection may then
         * be taken to use for whatever purposes you like by calling get_connection().
         *
         * This establishes a blocking I/O socket.  Also see begin_connect_to().
         */
        """
        pass

    def deleteDocument(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        delete_document(const HTTPChannel self, const DocumentSpec url)
        
        /**
         * Requests the server to remove the indicated URL.
         */
        """
        pass

    def delete_document(self, const_HTTPChannel_self, const_DocumentSpec_url): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        delete_document(const HTTPChannel self, const DocumentSpec url)
        
        /**
         * Requests the server to remove the indicated URL.
         */
        """
        pass

    def downloadToFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        download_to_file(const HTTPChannel self, const Filename filename, bool subdocument_resumes)
        
        /**
         * Specifies the name of a file to download the resulting document to.  This
         * should be called immediately after get_document() or begin_get_document()
         * or related functions.
         *
         * In the case of the blocking I/O methods like get_document(), this function
         * will download the entire document to the file and return true if it was
         * successfully downloaded, false otherwise.
         *
         * In the case of non-blocking I/O methods like begin_get_document(), this
         * function simply indicates an intention to download to the indicated file.
         * It returns true if the file can be opened for writing, false otherwise, but
         * the contents will not be completely downloaded until run() has returned
         * false.  At this time, it is possible that a communications error will have
         * left a partial file, so is_download_complete() may be called to test this.
         *
         * If subdocument_resumes is true and the document in question was previously
         * requested as a subdocument (i.e.  get_subdocument() with a first_byte value
         * greater than zero), this will automatically seek to the appropriate byte
         * within the file for writing the output.  In this case, the file must
         * already exist and must have at least first_byte bytes in it.  If
         * subdocument_resumes is false, a subdocument will always be downloaded
         * beginning at the first byte of the file.
         */
        """
        pass

    def downloadToRam(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        download_to_ram(const HTTPChannel self, Ramfile ramfile, bool subdocument_resumes)
        
        /**
         * Specifies a Ramfile object to download the resulting document to.  This
         * should be called immediately after get_document() or begin_get_document()
         * or related functions.
         *
         * In the case of the blocking I/O methods like get_document(), this function
         * will download the entire document to the Ramfile and return true if it was
         * successfully downloaded, false otherwise.
         *
         * In the case of non-blocking I/O methods like begin_get_document(), this
         * function simply indicates an intention to download to the indicated
         * Ramfile.  It returns true if the file can be opened for writing, false
         * otherwise, but the contents will not be completely downloaded until run()
         * has returned false.  At this time, it is possible that a communications
         * error will have left a partial file, so is_download_complete() may be
         * called to test this.
         *
         * If subdocument_resumes is true and the document in question was previously
         * requested as a subdocument (i.e.  get_subdocument() with a first_byte value
         * greater than zero), this will automatically seek to the appropriate byte
         * within the Ramfile for writing the output.  In this case, the Ramfile must
         * already have at least first_byte bytes in it.
         */
        """
        pass

    def downloadToStream(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        download_to_stream(const HTTPChannel self, ostream strm, bool subdocument_resumes)
        
        /**
         * Specifies the name of an ostream to download the resulting document to.
         * This should be called immediately after get_document() or
         * begin_get_document() or related functions.
         *
         * In the case of the blocking I/O methods like get_document(), this function
         * will download the entire document to the file and return true if it was
         * successfully downloaded, false otherwise.
         *
         * In the case of non-blocking I/O methods like begin_get_document(), this
         * function simply indicates an intention to download to the indicated file.
         * It returns true if the file can be opened for writing, false otherwise, but
         * the contents will not be completely downloaded until run() has returned
         * false.  At this time, it is possible that a communications error will have
         * left a partial file, so is_download_complete() may be called to test this.
         *
         * If subdocument_resumes is true and the document in question was previously
         * requested as a subdocument (i.e.  get_subdocument() with a first_byte value
         * greater than zero), this will automatically seek to the appropriate byte
         * within the file for writing the output.  In this case, the file must
         * already exist and must have at least first_byte bytes in it.  If
         * subdocument_resumes is false, a subdocument will always be downloaded
         * beginning at the first byte of the file.
         */
        """
        pass

    def download_to_file(self, const_HTTPChannel_self, const_Filename_filename, bool_subdocument_resumes): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        download_to_file(const HTTPChannel self, const Filename filename, bool subdocument_resumes)
        
        /**
         * Specifies the name of a file to download the resulting document to.  This
         * should be called immediately after get_document() or begin_get_document()
         * or related functions.
         *
         * In the case of the blocking I/O methods like get_document(), this function
         * will download the entire document to the file and return true if it was
         * successfully downloaded, false otherwise.
         *
         * In the case of non-blocking I/O methods like begin_get_document(), this
         * function simply indicates an intention to download to the indicated file.
         * It returns true if the file can be opened for writing, false otherwise, but
         * the contents will not be completely downloaded until run() has returned
         * false.  At this time, it is possible that a communications error will have
         * left a partial file, so is_download_complete() may be called to test this.
         *
         * If subdocument_resumes is true and the document in question was previously
         * requested as a subdocument (i.e.  get_subdocument() with a first_byte value
         * greater than zero), this will automatically seek to the appropriate byte
         * within the file for writing the output.  In this case, the file must
         * already exist and must have at least first_byte bytes in it.  If
         * subdocument_resumes is false, a subdocument will always be downloaded
         * beginning at the first byte of the file.
         */
        """
        pass

    def download_to_ram(self, const_HTTPChannel_self, Ramfile_ramfile, bool_subdocument_resumes): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        download_to_ram(const HTTPChannel self, Ramfile ramfile, bool subdocument_resumes)
        
        /**
         * Specifies a Ramfile object to download the resulting document to.  This
         * should be called immediately after get_document() or begin_get_document()
         * or related functions.
         *
         * In the case of the blocking I/O methods like get_document(), this function
         * will download the entire document to the Ramfile and return true if it was
         * successfully downloaded, false otherwise.
         *
         * In the case of non-blocking I/O methods like begin_get_document(), this
         * function simply indicates an intention to download to the indicated
         * Ramfile.  It returns true if the file can be opened for writing, false
         * otherwise, but the contents will not be completely downloaded until run()
         * has returned false.  At this time, it is possible that a communications
         * error will have left a partial file, so is_download_complete() may be
         * called to test this.
         *
         * If subdocument_resumes is true and the document in question was previously
         * requested as a subdocument (i.e.  get_subdocument() with a first_byte value
         * greater than zero), this will automatically seek to the appropriate byte
         * within the Ramfile for writing the output.  In this case, the Ramfile must
         * already have at least first_byte bytes in it.
         */
        """
        pass

    def download_to_stream(self, const_HTTPChannel_self, ostream_strm, bool_subdocument_resumes): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        download_to_stream(const HTTPChannel self, ostream strm, bool subdocument_resumes)
        
        /**
         * Specifies the name of an ostream to download the resulting document to.
         * This should be called immediately after get_document() or
         * begin_get_document() or related functions.
         *
         * In the case of the blocking I/O methods like get_document(), this function
         * will download the entire document to the file and return true if it was
         * successfully downloaded, false otherwise.
         *
         * In the case of non-blocking I/O methods like begin_get_document(), this
         * function simply indicates an intention to download to the indicated file.
         * It returns true if the file can be opened for writing, false otherwise, but
         * the contents will not be completely downloaded until run() has returned
         * false.  At this time, it is possible that a communications error will have
         * left a partial file, so is_download_complete() may be called to test this.
         *
         * If subdocument_resumes is true and the document in question was previously
         * requested as a subdocument (i.e.  get_subdocument() with a first_byte value
         * greater than zero), this will automatically seek to the appropriate byte
         * within the file for writing the output.  In this case, the file must
         * already exist and must have at least first_byte bytes in it.  If
         * subdocument_resumes is false, a subdocument will always be downloaded
         * beginning at the first byte of the file.
         */
        """
        pass

    def getAllowProxy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_allow_proxy(HTTPChannel self)
        
        /**
         * If this is true (the normal case), the HTTPClient will be consulted for
         * information about the proxy to be used for each connection via this
         * HTTPChannel.  If this has been set to false by the user, then all
         * connections will be made directly, regardless of the proxy settings
         * indicated on the HTTPClient.
         */
        """
        pass

    def getBlockingConnect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_blocking_connect(HTTPChannel self)
        
        /**
         * If this flag is true, a socket connect will block even for nonblocking I/O
         * calls like begin_get_document(), begin_connect_to(), etc.  If false, a
         * socket connect will not block for nonblocking I/O calls, but will block for
         * blocking I/O calls (get_document(), connect_to(), etc.).
         */
        """
        pass

    def getBytesDownloaded(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bytes_downloaded(HTTPChannel self)
        
        /**
         * Returns the number of bytes downloaded during the last (or current)
         * download_to_file() or download_to_ram operation().  This can be used in
         * conjunction with get_file_size() to report the percent complete (but be
         * careful, since get_file_size() may return 0 if the server has not told us
         * the size of the file).
         */
        """
        pass

    def getBytesRequested(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bytes_requested(HTTPChannel self)
        
        /**
         * When download throttling is in effect (set_download_throttle() has been set
         * to true) and non-blocking I/O methods (like begin_get_document()) are used,
         * this returns the number of bytes "requested" from the server so far: that
         * is, the theoretical maximum value for get_bytes_downloaded(), if the server
         * has been keeping up with our demand.
         *
         * If this number is less than get_bytes_downloaded(), then the server has not
         * been supplying bytes fast enough to meet our own download throttle rate.
         *
         * When download throttling is not in effect, or when the blocking I/O methods
         * (like get_document(), etc.) are used, this returns 0.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getClient(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_client(HTTPChannel self)
        
        /**
         * Returns the HTTPClient object that owns this channel.
         */
        """
        pass

    def getConnection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_connection(const HTTPChannel self)
        
        /**
         * Returns the connection that was established via a previous call to
         * connect_to() or begin_connect_to(), or NULL if the connection attempt
         * failed or if those methods have not recently been called.
         *
         * This stream has been allocated from the free store.  It is the user's
         * responsibility to delete this pointer when finished with it.
         */
        """
        pass

    def getConnectTimeout(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_connect_timeout(HTTPChannel self)
        
        /**
         * Returns the length of time, in seconds, to wait for a new nonblocking
         * socket to connect.  See set_connect_timeout().
         */
        """
        pass

    def getContentType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_content_type(HTTPChannel self)
        
        /**
         * Returns the value of the Content-Type header.
         */
        """
        pass

    def getDocument(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_document(const HTTPChannel self, const DocumentSpec url)
        
        /**
         * Opens the named document for reading, if available.  Returns true if
         * successful, false otherwise.
         */
        """
        pass

    def getDocumentSpec(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_document_spec(HTTPChannel self)
        
        /**
         * Returns the DocumentSpec associated with the most recent document.  This
         * includes its actual URL (following redirects) along with the identity tag
         * and last-modified date, if supplied by the server.
         *
         * This structure may be saved and used to retrieve the same version of the
         * document later, or to conditionally retrieve a newer version if it is
         * available.
         */
        """
        pass

    def getDownloadThrottle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_download_throttle(HTTPChannel self)
        
        /**
         * Returns whether the nonblocking downloads will be bandwidth-limited.  See
         * set_download_throttle().
         */
        """
        pass

    def getFileSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_file_size(HTTPChannel self)
        
        /**
         * Returns the size of the file, if it is known.  Returns the value set by
         * set_expected_file_size() if the file size is not known, or 0 if this value
         * was not set.
         *
         * If the file is dynamically generated, the size may not be available until a
         * read has started (e.g.  open_read_body() has been called); and even then it
         * may increase as more of the file is read due to the nature of HTTP/1.1
         * requests which can change their minds midstream about how much data they're
         * sending you.
         */
        """
        pass

    def getFirstByteDelivered(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_first_byte_delivered(HTTPChannel self)
        
        /**
         * Returns the first byte of the file (that will be) delivered by the server
         * in response to the current request.  Normally, this is the same as
         * get_first_byte_requested(), but some servers will ignore a subdocument
         * request and always return the whole file, in which case this value will be
         * 0, regardless of what was requested to get_subdocument().
         */
        """
        pass

    def getFirstByteRequested(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_first_byte_requested(HTTPChannel self)
        
        /**
         * Returns the first byte of the file requested by the request.  This will
         * normally be 0 to indicate that the file is being requested from the
         * beginning, but if the file was requested via a get_subdocument() call, this
         * will contain the first_byte parameter from that call.
         */
        """
        pass

    def getHeader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_header(const HTTPChannel self, const DocumentSpec url)
        
        /**
         * Like get_document(), except only the header associated with the document is
         * retrieved.  This may be used to test for existence of the document; it
         * might also return the size of the document (if the server gives us this
         * information).
         */
        """
        pass

    def getHeaderValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_header_value(HTTPChannel self, str key)
        
        /**
         * Returns the HTML header value associated with the indicated key, or empty
         * string if the key was not defined in the message returned by the server.
         */
        """
        pass

    def getHttpTimeout(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_http_timeout(HTTPChannel self)
        
        /**
         * Returns the length of time, in seconds, to wait for the HTTP server to
         * respond to our request.  See set_http_timeout().
         */
        """
        pass

    def getHttpVersion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_http_version(HTTPChannel self)
        
        /**
         * Returns the HTTP version number returned by the server, as one of the
         * HTTPClient enumerated types, e.g.  HTTPClient::HV_11.
         */
        """
        pass

    def getHttpVersionString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_http_version_string(HTTPChannel self)
        
        /**
         * Returns the HTTP version number returned by the server, formatted as a
         * string, e.g.  "HTTP/1.1".
         */
        """
        pass

    def getIdleTimeout(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_idle_timeout(HTTPChannel self)
        
        /**
         * Returns the amount of time, in seconds, in which an previously-established
         * connection is allowed to remain open and unused.  See set_idle_timeout().
         */
        """
        pass

    def getLastByteDelivered(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_last_byte_delivered(HTTPChannel self)
        
        /**
         * Returns the last byte of the file (that will be) delivered by the server in
         * response to the current request.  Normally, this is the same as
         * get_last_byte_requested(), but some servers will ignore a subdocument
         * request and always return the whole file, in which case this value will be
         * 0, regardless of what was requested to get_subdocument().
         */
        """
        pass

    def getLastByteRequested(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_last_byte_requested(HTTPChannel self)
        
        /**
         * Returns the last byte of the file requested by the request.  This will
         * normally be 0 to indicate that the file is being requested to its last
         * byte, but if the file was requested via a get_subdocument() call, this will
         * contain the last_byte parameter from that call.
         */
        """
        pass

    def getMaxBytesPerSecond(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_bytes_per_second(HTTPChannel self)
        
        /**
         * Returns the maximum number of bytes per second that may be consumed by this
         * channel when get_download_throttle() is true.
         */
        """
        pass

    def getMaxUpdatesPerSecond(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_updates_per_second(HTTPChannel self)
        
        /**
         * Returns the maximum number of times per second that run() will do anything
         * at all, when get_download_throttle() is true.
         */
        """
        pass

    def getNumRedirectSteps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_redirect_steps(HTTPChannel self)
        
        /**
         * If the document automatically followed one or more redirects, this will
         * return the number of redirects that were automatically followed.  Use
         * get_redirect_step() to retrieve each URL in sequence.
         */
        """
        pass

    def getOptions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_options(const HTTPChannel self, const DocumentSpec url)
        
        /**
         * Sends an OPTIONS message to the server, which should query the available
         * options, possibly in relation to a specified URL.
         */
        """
        pass

    def getPersistentConnection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_persistent_connection(HTTPChannel self)
        
        /**
         * Returns whether the HTTPChannel should try to keep the connection to the
         * server open and reuse that connection for multiple documents, or whether it
         * should close the connection and open a new one for each request.  See
         * set_persistent_connection().
         */
        """
        pass

    def getProxyRealm(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_proxy_realm(HTTPChannel self)
        
        /**
         * If the document failed to connect because of a 407 (Proxy authorization
         * required), this method will return the "realm" returned by the proxy.  This
         * string may be presented to the user to request an associated username and
         * password (which then should be stored in HTTPClient::set_username()).
         */
        """
        pass

    def getProxyTunnel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_proxy_tunnel(HTTPChannel self)
        
        /**
         * Returns true if connections always tunnel through a proxy, or false (the
         * normal case) if we allow the proxy to serve up documents.  See
         * set_proxy_tunnel().
         */
        """
        pass

    def getRedirect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_redirect(HTTPChannel self)
        
        /**
         * If the document failed with a redirect code (300 series), this will
         * generally contain the new URL the server wants us to try.  In many cases,
         * the client will automatically follow redirects; if these are successful the
         * client will return a successful code and get_redirect() will return empty,
         * but get_url() will return the new, redirected URL.
         */
        """
        pass

    def getRedirectStep(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_redirect_step(HTTPChannel self, int n)
        
        /**
         * Use in conjunction with get_num_redirect_steps() to extract the chain of
         * URL's that the channel was automatically redirected through to arrive at
         * the final document.
         */
        """
        pass

    def getRedirectSteps(self, *args, **kwargs): # real signature unknown
        pass

    def getSkipBodySize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_skip_body_size(HTTPChannel self)
        
        /**
         * Returns the maximum number of bytes in a received (but unwanted) body that
         * will be skipped past, in order to reset to a new request.  See
         * set_skip_body_size().
         */
        """
        pass

    def getStatusCode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_status_code(HTTPChannel self)
        
        /**
         * Returns the HTML return code from the document retrieval request.  This
         * will be in the 200 range if the document is successfully retrieved, or some
         * other value in the case of an error.
         *
         * Some proxy errors during an https-over-proxy request would return the same
         * status code as a different error that occurred on the host server.  To
         * differentiate these cases, status codes that are returned by the proxy
         * during the CONNECT phase (except code 407) are incremented by 1000.
         */
        """
        pass

    def getStatusString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_status_string(HTTPChannel self)
        
        /**
         * Returns the string as returned by the server describing the status code for
         * humans.  This may or may not be meaningful.
         */
        """
        pass

    def getSubdocument(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_subdocument(const HTTPChannel self, const DocumentSpec url, int first_byte, int last_byte)
        
        /**
         * Retrieves only the specified byte range of the indicated document.  If
         * last_byte is 0, it stands for the last byte of the document.  When a
         * subdocument is requested, get_file_size() and get_bytes_downloaded() will
         * report the number of bytes of the subdocument, not of the complete
         * document.
         */
        """
        pass

    def getTrace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_trace(const HTTPChannel self, const DocumentSpec url)
        
        /**
         * Sends a TRACE message to the server, which should return back the same
         * message as the server received it, allowing inspection of proxy hops, etc.
         */
        """
        pass

    def getUrl(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_url(HTTPChannel self)
        
        /**
         * Returns the URL that was used to retrieve the most recent document:
         * whatever URL was last passed to get_document() or get_header().  If a
         * redirect has transparently occurred, this will return the new, redirected
         * URL (the actual URL at which the document was located).
         */
        """
        pass

    def getWwwRealm(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_www_realm(HTTPChannel self)
        
        /**
         * If the document failed to connect because of a 401 (Authorization
         * required), this method will return the "realm" returned by the server in
         * which the requested document must be authenticated.  This string may be
         * presented to the user to request an associated username and password (which
         * then should be stored in HTTPClient::set_username()).
         */
        """
        pass

    def get_allow_proxy(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_allow_proxy(HTTPChannel self)
        
        /**
         * If this is true (the normal case), the HTTPClient will be consulted for
         * information about the proxy to be used for each connection via this
         * HTTPChannel.  If this has been set to false by the user, then all
         * connections will be made directly, regardless of the proxy settings
         * indicated on the HTTPClient.
         */
        """
        pass

    def get_blocking_connect(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_blocking_connect(HTTPChannel self)
        
        /**
         * If this flag is true, a socket connect will block even for nonblocking I/O
         * calls like begin_get_document(), begin_connect_to(), etc.  If false, a
         * socket connect will not block for nonblocking I/O calls, but will block for
         * blocking I/O calls (get_document(), connect_to(), etc.).
         */
        """
        pass

    def get_bytes_downloaded(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bytes_downloaded(HTTPChannel self)
        
        /**
         * Returns the number of bytes downloaded during the last (or current)
         * download_to_file() or download_to_ram operation().  This can be used in
         * conjunction with get_file_size() to report the percent complete (but be
         * careful, since get_file_size() may return 0 if the server has not told us
         * the size of the file).
         */
        """
        pass

    def get_bytes_requested(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bytes_requested(HTTPChannel self)
        
        /**
         * When download throttling is in effect (set_download_throttle() has been set
         * to true) and non-blocking I/O methods (like begin_get_document()) are used,
         * this returns the number of bytes "requested" from the server so far: that
         * is, the theoretical maximum value for get_bytes_downloaded(), if the server
         * has been keeping up with our demand.
         *
         * If this number is less than get_bytes_downloaded(), then the server has not
         * been supplying bytes fast enough to meet our own download throttle rate.
         *
         * When download throttling is not in effect, or when the blocking I/O methods
         * (like get_document(), etc.) are used, this returns 0.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_client(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_client(HTTPChannel self)
        
        /**
         * Returns the HTTPClient object that owns this channel.
         */
        """
        pass

    def get_connection(self, const_HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_connection(const HTTPChannel self)
        
        /**
         * Returns the connection that was established via a previous call to
         * connect_to() or begin_connect_to(), or NULL if the connection attempt
         * failed or if those methods have not recently been called.
         *
         * This stream has been allocated from the free store.  It is the user's
         * responsibility to delete this pointer when finished with it.
         */
        """
        pass

    def get_connect_timeout(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_connect_timeout(HTTPChannel self)
        
        /**
         * Returns the length of time, in seconds, to wait for a new nonblocking
         * socket to connect.  See set_connect_timeout().
         */
        """
        pass

    def get_content_type(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_content_type(HTTPChannel self)
        
        /**
         * Returns the value of the Content-Type header.
         */
        """
        pass

    def get_document(self, const_HTTPChannel_self, const_DocumentSpec_url): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_document(const HTTPChannel self, const DocumentSpec url)
        
        /**
         * Opens the named document for reading, if available.  Returns true if
         * successful, false otherwise.
         */
        """
        pass

    def get_document_spec(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_document_spec(HTTPChannel self)
        
        /**
         * Returns the DocumentSpec associated with the most recent document.  This
         * includes its actual URL (following redirects) along with the identity tag
         * and last-modified date, if supplied by the server.
         *
         * This structure may be saved and used to retrieve the same version of the
         * document later, or to conditionally retrieve a newer version if it is
         * available.
         */
        """
        pass

    def get_download_throttle(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_download_throttle(HTTPChannel self)
        
        /**
         * Returns whether the nonblocking downloads will be bandwidth-limited.  See
         * set_download_throttle().
         */
        """
        pass

    def get_file_size(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_file_size(HTTPChannel self)
        
        /**
         * Returns the size of the file, if it is known.  Returns the value set by
         * set_expected_file_size() if the file size is not known, or 0 if this value
         * was not set.
         *
         * If the file is dynamically generated, the size may not be available until a
         * read has started (e.g.  open_read_body() has been called); and even then it
         * may increase as more of the file is read due to the nature of HTTP/1.1
         * requests which can change their minds midstream about how much data they're
         * sending you.
         */
        """
        pass

    def get_first_byte_delivered(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_first_byte_delivered(HTTPChannel self)
        
        /**
         * Returns the first byte of the file (that will be) delivered by the server
         * in response to the current request.  Normally, this is the same as
         * get_first_byte_requested(), but some servers will ignore a subdocument
         * request and always return the whole file, in which case this value will be
         * 0, regardless of what was requested to get_subdocument().
         */
        """
        pass

    def get_first_byte_requested(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_first_byte_requested(HTTPChannel self)
        
        /**
         * Returns the first byte of the file requested by the request.  This will
         * normally be 0 to indicate that the file is being requested from the
         * beginning, but if the file was requested via a get_subdocument() call, this
         * will contain the first_byte parameter from that call.
         */
        """
        pass

    def get_header(self, const_HTTPChannel_self, const_DocumentSpec_url): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_header(const HTTPChannel self, const DocumentSpec url)
        
        /**
         * Like get_document(), except only the header associated with the document is
         * retrieved.  This may be used to test for existence of the document; it
         * might also return the size of the document (if the server gives us this
         * information).
         */
        """
        pass

    def get_header_value(self, HTTPChannel_self, str_key): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_header_value(HTTPChannel self, str key)
        
        /**
         * Returns the HTML header value associated with the indicated key, or empty
         * string if the key was not defined in the message returned by the server.
         */
        """
        pass

    def get_http_timeout(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_http_timeout(HTTPChannel self)
        
        /**
         * Returns the length of time, in seconds, to wait for the HTTP server to
         * respond to our request.  See set_http_timeout().
         */
        """
        pass

    def get_http_version(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_http_version(HTTPChannel self)
        
        /**
         * Returns the HTTP version number returned by the server, as one of the
         * HTTPClient enumerated types, e.g.  HTTPClient::HV_11.
         */
        """
        pass

    def get_http_version_string(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_http_version_string(HTTPChannel self)
        
        /**
         * Returns the HTTP version number returned by the server, formatted as a
         * string, e.g.  "HTTP/1.1".
         */
        """
        pass

    def get_idle_timeout(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_idle_timeout(HTTPChannel self)
        
        /**
         * Returns the amount of time, in seconds, in which an previously-established
         * connection is allowed to remain open and unused.  See set_idle_timeout().
         */
        """
        pass

    def get_last_byte_delivered(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_last_byte_delivered(HTTPChannel self)
        
        /**
         * Returns the last byte of the file (that will be) delivered by the server in
         * response to the current request.  Normally, this is the same as
         * get_last_byte_requested(), but some servers will ignore a subdocument
         * request and always return the whole file, in which case this value will be
         * 0, regardless of what was requested to get_subdocument().
         */
        """
        pass

    def get_last_byte_requested(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_last_byte_requested(HTTPChannel self)
        
        /**
         * Returns the last byte of the file requested by the request.  This will
         * normally be 0 to indicate that the file is being requested to its last
         * byte, but if the file was requested via a get_subdocument() call, this will
         * contain the last_byte parameter from that call.
         */
        """
        pass

    def get_max_bytes_per_second(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_bytes_per_second(HTTPChannel self)
        
        /**
         * Returns the maximum number of bytes per second that may be consumed by this
         * channel when get_download_throttle() is true.
         */
        """
        pass

    def get_max_updates_per_second(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_updates_per_second(HTTPChannel self)
        
        /**
         * Returns the maximum number of times per second that run() will do anything
         * at all, when get_download_throttle() is true.
         */
        """
        pass

    def get_num_redirect_steps(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_redirect_steps(HTTPChannel self)
        
        /**
         * If the document automatically followed one or more redirects, this will
         * return the number of redirects that were automatically followed.  Use
         * get_redirect_step() to retrieve each URL in sequence.
         */
        """
        pass

    def get_options(self, const_HTTPChannel_self, const_DocumentSpec_url): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_options(const HTTPChannel self, const DocumentSpec url)
        
        /**
         * Sends an OPTIONS message to the server, which should query the available
         * options, possibly in relation to a specified URL.
         */
        """
        pass

    def get_persistent_connection(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_persistent_connection(HTTPChannel self)
        
        /**
         * Returns whether the HTTPChannel should try to keep the connection to the
         * server open and reuse that connection for multiple documents, or whether it
         * should close the connection and open a new one for each request.  See
         * set_persistent_connection().
         */
        """
        pass

    def get_proxy_realm(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_proxy_realm(HTTPChannel self)
        
        /**
         * If the document failed to connect because of a 407 (Proxy authorization
         * required), this method will return the "realm" returned by the proxy.  This
         * string may be presented to the user to request an associated username and
         * password (which then should be stored in HTTPClient::set_username()).
         */
        """
        pass

    def get_proxy_tunnel(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_proxy_tunnel(HTTPChannel self)
        
        /**
         * Returns true if connections always tunnel through a proxy, or false (the
         * normal case) if we allow the proxy to serve up documents.  See
         * set_proxy_tunnel().
         */
        """
        pass

    def get_redirect(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_redirect(HTTPChannel self)
        
        /**
         * If the document failed with a redirect code (300 series), this will
         * generally contain the new URL the server wants us to try.  In many cases,
         * the client will automatically follow redirects; if these are successful the
         * client will return a successful code and get_redirect() will return empty,
         * but get_url() will return the new, redirected URL.
         */
        """
        pass

    def get_redirect_step(self, HTTPChannel_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_redirect_step(HTTPChannel self, int n)
        
        /**
         * Use in conjunction with get_num_redirect_steps() to extract the chain of
         * URL's that the channel was automatically redirected through to arrive at
         * the final document.
         */
        """
        pass

    def get_redirect_steps(self, *args, **kwargs): # real signature unknown
        pass

    def get_skip_body_size(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_skip_body_size(HTTPChannel self)
        
        /**
         * Returns the maximum number of bytes in a received (but unwanted) body that
         * will be skipped past, in order to reset to a new request.  See
         * set_skip_body_size().
         */
        """
        pass

    def get_status_code(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_status_code(HTTPChannel self)
        
        /**
         * Returns the HTML return code from the document retrieval request.  This
         * will be in the 200 range if the document is successfully retrieved, or some
         * other value in the case of an error.
         *
         * Some proxy errors during an https-over-proxy request would return the same
         * status code as a different error that occurred on the host server.  To
         * differentiate these cases, status codes that are returned by the proxy
         * during the CONNECT phase (except code 407) are incremented by 1000.
         */
        """
        pass

    def get_status_string(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_status_string(HTTPChannel self)
        
        /**
         * Returns the string as returned by the server describing the status code for
         * humans.  This may or may not be meaningful.
         */
        """
        pass

    def get_subdocument(self, const_HTTPChannel_self, const_DocumentSpec_url, int_first_byte, int_last_byte): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_subdocument(const HTTPChannel self, const DocumentSpec url, int first_byte, int last_byte)
        
        /**
         * Retrieves only the specified byte range of the indicated document.  If
         * last_byte is 0, it stands for the last byte of the document.  When a
         * subdocument is requested, get_file_size() and get_bytes_downloaded() will
         * report the number of bytes of the subdocument, not of the complete
         * document.
         */
        """
        pass

    def get_trace(self, const_HTTPChannel_self, const_DocumentSpec_url): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_trace(const HTTPChannel self, const DocumentSpec url)
        
        /**
         * Sends a TRACE message to the server, which should return back the same
         * message as the server received it, allowing inspection of proxy hops, etc.
         */
        """
        pass

    def get_url(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_url(HTTPChannel self)
        
        /**
         * Returns the URL that was used to retrieve the most recent document:
         * whatever URL was last passed to get_document() or get_header().  If a
         * redirect has transparently occurred, this will return the new, redirected
         * URL (the actual URL at which the document was located).
         */
        """
        pass

    def get_www_realm(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_www_realm(HTTPChannel self)
        
        /**
         * If the document failed to connect because of a 401 (Authorization
         * required), this method will return the "realm" returned by the server in
         * which the requested document must be authenticated.  This string may be
         * presented to the user to request an associated username and password (which
         * then should be stored in HTTPClient::set_username()).
         */
        """
        pass

    def isConnectionReady(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_connection_ready(HTTPChannel self)
        
        /**
         * Returns true if a connection has been established to the named server in a
         * previous call to connect_to() or begin_connect_to(), false otherwise.
         */
        """
        pass

    def isDownloadComplete(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_download_complete(HTTPChannel self)
        
        /**
         * Returns true when a download_to() or download_to_ram() has executed and the
         * file has been fully downloaded.  If this still returns false after
         * processing has completed, there was an error in transmission.
         *
         * Note that simply testing is_download_complete() does not prove that the
         * requested document was successfully retrieved--you might have just
         * downloaded the "404 not found" stub (for instance) that a server would
         * provide in response to some error condition.  You should also check
         * is_valid() to prove that the file you expected has been successfully
         * retrieved.
         */
        """
        pass

    def isFileSizeKnown(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_file_size_known(HTTPChannel self)
        
        /**
         * Returns true if the size of the file we are currently retrieving was told
         * us by the server and thus is reliably known, or false if the size reported
         * by get_file_size() represents an educated guess (possibly as set by
         * set_expected_file_size(), or as inferred from a chunked transfer encoding
         * in progress).
         */
        """
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_valid(HTTPChannel self)
        
        /**
         * Returns true if the last-requested document was successfully retrieved and
         * is ready to be read, false otherwise.
         */
        """
        pass

    def is_connection_ready(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_connection_ready(HTTPChannel self)
        
        /**
         * Returns true if a connection has been established to the named server in a
         * previous call to connect_to() or begin_connect_to(), false otherwise.
         */
        """
        pass

    def is_download_complete(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_download_complete(HTTPChannel self)
        
        /**
         * Returns true when a download_to() or download_to_ram() has executed and the
         * file has been fully downloaded.  If this still returns false after
         * processing has completed, there was an error in transmission.
         *
         * Note that simply testing is_download_complete() does not prove that the
         * requested document was successfully retrieved--you might have just
         * downloaded the "404 not found" stub (for instance) that a server would
         * provide in response to some error condition.  You should also check
         * is_valid() to prove that the file you expected has been successfully
         * retrieved.
         */
        """
        pass

    def is_file_size_known(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_file_size_known(HTTPChannel self)
        
        /**
         * Returns true if the size of the file we are currently retrieving was told
         * us by the server and thus is reliably known, or false if the size reported
         * by get_file_size() represents an educated guess (possibly as set by
         * set_expected_file_size(), or as inferred from a chunked transfer encoding
         * in progress).
         */
        """
        pass

    def is_valid(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_valid(HTTPChannel self)
        
        /**
         * Returns true if the last-requested document was successfully retrieved and
         * is ready to be read, false otherwise.
         */
        """
        pass

    def openReadBody(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        open_read_body(const HTTPChannel self)
        
        /**
         * Returns a newly-allocated istream suitable for reading the body of the
         * document.  This may only be called immediately after a call to
         * get_document() or post_form(), or after a call to run() has returned false.
         *
         * Note that, in nonblocking mode, the returned stream may report an early
         * EOF, even before the actual end of file.  When this happens, you should
         * call stream->is_closed() to determine whether you should attempt to read
         * some more later.
         *
         * The user is responsible for passing the returned istream to
         * close_read_body() later.
         */
        """
        pass

    def open_read_body(self, const_HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open_read_body(const HTTPChannel self)
        
        /**
         * Returns a newly-allocated istream suitable for reading the body of the
         * document.  This may only be called immediately after a call to
         * get_document() or post_form(), or after a call to run() has returned false.
         *
         * Note that, in nonblocking mode, the returned stream may report an early
         * EOF, even before the actual end of file.  When this happens, you should
         * call stream->is_closed() to determine whether you should attempt to read
         * some more later.
         *
         * The user is responsible for passing the returned istream to
         * close_read_body() later.
         */
        """
        pass

    def postForm(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        post_form(const HTTPChannel self, const DocumentSpec url, str body)
        
        /**
         * Posts form data to a particular URL and retrieves the response.
         */
        """
        pass

    def post_form(self, const_HTTPChannel_self, const_DocumentSpec_url, str_body): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        post_form(const HTTPChannel self, const DocumentSpec url, str body)
        
        /**
         * Posts form data to a particular URL and retrieves the response.
         */
        """
        pass

    def preserveStatus(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        preserve_status(const HTTPChannel self)
        
        /**
         * Preserves the previous status code (presumably a failure) from the previous
         * connection attempt.  If the subsequent connection attempt also fails, the
         * returned status code will be the better of the previous code and the
         * current code.
         *
         * This can be called to daisy-chain subsequent attempts to download the same
         * document from different servers.  After all servers have been attempted,
         * the final status code will reflect the attempt that most nearly succeeded.
         */
        """
        pass

    def preserve_status(self, const_HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        preserve_status(const HTTPChannel self)
        
        /**
         * Preserves the previous status code (presumably a failure) from the previous
         * connection attempt.  If the subsequent connection attempt also fails, the
         * returned status code will be the better of the previous code and the
         * current code.
         *
         * This can be called to daisy-chain subsequent attempts to download the same
         * document from different servers.  After all servers have been attempted,
         * the final status code will reflect the attempt that most nearly succeeded.
         */
        """
        pass

    def putDocument(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        put_document(const HTTPChannel self, const DocumentSpec url, str body)
        
        /**
         * Uploads the indicated body to the server to replace the indicated URL, if
         * the server allows this.
         */
        """
        pass

    def put_document(self, const_HTTPChannel_self, const_DocumentSpec_url, str_body): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        put_document(const HTTPChannel self, const DocumentSpec url, str body)
        
        /**
         * Uploads the indicated body to the server to replace the indicated URL, if
         * the server allows this.
         */
        """
        pass

    def reset(self, const_HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reset(const HTTPChannel self)
        
        /**
         * Stops whatever file transaction is currently in progress, closes the
         * connection, and resets to begin anew.  You shouldn't ever need to call
         * this, since the channel should be able to reset itself cleanly between
         * requests, but it is provided in case you are an especially nervous type.
         *
         * Don't call this after every request unless you set
         * set_persistent_connection() to false, since calling reset() rudely closes
         * the connection regardless of whether we have told the server we intend to
         * keep it open or not.
         */
        """
        pass

    def run(self, const_HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        run(const HTTPChannel self)
        
        /**
         * This must be called from time to time when non-blocking I/O is in use.  It
         * checks for data coming in on the socket and writes data out to the socket
         * when possible, and does whatever processing is required towards completing
         * the current task.
         *
         * The return value is true if the task is still pending (and run() will need
         * to be called again in the future), or false if the current task is
         * complete.
         */
        """
        pass

    def sendExtraHeader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        send_extra_header(const HTTPChannel self, str key, str value)
        
        /**
         * Specifies an additional key: value pair that is added into the header sent
         * to the server with the next request.  This is passed along with no
         * interpretation by the HTTPChannel code.  You may call this repeatedly to
         * append multiple headers.
         *
         * This is persistent for one request only; it must be set again for each new
         * request.
         */
        """
        pass

    def send_extra_header(self, const_HTTPChannel_self, str_key, str_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        send_extra_header(const HTTPChannel self, str key, str value)
        
        /**
         * Specifies an additional key: value pair that is added into the header sent
         * to the server with the next request.  This is passed along with no
         * interpretation by the HTTPChannel code.  You may call this repeatedly to
         * append multiple headers.
         *
         * This is persistent for one request only; it must be set again for each new
         * request.
         */
        """
        pass

    def setAllowProxy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_allow_proxy(const HTTPChannel self, bool allow_proxy)
        
        /**
         * If this is true (the normal case), the HTTPClient will be consulted for
         * information about the proxy to be used for each connection via this
         * HTTPChannel.  If this has been set to false by the user, then all
         * connections will be made directly, regardless of the proxy settings
         * indicated on the HTTPClient.
         */
        """
        pass

    def setBlockingConnect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_blocking_connect(const HTTPChannel self, bool blocking_connect)
        
        /**
         * If this flag is true, a socket connect will block even for nonblocking I/O
         * calls like begin_get_document(), begin_connect_to(), etc.  If false, a
         * socket connect will not block for nonblocking I/O calls, but will block for
         * blocking I/O calls (get_document(), connect_to(), etc.).
         *
         * Setting this true is useful when you want to use non-blocking I/O once you
         * have established the connection, but you don't want to bother with polling
         * for the initial connection.  It's also useful when you don't particularly
         * care about non-blocking I/O, but you need to respect timeouts like
         * connect_timeout and http_timeout.
         */
        """
        pass

    def setConnectTimeout(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_connect_timeout(const HTTPChannel self, double timeout_seconds)
        
        /**
         * Sets the maximum length of time, in seconds, that the channel will wait
         * before giving up on establishing a TCP connection.
         *
         * At present, this is used only for the nonblocking interfaces (e.g.
         * begin_get_document(), begin_connect_to()), but it is used whether
         * set_blocking_connect() is true or false.
         */
        """
        pass

    def setContentType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_content_type(const HTTPChannel self, str content_type)
        
        /**
         * Specifies the Content-Type header, useful for applications that require
         * different types of content, such as JSON.
         */
        """
        pass

    def setDownloadThrottle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_download_throttle(const HTTPChannel self, bool download_throttle)
        
        /**
         * Specifies whether nonblocking downloads (via download_to_file() or
         * download_to_ram()) will be limited so as not to use all available
         * bandwidth.
         *
         * If this is true, when a download has been started on this channel it will
         * be invoked no more frequently than get_max_updates_per_second(), and the
         * total bandwidth used by the download will be no more than
         * get_max_bytes_per_second().  If this is false, downloads will proceed as
         * fast as the server can send the data.
         *
         * This only has effect on the nonblocking I/O methods like
         * begin_get_document(), etc.  The blocking methods like get_document() always
         * use as much CPU and bandwidth as they can get.
         */
        """
        pass

    def setExpectedFileSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_expected_file_size(const HTTPChannel self, int file_size)
        
        /**
         * This may be called immediately after a call to get_document() or some
         * related function to specify the expected size of the document we are
         * retrieving, if we happen to know.  This is used as the return value to
         * get_file_size() only in the case that the server does not tell us the
         * actual file size.
         */
        """
        pass

    def setHttpTimeout(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_http_timeout(const HTTPChannel self, double timeout_seconds)
        
        /**
         * Sets the maximum length of time, in seconds, that the channel will wait for
         * the HTTP server to finish sending its response to our request.
         *
         * The timer starts counting after the TCP connection has been established
         * (see set_connect_timeout(), above) and the request has been sent.
         *
         * At present, this is used only for the nonblocking interfaces (e.g.
         * begin_get_document(), begin_connect_to()), but it is used whether
         * set_blocking_connect() is true or false.
         */
        """
        pass

    def setIdleTimeout(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_idle_timeout(const HTTPChannel self, double idle_timeout)
        
        /**
         * Specifies the amount of time, in seconds, in which a previously-established
         * connection is allowed to remain open and unused.  If a previous connection
         * has remained unused for at least this number of seconds, it will be closed
         * and a new connection will be opened; otherwise, the same connection will be
         * reused for the next request (for this particular HTTPChannel).
         */
        """
        pass

    def setMaxBytesPerSecond(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_bytes_per_second(const HTTPChannel self, double max_bytes_per_second)
        
        /**
         * When bandwidth throttling is in effect (see set_download_throttle()), this
         * specifies the maximum number of bytes per second that may be consumed by
         * this channel.
         */
        """
        pass

    def setMaxUpdatesPerSecond(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_updates_per_second(const HTTPChannel self, double max_updates_per_second)
        
        /**
         * When bandwidth throttling is in effect (see set_download_throttle()), this
         * specifies the maximum number of times per second that run() will attempt to
         * do any downloading at all.
         */
        """
        pass

    def setPersistentConnection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_persistent_connection(const HTTPChannel self, bool persistent_connection)
        
        /**
         * Indicates whether the HTTPChannel should try to keep the connection to the
         * server open and reuse that connection for multiple documents, or whether it
         * should close the connection and open a new one for each request.  Set this
         * true to keep the connections around when possible, false to recycle them.
         *
         * It makes most sense to set this false when the HTTPChannel will be used
         * only once to retrieve a single document, true when you will be using the
         * same HTTPChannel object to retrieve multiple documents.
         */
        """
        pass

    def setProxyTunnel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_proxy_tunnel(const HTTPChannel self, bool proxy_tunnel)
        
        /**
         * Normally, a proxy is itself asked for ordinary URL's, and the proxy decides
         * whether to hand the client a cached version of the document or to contact
         * the server for a fresh version.  The proxy may also modify the headers and
         * transfer encoding on the way.
         *
         * If this is set to true, then instead of asking for URL's from the proxy, we
         * will ask the proxy to open a connection to the server (for instance, on
         * port 80); if the proxy honors this request, then we contact the server
         * directly through this connection to retrieve the document.  If the proxy
         * does not honor the connect request, then the retrieve operation fails.
         *
         * SSL connections (e.g.  https), and connections through a Socks proxy, are
         * always tunneled, regardless of the setting of this flag.
         */
        """
        pass

    def setSkipBodySize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_skip_body_size(const HTTPChannel self, int skip_body_size)
        
        /**
         * Specifies the maximum number of bytes in a received (but unwanted) body
         * that will be skipped past, in order to reset to a new request.
         *
         * That is, if this HTTPChannel requests a file via get_document(), but does
         * not call download_to_ram(), download_to_file(), or open_read_body(), and
         * instead immediately requests a new file, then the HTTPChannel has a choice
         * whether to skip past the unwanted document, or to close the connection and
         * open a new one.  If the number of bytes to skip is more than this
         * threshold, the connection will be closed; otherwise, the data will simply
         * be read and discarded.
         */
        """
        pass

    def set_allow_proxy(self, const_HTTPChannel_self, bool_allow_proxy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_allow_proxy(const HTTPChannel self, bool allow_proxy)
        
        /**
         * If this is true (the normal case), the HTTPClient will be consulted for
         * information about the proxy to be used for each connection via this
         * HTTPChannel.  If this has been set to false by the user, then all
         * connections will be made directly, regardless of the proxy settings
         * indicated on the HTTPClient.
         */
        """
        pass

    def set_blocking_connect(self, const_HTTPChannel_self, bool_blocking_connect): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_blocking_connect(const HTTPChannel self, bool blocking_connect)
        
        /**
         * If this flag is true, a socket connect will block even for nonblocking I/O
         * calls like begin_get_document(), begin_connect_to(), etc.  If false, a
         * socket connect will not block for nonblocking I/O calls, but will block for
         * blocking I/O calls (get_document(), connect_to(), etc.).
         *
         * Setting this true is useful when you want to use non-blocking I/O once you
         * have established the connection, but you don't want to bother with polling
         * for the initial connection.  It's also useful when you don't particularly
         * care about non-blocking I/O, but you need to respect timeouts like
         * connect_timeout and http_timeout.
         */
        """
        pass

    def set_connect_timeout(self, const_HTTPChannel_self, double_timeout_seconds): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_connect_timeout(const HTTPChannel self, double timeout_seconds)
        
        /**
         * Sets the maximum length of time, in seconds, that the channel will wait
         * before giving up on establishing a TCP connection.
         *
         * At present, this is used only for the nonblocking interfaces (e.g.
         * begin_get_document(), begin_connect_to()), but it is used whether
         * set_blocking_connect() is true or false.
         */
        """
        pass

    def set_content_type(self, const_HTTPChannel_self, str_content_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_content_type(const HTTPChannel self, str content_type)
        
        /**
         * Specifies the Content-Type header, useful for applications that require
         * different types of content, such as JSON.
         */
        """
        pass

    def set_download_throttle(self, const_HTTPChannel_self, bool_download_throttle): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_download_throttle(const HTTPChannel self, bool download_throttle)
        
        /**
         * Specifies whether nonblocking downloads (via download_to_file() or
         * download_to_ram()) will be limited so as not to use all available
         * bandwidth.
         *
         * If this is true, when a download has been started on this channel it will
         * be invoked no more frequently than get_max_updates_per_second(), and the
         * total bandwidth used by the download will be no more than
         * get_max_bytes_per_second().  If this is false, downloads will proceed as
         * fast as the server can send the data.
         *
         * This only has effect on the nonblocking I/O methods like
         * begin_get_document(), etc.  The blocking methods like get_document() always
         * use as much CPU and bandwidth as they can get.
         */
        """
        pass

    def set_expected_file_size(self, const_HTTPChannel_self, int_file_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_expected_file_size(const HTTPChannel self, int file_size)
        
        /**
         * This may be called immediately after a call to get_document() or some
         * related function to specify the expected size of the document we are
         * retrieving, if we happen to know.  This is used as the return value to
         * get_file_size() only in the case that the server does not tell us the
         * actual file size.
         */
        """
        pass

    def set_http_timeout(self, const_HTTPChannel_self, double_timeout_seconds): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_http_timeout(const HTTPChannel self, double timeout_seconds)
        
        /**
         * Sets the maximum length of time, in seconds, that the channel will wait for
         * the HTTP server to finish sending its response to our request.
         *
         * The timer starts counting after the TCP connection has been established
         * (see set_connect_timeout(), above) and the request has been sent.
         *
         * At present, this is used only for the nonblocking interfaces (e.g.
         * begin_get_document(), begin_connect_to()), but it is used whether
         * set_blocking_connect() is true or false.
         */
        """
        pass

    def set_idle_timeout(self, const_HTTPChannel_self, double_idle_timeout): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_idle_timeout(const HTTPChannel self, double idle_timeout)
        
        /**
         * Specifies the amount of time, in seconds, in which a previously-established
         * connection is allowed to remain open and unused.  If a previous connection
         * has remained unused for at least this number of seconds, it will be closed
         * and a new connection will be opened; otherwise, the same connection will be
         * reused for the next request (for this particular HTTPChannel).
         */
        """
        pass

    def set_max_bytes_per_second(self, const_HTTPChannel_self, double_max_bytes_per_second): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_bytes_per_second(const HTTPChannel self, double max_bytes_per_second)
        
        /**
         * When bandwidth throttling is in effect (see set_download_throttle()), this
         * specifies the maximum number of bytes per second that may be consumed by
         * this channel.
         */
        """
        pass

    def set_max_updates_per_second(self, const_HTTPChannel_self, double_max_updates_per_second): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_updates_per_second(const HTTPChannel self, double max_updates_per_second)
        
        /**
         * When bandwidth throttling is in effect (see set_download_throttle()), this
         * specifies the maximum number of times per second that run() will attempt to
         * do any downloading at all.
         */
        """
        pass

    def set_persistent_connection(self, const_HTTPChannel_self, bool_persistent_connection): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_persistent_connection(const HTTPChannel self, bool persistent_connection)
        
        /**
         * Indicates whether the HTTPChannel should try to keep the connection to the
         * server open and reuse that connection for multiple documents, or whether it
         * should close the connection and open a new one for each request.  Set this
         * true to keep the connections around when possible, false to recycle them.
         *
         * It makes most sense to set this false when the HTTPChannel will be used
         * only once to retrieve a single document, true when you will be using the
         * same HTTPChannel object to retrieve multiple documents.
         */
        """
        pass

    def set_proxy_tunnel(self, const_HTTPChannel_self, bool_proxy_tunnel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_proxy_tunnel(const HTTPChannel self, bool proxy_tunnel)
        
        /**
         * Normally, a proxy is itself asked for ordinary URL's, and the proxy decides
         * whether to hand the client a cached version of the document or to contact
         * the server for a fresh version.  The proxy may also modify the headers and
         * transfer encoding on the way.
         *
         * If this is set to true, then instead of asking for URL's from the proxy, we
         * will ask the proxy to open a connection to the server (for instance, on
         * port 80); if the proxy honors this request, then we contact the server
         * directly through this connection to retrieve the document.  If the proxy
         * does not honor the connect request, then the retrieve operation fails.
         *
         * SSL connections (e.g.  https), and connections through a Socks proxy, are
         * always tunneled, regardless of the setting of this flag.
         */
        """
        pass

    def set_skip_body_size(self, const_HTTPChannel_self, int_skip_body_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_skip_body_size(const HTTPChannel self, int skip_body_size)
        
        /**
         * Specifies the maximum number of bytes in a received (but unwanted) body
         * that will be skipped past, in order to reset to a new request.
         *
         * That is, if this HTTPChannel requests a file via get_document(), but does
         * not call download_to_ram(), download_to_file(), or open_read_body(), and
         * instead immediately requests a new file, then the HTTPChannel has a choice
         * whether to skip past the unwanted document, or to close the connection and
         * open a new one.  If the number of bytes to skip is more than this
         * threshold, the connection will be closed; otherwise, the data will simply
         * be read and discarded.
         */
        """
        pass

    def willCloseConnection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        will_close_connection(HTTPChannel self)
        
        /**
         * Returns true if the server has indicated it will close the connection after
         * this document has been read, or false if it will remain open (and future
         * documents may be requested on the same connection).
         */
        """
        pass

    def will_close_connection(self, HTTPChannel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        will_close_connection(HTTPChannel self)
        
        /**
         * Returns true if the server has indicated it will close the connection after
         * this document has been read, or false if it will remain open (and future
         * documents may be requested on the same connection).
         */
        """
        pass

    def writeHeaders(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_headers(HTTPChannel self, ostream out)
        
        /**
         * Outputs a list of all headers defined by the server to the indicated output
         * stream.
         */
        """
        pass

    def write_headers(self, HTTPChannel_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_headers(HTTPChannel self, ostream out)
        
        /**
         * Outputs a list of all headers defined by the server to the indicated output
         * stream.
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'SCDownloadInvalidRange': 19,
        'SCDownloadOpenError': 17,
        'SCDownloadWriteError': 18,
        'SCHttpErrorWatermark': 13,
        'SCIncomplete': 0,
        'SCInternalError': 1,
        'SCInvalidHttp': 6,
        'SCLostConnection': 4,
        'SCNoConnection': 2,
        'SCNonHttpResponse': 5,
        'SCSocksInvalidVersion': 7,
        'SCSocksNoAcceptableLoginMethod': 8,
        'SCSocksNoConnection': 10,
        'SCSocksRefused': 9,
        'SCSslInternalFailure': 11,
        'SCSslInvalidServerCertificate': 14,
        'SCSslNoHandshake': 12,
        'SCSslSelfSignedServerCertificate': 15,
        'SCSslUnexpectedServer': 16,
        'SCTimeout': 3,
        'SC_download_invalid_range': 19,
        'SC_download_open_error': 17,
        'SC_download_write_error': 18,
        'SC_http_error_watermark': 13,
        'SC_incomplete': 0,
        'SC_internal_error': 1,
        'SC_invalid_http': 6,
        'SC_lost_connection': 4,
        'SC_no_connection': 2,
        'SC_non_http_response': 5,
        'SC_socks_invalid_version': 7,
        'SC_socks_no_acceptable_login_method': 8,
        'SC_socks_no_connection': 10,
        'SC_socks_refused': 9,
        'SC_ssl_internal_failure': 11,
        'SC_ssl_invalid_server_certificate': 14,
        'SC_ssl_no_handshake': 12,
        'SC_ssl_self_signed_server_certificate': 15,
        'SC_ssl_unexpected_server': 16,
        'SC_timeout': 3,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.HTTPChannel' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.HTTPChannel' objects>"
        '__doc__': "/**\n * A single channel of communication from an HTTPClient.  This is similar to\n * the concept of a 'connection', except that HTTP is technically\n * connectionless; in fact, a channel may represent one unbroken connection or\n * it may transparently close and reopen a new connection with each request.\n *\n * A channel is conceptually a single thread of I/O. One document at a time\n * may be requested using a channel; a new document may (in general) not be\n * requested from the same HTTPChannel until the first document has been fully\n * retrieved.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.HTTPChannel' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE26CE80>'
        'beginConnectTo': None, # (!) real value is "<method 'beginConnectTo' of 'panda3d.core.HTTPChannel' objects>"
        'beginGetDocument': None, # (!) real value is "<method 'beginGetDocument' of 'panda3d.core.HTTPChannel' objects>"
        'beginGetHeader': None, # (!) real value is "<method 'beginGetHeader' of 'panda3d.core.HTTPChannel' objects>"
        'beginGetSubdocument': None, # (!) real value is "<method 'beginGetSubdocument' of 'panda3d.core.HTTPChannel' objects>"
        'beginPostForm': None, # (!) real value is "<method 'beginPostForm' of 'panda3d.core.HTTPChannel' objects>"
        'begin_connect_to': None, # (!) real value is "<method 'begin_connect_to' of 'panda3d.core.HTTPChannel' objects>"
        'begin_get_document': None, # (!) real value is "<method 'begin_get_document' of 'panda3d.core.HTTPChannel' objects>"
        'begin_get_header': None, # (!) real value is "<method 'begin_get_header' of 'panda3d.core.HTTPChannel' objects>"
        'begin_get_subdocument': None, # (!) real value is "<method 'begin_get_subdocument' of 'panda3d.core.HTTPChannel' objects>"
        'begin_post_form': None, # (!) real value is "<method 'begin_post_form' of 'panda3d.core.HTTPChannel' objects>"
        'clearExtraHeaders': None, # (!) real value is "<method 'clearExtraHeaders' of 'panda3d.core.HTTPChannel' objects>"
        'clear_extra_headers': None, # (!) real value is "<method 'clear_extra_headers' of 'panda3d.core.HTTPChannel' objects>"
        'closeReadBody': None, # (!) real value is "<method 'closeReadBody' of 'panda3d.core.HTTPChannel' objects>"
        'close_read_body': None, # (!) real value is "<method 'close_read_body' of 'panda3d.core.HTTPChannel' objects>"
        'connectTo': None, # (!) real value is "<method 'connectTo' of 'panda3d.core.HTTPChannel' objects>"
        'connect_to': None, # (!) real value is "<method 'connect_to' of 'panda3d.core.HTTPChannel' objects>"
        'deleteDocument': None, # (!) real value is "<method 'deleteDocument' of 'panda3d.core.HTTPChannel' objects>"
        'delete_document': None, # (!) real value is "<method 'delete_document' of 'panda3d.core.HTTPChannel' objects>"
        'downloadToFile': None, # (!) real value is "<method 'downloadToFile' of 'panda3d.core.HTTPChannel' objects>"
        'downloadToRam': None, # (!) real value is "<method 'downloadToRam' of 'panda3d.core.HTTPChannel' objects>"
        'downloadToStream': None, # (!) real value is "<method 'downloadToStream' of 'panda3d.core.HTTPChannel' objects>"
        'download_to_file': None, # (!) real value is "<method 'download_to_file' of 'panda3d.core.HTTPChannel' objects>"
        'download_to_ram': None, # (!) real value is "<method 'download_to_ram' of 'panda3d.core.HTTPChannel' objects>"
        'download_to_stream': None, # (!) real value is "<method 'download_to_stream' of 'panda3d.core.HTTPChannel' objects>"
        'getAllowProxy': None, # (!) real value is "<method 'getAllowProxy' of 'panda3d.core.HTTPChannel' objects>"
        'getBlockingConnect': None, # (!) real value is "<method 'getBlockingConnect' of 'panda3d.core.HTTPChannel' objects>"
        'getBytesDownloaded': None, # (!) real value is "<method 'getBytesDownloaded' of 'panda3d.core.HTTPChannel' objects>"
        'getBytesRequested': None, # (!) real value is "<method 'getBytesRequested' of 'panda3d.core.HTTPChannel' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE26CE80>)>'
        'getClient': None, # (!) real value is "<method 'getClient' of 'panda3d.core.HTTPChannel' objects>"
        'getConnectTimeout': None, # (!) real value is "<method 'getConnectTimeout' of 'panda3d.core.HTTPChannel' objects>"
        'getConnection': None, # (!) real value is "<method 'getConnection' of 'panda3d.core.HTTPChannel' objects>"
        'getContentType': None, # (!) real value is "<method 'getContentType' of 'panda3d.core.HTTPChannel' objects>"
        'getDocument': None, # (!) real value is "<method 'getDocument' of 'panda3d.core.HTTPChannel' objects>"
        'getDocumentSpec': None, # (!) real value is "<method 'getDocumentSpec' of 'panda3d.core.HTTPChannel' objects>"
        'getDownloadThrottle': None, # (!) real value is "<method 'getDownloadThrottle' of 'panda3d.core.HTTPChannel' objects>"
        'getFileSize': None, # (!) real value is "<method 'getFileSize' of 'panda3d.core.HTTPChannel' objects>"
        'getFirstByteDelivered': None, # (!) real value is "<method 'getFirstByteDelivered' of 'panda3d.core.HTTPChannel' objects>"
        'getFirstByteRequested': None, # (!) real value is "<method 'getFirstByteRequested' of 'panda3d.core.HTTPChannel' objects>"
        'getHeader': None, # (!) real value is "<method 'getHeader' of 'panda3d.core.HTTPChannel' objects>"
        'getHeaderValue': None, # (!) real value is "<method 'getHeaderValue' of 'panda3d.core.HTTPChannel' objects>"
        'getHttpTimeout': None, # (!) real value is "<method 'getHttpTimeout' of 'panda3d.core.HTTPChannel' objects>"
        'getHttpVersion': None, # (!) real value is "<method 'getHttpVersion' of 'panda3d.core.HTTPChannel' objects>"
        'getHttpVersionString': None, # (!) real value is "<method 'getHttpVersionString' of 'panda3d.core.HTTPChannel' objects>"
        'getIdleTimeout': None, # (!) real value is "<method 'getIdleTimeout' of 'panda3d.core.HTTPChannel' objects>"
        'getLastByteDelivered': None, # (!) real value is "<method 'getLastByteDelivered' of 'panda3d.core.HTTPChannel' objects>"
        'getLastByteRequested': None, # (!) real value is "<method 'getLastByteRequested' of 'panda3d.core.HTTPChannel' objects>"
        'getMaxBytesPerSecond': None, # (!) real value is "<method 'getMaxBytesPerSecond' of 'panda3d.core.HTTPChannel' objects>"
        'getMaxUpdatesPerSecond': None, # (!) real value is "<method 'getMaxUpdatesPerSecond' of 'panda3d.core.HTTPChannel' objects>"
        'getNumRedirectSteps': None, # (!) real value is "<method 'getNumRedirectSteps' of 'panda3d.core.HTTPChannel' objects>"
        'getOptions': None, # (!) real value is "<method 'getOptions' of 'panda3d.core.HTTPChannel' objects>"
        'getPersistentConnection': None, # (!) real value is "<method 'getPersistentConnection' of 'panda3d.core.HTTPChannel' objects>"
        'getProxyRealm': None, # (!) real value is "<method 'getProxyRealm' of 'panda3d.core.HTTPChannel' objects>"
        'getProxyTunnel': None, # (!) real value is "<method 'getProxyTunnel' of 'panda3d.core.HTTPChannel' objects>"
        'getRedirect': None, # (!) real value is "<method 'getRedirect' of 'panda3d.core.HTTPChannel' objects>"
        'getRedirectStep': None, # (!) real value is "<method 'getRedirectStep' of 'panda3d.core.HTTPChannel' objects>"
        'getRedirectSteps': None, # (!) real value is "<method 'getRedirectSteps' of 'panda3d.core.HTTPChannel' objects>"
        'getSkipBodySize': None, # (!) real value is "<method 'getSkipBodySize' of 'panda3d.core.HTTPChannel' objects>"
        'getStatusCode': None, # (!) real value is "<method 'getStatusCode' of 'panda3d.core.HTTPChannel' objects>"
        'getStatusString': None, # (!) real value is "<method 'getStatusString' of 'panda3d.core.HTTPChannel' objects>"
        'getSubdocument': None, # (!) real value is "<method 'getSubdocument' of 'panda3d.core.HTTPChannel' objects>"
        'getTrace': None, # (!) real value is "<method 'getTrace' of 'panda3d.core.HTTPChannel' objects>"
        'getUrl': None, # (!) real value is "<method 'getUrl' of 'panda3d.core.HTTPChannel' objects>"
        'getWwwRealm': None, # (!) real value is "<method 'getWwwRealm' of 'panda3d.core.HTTPChannel' objects>"
        'get_allow_proxy': None, # (!) real value is "<method 'get_allow_proxy' of 'panda3d.core.HTTPChannel' objects>"
        'get_blocking_connect': None, # (!) real value is "<method 'get_blocking_connect' of 'panda3d.core.HTTPChannel' objects>"
        'get_bytes_downloaded': None, # (!) real value is "<method 'get_bytes_downloaded' of 'panda3d.core.HTTPChannel' objects>"
        'get_bytes_requested': None, # (!) real value is "<method 'get_bytes_requested' of 'panda3d.core.HTTPChannel' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE26CE80>)>'
        'get_client': None, # (!) real value is "<method 'get_client' of 'panda3d.core.HTTPChannel' objects>"
        'get_connect_timeout': None, # (!) real value is "<method 'get_connect_timeout' of 'panda3d.core.HTTPChannel' objects>"
        'get_connection': None, # (!) real value is "<method 'get_connection' of 'panda3d.core.HTTPChannel' objects>"
        'get_content_type': None, # (!) real value is "<method 'get_content_type' of 'panda3d.core.HTTPChannel' objects>"
        'get_document': None, # (!) real value is "<method 'get_document' of 'panda3d.core.HTTPChannel' objects>"
        'get_document_spec': None, # (!) real value is "<method 'get_document_spec' of 'panda3d.core.HTTPChannel' objects>"
        'get_download_throttle': None, # (!) real value is "<method 'get_download_throttle' of 'panda3d.core.HTTPChannel' objects>"
        'get_file_size': None, # (!) real value is "<method 'get_file_size' of 'panda3d.core.HTTPChannel' objects>"
        'get_first_byte_delivered': None, # (!) real value is "<method 'get_first_byte_delivered' of 'panda3d.core.HTTPChannel' objects>"
        'get_first_byte_requested': None, # (!) real value is "<method 'get_first_byte_requested' of 'panda3d.core.HTTPChannel' objects>"
        'get_header': None, # (!) real value is "<method 'get_header' of 'panda3d.core.HTTPChannel' objects>"
        'get_header_value': None, # (!) real value is "<method 'get_header_value' of 'panda3d.core.HTTPChannel' objects>"
        'get_http_timeout': None, # (!) real value is "<method 'get_http_timeout' of 'panda3d.core.HTTPChannel' objects>"
        'get_http_version': None, # (!) real value is "<method 'get_http_version' of 'panda3d.core.HTTPChannel' objects>"
        'get_http_version_string': None, # (!) real value is "<method 'get_http_version_string' of 'panda3d.core.HTTPChannel' objects>"
        'get_idle_timeout': None, # (!) real value is "<method 'get_idle_timeout' of 'panda3d.core.HTTPChannel' objects>"
        'get_last_byte_delivered': None, # (!) real value is "<method 'get_last_byte_delivered' of 'panda3d.core.HTTPChannel' objects>"
        'get_last_byte_requested': None, # (!) real value is "<method 'get_last_byte_requested' of 'panda3d.core.HTTPChannel' objects>"
        'get_max_bytes_per_second': None, # (!) real value is "<method 'get_max_bytes_per_second' of 'panda3d.core.HTTPChannel' objects>"
        'get_max_updates_per_second': None, # (!) real value is "<method 'get_max_updates_per_second' of 'panda3d.core.HTTPChannel' objects>"
        'get_num_redirect_steps': None, # (!) real value is "<method 'get_num_redirect_steps' of 'panda3d.core.HTTPChannel' objects>"
        'get_options': None, # (!) real value is "<method 'get_options' of 'panda3d.core.HTTPChannel' objects>"
        'get_persistent_connection': None, # (!) real value is "<method 'get_persistent_connection' of 'panda3d.core.HTTPChannel' objects>"
        'get_proxy_realm': None, # (!) real value is "<method 'get_proxy_realm' of 'panda3d.core.HTTPChannel' objects>"
        'get_proxy_tunnel': None, # (!) real value is "<method 'get_proxy_tunnel' of 'panda3d.core.HTTPChannel' objects>"
        'get_redirect': None, # (!) real value is "<method 'get_redirect' of 'panda3d.core.HTTPChannel' objects>"
        'get_redirect_step': None, # (!) real value is "<method 'get_redirect_step' of 'panda3d.core.HTTPChannel' objects>"
        'get_redirect_steps': None, # (!) real value is "<method 'get_redirect_steps' of 'panda3d.core.HTTPChannel' objects>"
        'get_skip_body_size': None, # (!) real value is "<method 'get_skip_body_size' of 'panda3d.core.HTTPChannel' objects>"
        'get_status_code': None, # (!) real value is "<method 'get_status_code' of 'panda3d.core.HTTPChannel' objects>"
        'get_status_string': None, # (!) real value is "<method 'get_status_string' of 'panda3d.core.HTTPChannel' objects>"
        'get_subdocument': None, # (!) real value is "<method 'get_subdocument' of 'panda3d.core.HTTPChannel' objects>"
        'get_trace': None, # (!) real value is "<method 'get_trace' of 'panda3d.core.HTTPChannel' objects>"
        'get_url': None, # (!) real value is "<method 'get_url' of 'panda3d.core.HTTPChannel' objects>"
        'get_www_realm': None, # (!) real value is "<method 'get_www_realm' of 'panda3d.core.HTTPChannel' objects>"
        'isConnectionReady': None, # (!) real value is "<method 'isConnectionReady' of 'panda3d.core.HTTPChannel' objects>"
        'isDownloadComplete': None, # (!) real value is "<method 'isDownloadComplete' of 'panda3d.core.HTTPChannel' objects>"
        'isFileSizeKnown': None, # (!) real value is "<method 'isFileSizeKnown' of 'panda3d.core.HTTPChannel' objects>"
        'isValid': None, # (!) real value is "<method 'isValid' of 'panda3d.core.HTTPChannel' objects>"
        'is_connection_ready': None, # (!) real value is "<method 'is_connection_ready' of 'panda3d.core.HTTPChannel' objects>"
        'is_download_complete': None, # (!) real value is "<method 'is_download_complete' of 'panda3d.core.HTTPChannel' objects>"
        'is_file_size_known': None, # (!) real value is "<method 'is_file_size_known' of 'panda3d.core.HTTPChannel' objects>"
        'is_valid': None, # (!) real value is "<method 'is_valid' of 'panda3d.core.HTTPChannel' objects>"
        'openReadBody': None, # (!) real value is "<method 'openReadBody' of 'panda3d.core.HTTPChannel' objects>"
        'open_read_body': None, # (!) real value is "<method 'open_read_body' of 'panda3d.core.HTTPChannel' objects>"
        'postForm': None, # (!) real value is "<method 'postForm' of 'panda3d.core.HTTPChannel' objects>"
        'post_form': None, # (!) real value is "<method 'post_form' of 'panda3d.core.HTTPChannel' objects>"
        'preserveStatus': None, # (!) real value is "<method 'preserveStatus' of 'panda3d.core.HTTPChannel' objects>"
        'preserve_status': None, # (!) real value is "<method 'preserve_status' of 'panda3d.core.HTTPChannel' objects>"
        'putDocument': None, # (!) real value is "<method 'putDocument' of 'panda3d.core.HTTPChannel' objects>"
        'put_document': None, # (!) real value is "<method 'put_document' of 'panda3d.core.HTTPChannel' objects>"
        'reset': None, # (!) real value is "<method 'reset' of 'panda3d.core.HTTPChannel' objects>"
        'run': None, # (!) real value is "<method 'run' of 'panda3d.core.HTTPChannel' objects>"
        'sendExtraHeader': None, # (!) real value is "<method 'sendExtraHeader' of 'panda3d.core.HTTPChannel' objects>"
        'send_extra_header': None, # (!) real value is "<method 'send_extra_header' of 'panda3d.core.HTTPChannel' objects>"
        'setAllowProxy': None, # (!) real value is "<method 'setAllowProxy' of 'panda3d.core.HTTPChannel' objects>"
        'setBlockingConnect': None, # (!) real value is "<method 'setBlockingConnect' of 'panda3d.core.HTTPChannel' objects>"
        'setConnectTimeout': None, # (!) real value is "<method 'setConnectTimeout' of 'panda3d.core.HTTPChannel' objects>"
        'setContentType': None, # (!) real value is "<method 'setContentType' of 'panda3d.core.HTTPChannel' objects>"
        'setDownloadThrottle': None, # (!) real value is "<method 'setDownloadThrottle' of 'panda3d.core.HTTPChannel' objects>"
        'setExpectedFileSize': None, # (!) real value is "<method 'setExpectedFileSize' of 'panda3d.core.HTTPChannel' objects>"
        'setHttpTimeout': None, # (!) real value is "<method 'setHttpTimeout' of 'panda3d.core.HTTPChannel' objects>"
        'setIdleTimeout': None, # (!) real value is "<method 'setIdleTimeout' of 'panda3d.core.HTTPChannel' objects>"
        'setMaxBytesPerSecond': None, # (!) real value is "<method 'setMaxBytesPerSecond' of 'panda3d.core.HTTPChannel' objects>"
        'setMaxUpdatesPerSecond': None, # (!) real value is "<method 'setMaxUpdatesPerSecond' of 'panda3d.core.HTTPChannel' objects>"
        'setPersistentConnection': None, # (!) real value is "<method 'setPersistentConnection' of 'panda3d.core.HTTPChannel' objects>"
        'setProxyTunnel': None, # (!) real value is "<method 'setProxyTunnel' of 'panda3d.core.HTTPChannel' objects>"
        'setSkipBodySize': None, # (!) real value is "<method 'setSkipBodySize' of 'panda3d.core.HTTPChannel' objects>"
        'set_allow_proxy': None, # (!) real value is "<method 'set_allow_proxy' of 'panda3d.core.HTTPChannel' objects>"
        'set_blocking_connect': None, # (!) real value is "<method 'set_blocking_connect' of 'panda3d.core.HTTPChannel' objects>"
        'set_connect_timeout': None, # (!) real value is "<method 'set_connect_timeout' of 'panda3d.core.HTTPChannel' objects>"
        'set_content_type': None, # (!) real value is "<method 'set_content_type' of 'panda3d.core.HTTPChannel' objects>"
        'set_download_throttle': None, # (!) real value is "<method 'set_download_throttle' of 'panda3d.core.HTTPChannel' objects>"
        'set_expected_file_size': None, # (!) real value is "<method 'set_expected_file_size' of 'panda3d.core.HTTPChannel' objects>"
        'set_http_timeout': None, # (!) real value is "<method 'set_http_timeout' of 'panda3d.core.HTTPChannel' objects>"
        'set_idle_timeout': None, # (!) real value is "<method 'set_idle_timeout' of 'panda3d.core.HTTPChannel' objects>"
        'set_max_bytes_per_second': None, # (!) real value is "<method 'set_max_bytes_per_second' of 'panda3d.core.HTTPChannel' objects>"
        'set_max_updates_per_second': None, # (!) real value is "<method 'set_max_updates_per_second' of 'panda3d.core.HTTPChannel' objects>"
        'set_persistent_connection': None, # (!) real value is "<method 'set_persistent_connection' of 'panda3d.core.HTTPChannel' objects>"
        'set_proxy_tunnel': None, # (!) real value is "<method 'set_proxy_tunnel' of 'panda3d.core.HTTPChannel' objects>"
        'set_skip_body_size': None, # (!) real value is "<method 'set_skip_body_size' of 'panda3d.core.HTTPChannel' objects>"
        'willCloseConnection': None, # (!) real value is "<method 'willCloseConnection' of 'panda3d.core.HTTPChannel' objects>"
        'will_close_connection': None, # (!) real value is "<method 'will_close_connection' of 'panda3d.core.HTTPChannel' objects>"
        'writeHeaders': None, # (!) real value is "<method 'writeHeaders' of 'panda3d.core.HTTPChannel' objects>"
        'write_headers': None, # (!) real value is "<method 'write_headers' of 'panda3d.core.HTTPChannel' objects>"
    }
    SCDownloadInvalidRange = 19
    SCDownloadOpenError = 17
    SCDownloadWriteError = 18
    SCHttpErrorWatermark = 13
    SCIncomplete = 0
    SCInternalError = 1
    SCInvalidHttp = 6
    SCLostConnection = 4
    SCNoConnection = 2
    SCNonHttpResponse = 5
    SCSocksInvalidVersion = 7
    SCSocksNoAcceptableLoginMethod = 8
    SCSocksNoConnection = 10
    SCSocksRefused = 9
    SCSslInternalFailure = 11
    SCSslInvalidServerCertificate = 14
    SCSslNoHandshake = 12
    SCSslSelfSignedServerCertificate = 15
    SCSslUnexpectedServer = 16
    SCTimeout = 3
    SC_download_invalid_range = 19
    SC_download_open_error = 17
    SC_download_write_error = 18
    SC_http_error_watermark = 13
    SC_incomplete = 0
    SC_internal_error = 1
    SC_invalid_http = 6
    SC_lost_connection = 4
    SC_non_http_response = 5
    SC_no_connection = 2
    SC_socks_invalid_version = 7
    SC_socks_no_acceptable_login_method = 8
    SC_socks_no_connection = 10
    SC_socks_refused = 9
    SC_ssl_internal_failure = 11
    SC_ssl_invalid_server_certificate = 14
    SC_ssl_no_handshake = 12
    SC_ssl_self_signed_server_certificate = 15
    SC_ssl_unexpected_server = 16
    SC_timeout = 3


