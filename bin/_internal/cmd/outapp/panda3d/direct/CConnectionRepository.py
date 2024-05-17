# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class CConnectionRepository(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class implements the C++ side of the ConnectionRepository object.  In
     * particular, it manages the connection to the server once it has been opened
     * (but does not open it directly).  It manages reading and writing datagrams
     * on the connection and monitoring for unexpected disconnects as well as
     * handling intentional disconnects.
     *
     * Certain server messages, like field updates, are handled entirely within
     * the C++ layer, while server messages that are not understood by the C++
     * layer are returned up to the Python layer for processing.
     */
    """
    def abandonMessageBundles(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        abandon_message_bundles(const CConnectionRepository self)
        
        /**
         * throw out any msgs that have been queued up for message bundles
         */
        """
        pass

    def abandon_message_bundles(self, const_CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        abandon_message_bundles(const CConnectionRepository self)
        
        /**
         * throw out any msgs that have been queued up for message bundles
         */
        """
        pass

    def bundleMsg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        bundle_msg(const CConnectionRepository self, const Datagram dg)
        
        /**
         *
         */
        """
        pass

    def bundle_msg(self, const_CConnectionRepository_self, const_Datagram_dg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        bundle_msg(const CConnectionRepository self, const Datagram dg)
        
        /**
         *
         */
        """
        pass

    def checkDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        check_datagram(const CConnectionRepository self)
        
        /**
         * Returns true if a new datagram is available, false otherwise.  If the
         * return value is true, the new datagram may be retrieved via get_datagram(),
         * or preferably, with get_datagram_iterator() and get_msg_type().
         */
        """
        pass

    def check_datagram(self, const_CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        check_datagram(const CConnectionRepository self)
        
        /**
         * Returns true if a new datagram is available, false otherwise.  If the
         * return value is true, the new datagram may be retrieved via get_datagram(),
         * or preferably, with get_datagram_iterator() and get_msg_type().
         */
        """
        pass

    def connectNative(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        connect_native(const CConnectionRepository self, const URLSpec url)
        
        /**
         * Connects to the server using Panda's low-level and fast "native net"
         * library.
         */
        """
        pass

    def connect_native(self, const_CConnectionRepository_self, const_URLSpec_url): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        connect_native(const CConnectionRepository self, const URLSpec url)
        
        /**
         * Connects to the server using Panda's low-level and fast "native net"
         * library.
         */
        """
        pass

    def considerFlush(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        consider_flush(const CConnectionRepository self)
        
        /**
         * Sends the most recently queued data if enough time has elapsed.  This only
         * has meaning if set_collect_tcp() has been set to true.
         */
        """
        pass

    def consider_flush(self, const_CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        consider_flush(const CConnectionRepository self)
        
        /**
         * Sends the most recently queued data if enough time has elapsed.  This only
         * has meaning if set_collect_tcp() has been set to true.
         */
        """
        pass

    def disconnect(self, const_CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        disconnect(const CConnectionRepository self)
        
        /**
         * Closes the connection to the server.
         */
        """
        pass

    def flush(self, const_CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flush(const CConnectionRepository self)
        
        /**
         * Sends the most recently queued data now.  This only has meaning if
         * set_collect_tcp() has been set to true.
         */
        """
        pass

    def getBdc(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bdc(const CConnectionRepository self)
        
        /**
         * Returns the Buffered_DatagramConnection object associated with the
         * repository.
         */
        """
        pass

    def getClientDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_client_datagram(CConnectionRepository self)
        
        /**
         * Returns the client_datagram flag.
         */
        """
        pass

    def getCw(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cw(const CConnectionRepository self)
        
        /**
         * Returns the ConnectionWriter object associated with the repository.
         */
        """
        pass

    def getDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_datagram(const CConnectionRepository self, Datagram dg)
        
        /**
         * Fills the datagram object with the datagram most recently retrieved by
         * check_datagram().
         */
        """
        pass

    def getDatagramIterator(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_datagram_iterator(const CConnectionRepository self, DatagramIterator di)
        
        /**
         * Fills the DatagramIterator object with the iterator for the datagram most
         * recently retrieved by check_datagram().  This iterator has already read
         * past the datagram header and the message type, and is positioned at the
         * beginning of data.
         */
        """
        pass

    def getDcFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_dc_file(const CConnectionRepository self)
        
        /**
         * Returns the DCFile object associated with this repository.
         */
        """
        pass

    def getHandleCUpdates(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_handle_c_updates(CConnectionRepository self)
        
        /**
         * Returns true if this repository will process distributed updates internally
         * in C++ code, or false if it will return them to Python.
         */
        """
        pass

    def getHandleDatagramsInternally(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_handle_datagrams_internally(CConnectionRepository self)
        
        /**
         * Returns the handle_datagrams_internally flag.
         */
        """
        pass

    def getInQuietZone(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_in_quiet_zone(CConnectionRepository self)
        
        /**
         * Returns true if repository is in quiet zone mode
         */
        """
        pass

    def getMsgChannel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_msg_channel(CConnectionRepository self, int offset)
        
        /**
         * Returns the channel(s) to which the current message was sent, according to
         * the datagram headers.  This information is not available to the client.
         */
        """
        pass

    def getMsgChannelCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_msg_channel_count(CConnectionRepository self)
        """
        pass

    def getMsgSender(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_msg_sender(CConnectionRepository self)
        
        /**
         * Returns the sender ID of the current message, according to the datagram
         * headers.  This information is not available to the client.
         */
        """
        pass

    def getMsgType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_msg_type(CConnectionRepository self)
        
        // INLINE unsigned char get_sec_code() const;
        
        /**
         * Returns the type ID of the current message, according to the datagram
         * headers.
         */
        """
        pass

    def getOverflowEventName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_overflow_event_name()
        
        /**
         * Returns event string that will be thrown if the datagram reader queue
         * overflows.
         */
        """
        pass

    def getQcm(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_qcm(const CConnectionRepository self)
        
        /**
         * Returns the QueuedConnectionManager object associated with the repository.
         */
        """
        pass

    def getQcr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_qcr(const CConnectionRepository self)
        
        /**
         * Returns the QueuedConnectionReader object associated with the repository.
         */
        """
        pass

    def getSimulatedDisconnect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_simulated_disconnect(CConnectionRepository self)
        
        /**
         * Returns the simulated disconnect flag.  While this is true, no datagrams
         * will be retrieved from or sent to the server.  The idea is to simulate a
         * temporary network outage.
         */
        """
        pass

    def getStream(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_stream(const CConnectionRepository self)
        
        /**
         * Returns the SocketStream that internally represents the already-established
         * HTTP connection.  Returns NULL if there is no current HTTP connection.
         */
        """
        pass

    def getTcpHeaderSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tcp_header_size(CConnectionRepository self)
        
        /**
         * Returns the current setting of TCP header size.  See set_tcp_header_size().
         */
        """
        pass

    def getTimeWarning(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_time_warning(CConnectionRepository self)
        
        /**
         * Returns the current setting of the time_warning field.
         */
        """
        pass

    def getVerbose(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_verbose(CConnectionRepository self)
        
        /**
         * Returns the current setting of the verbose flag.  When true, this describes
         * every message going back and forth on the wire.
         */
        """
        pass

    def getWantMessageBundling(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_want_message_bundling(CConnectionRepository self)
        
        /**
         * Returns true if message bundling enabled
         */
        """
        pass

    def get_bdc(self, const_CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bdc(const CConnectionRepository self)
        
        /**
         * Returns the Buffered_DatagramConnection object associated with the
         * repository.
         */
        """
        pass

    def get_client_datagram(self, CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_client_datagram(CConnectionRepository self)
        
        /**
         * Returns the client_datagram flag.
         */
        """
        pass

    def get_cw(self, const_CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cw(const CConnectionRepository self)
        
        /**
         * Returns the ConnectionWriter object associated with the repository.
         */
        """
        pass

    def get_datagram(self, const_CConnectionRepository_self, Datagram_dg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_datagram(const CConnectionRepository self, Datagram dg)
        
        /**
         * Fills the datagram object with the datagram most recently retrieved by
         * check_datagram().
         */
        """
        pass

    def get_datagram_iterator(self, const_CConnectionRepository_self, DatagramIterator_di): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_datagram_iterator(const CConnectionRepository self, DatagramIterator di)
        
        /**
         * Fills the DatagramIterator object with the iterator for the datagram most
         * recently retrieved by check_datagram().  This iterator has already read
         * past the datagram header and the message type, and is positioned at the
         * beginning of data.
         */
        """
        pass

    def get_dc_file(self, const_CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_dc_file(const CConnectionRepository self)
        
        /**
         * Returns the DCFile object associated with this repository.
         */
        """
        pass

    def get_handle_c_updates(self, CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_handle_c_updates(CConnectionRepository self)
        
        /**
         * Returns true if this repository will process distributed updates internally
         * in C++ code, or false if it will return them to Python.
         */
        """
        pass

    def get_handle_datagrams_internally(self, CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_handle_datagrams_internally(CConnectionRepository self)
        
        /**
         * Returns the handle_datagrams_internally flag.
         */
        """
        pass

    def get_in_quiet_zone(self, CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_in_quiet_zone(CConnectionRepository self)
        
        /**
         * Returns true if repository is in quiet zone mode
         */
        """
        pass

    def get_msg_channel(self, CConnectionRepository_self, int_offset): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_msg_channel(CConnectionRepository self, int offset)
        
        /**
         * Returns the channel(s) to which the current message was sent, according to
         * the datagram headers.  This information is not available to the client.
         */
        """
        pass

    def get_msg_channel_count(self, CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_msg_channel_count(CConnectionRepository self)
        """
        pass

    def get_msg_sender(self, CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_msg_sender(CConnectionRepository self)
        
        /**
         * Returns the sender ID of the current message, according to the datagram
         * headers.  This information is not available to the client.
         */
        """
        pass

    def get_msg_type(self, CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_msg_type(CConnectionRepository self)
        
        // INLINE unsigned char get_sec_code() const;
        
        /**
         * Returns the type ID of the current message, according to the datagram
         * headers.
         */
        """
        pass

    def get_overflow_event_name(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_overflow_event_name()
        
        /**
         * Returns event string that will be thrown if the datagram reader queue
         * overflows.
         */
        """
        pass

    def get_qcm(self, const_CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_qcm(const CConnectionRepository self)
        
        /**
         * Returns the QueuedConnectionManager object associated with the repository.
         */
        """
        pass

    def get_qcr(self, const_CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_qcr(const CConnectionRepository self)
        
        /**
         * Returns the QueuedConnectionReader object associated with the repository.
         */
        """
        pass

    def get_simulated_disconnect(self, CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_simulated_disconnect(CConnectionRepository self)
        
        /**
         * Returns the simulated disconnect flag.  While this is true, no datagrams
         * will be retrieved from or sent to the server.  The idea is to simulate a
         * temporary network outage.
         */
        """
        pass

    def get_stream(self, const_CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_stream(const CConnectionRepository self)
        
        /**
         * Returns the SocketStream that internally represents the already-established
         * HTTP connection.  Returns NULL if there is no current HTTP connection.
         */
        """
        pass

    def get_tcp_header_size(self, CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tcp_header_size(CConnectionRepository self)
        
        /**
         * Returns the current setting of TCP header size.  See set_tcp_header_size().
         */
        """
        pass

    def get_time_warning(self, CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_time_warning(CConnectionRepository self)
        
        /**
         * Returns the current setting of the time_warning field.
         */
        """
        pass

    def get_verbose(self, CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_verbose(CConnectionRepository self)
        
        /**
         * Returns the current setting of the verbose flag.  When true, this describes
         * every message going back and forth on the wire.
         */
        """
        pass

    def get_want_message_bundling(self, CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_want_message_bundling(CConnectionRepository self)
        
        /**
         * Returns true if message bundling enabled
         */
        """
        pass

    def hasOwnerView(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_owner_view(CConnectionRepository self)
        
        /**
         * Returns true if this repository can have 'owner' views of distributed
         * objects.
         */
        """
        pass

    def has_owner_view(self, CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_owner_view(CConnectionRepository self)
        
        /**
         * Returns true if this repository can have 'owner' views of distributed
         * objects.
         */
        """
        pass

    def isBundlingMessages(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_bundling_messages(CConnectionRepository self)
        
        /**
         * Returns true if repository is queueing outgoing messages into a message
         * bundle
         */
        """
        pass

    def isConnected(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_connected(const CConnectionRepository self)
        
        /**
         * Returns true if the connection to the gameserver is established and still
         * good, false if we are not connected.  A false value means either (a) we
         * never successfully connected, (b) we explicitly called disconnect(), or (c)
         * we were connected, but the connection was spontaneously lost.
         */
        """
        pass

    def is_bundling_messages(self, CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_bundling_messages(CConnectionRepository self)
        
        /**
         * Returns true if repository is queueing outgoing messages into a message
         * bundle
         */
        """
        pass

    def is_connected(self, const_CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_connected(const CConnectionRepository self)
        
        /**
         * Returns true if the connection to the gameserver is established and still
         * good, false if we are not connected.  A false value means either (a) we
         * never successfully connected, (b) we explicitly called disconnect(), or (c)
         * we were connected, but the connection was spontaneously lost.
         */
        """
        pass

    def sendDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        send_datagram(const CConnectionRepository self, const Datagram dg)
        
        /**
         * Queues the indicated datagram for sending to the server.  It may not get
         * sent immediately if collect_tcp is in effect; call flush() to guarantee it
         * is sent now.
         */
        """
        pass

    def sendMessageBundle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        send_message_bundle(const CConnectionRepository self, int channel, int sender_channel)
        
        /**
         * Send network messages queued up since startMessageBundle was called.
         */
        """
        pass

    def send_datagram(self, const_CConnectionRepository_self, const_Datagram_dg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        send_datagram(const CConnectionRepository self, const Datagram dg)
        
        /**
         * Queues the indicated datagram for sending to the server.  It may not get
         * sent immediately if collect_tcp is in effect; call flush() to guarantee it
         * is sent now.
         */
        """
        pass

    def send_message_bundle(self, const_CConnectionRepository_self, int_channel, int_sender_channel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        send_message_bundle(const CConnectionRepository self, int channel, int sender_channel)
        
        /**
         * Send network messages queued up since startMessageBundle was called.
         */
        """
        pass

    def setClientDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_client_datagram(const CConnectionRepository self, bool client_datagram)
        
        /**
         * Sets the client_datagram flag.  If this is true, incoming datagrams are not
         * expected to be prefixed with the server routing information like message
         * sender, channel number, etc.; otherwise, these server fields are parsed and
         * removed from each incoming datagram.
         */
        """
        pass

    def setConnectionHttp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_connection_http(const CConnectionRepository self, HTTPChannel channel)
        
        /**
         * Once a connection has been established via the HTTP interface, gets the
         * connection and uses it.  The supplied HTTPChannel object must have a
         * connection available via get_connection().
         */
        """
        pass

    def setHandleCUpdates(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_handle_c_updates(const CConnectionRepository self, bool handle_c_updates)
        
        /**
         * Set true to specify this repository should process distributed updates
         * internally in C++ code, or false if it should return them to Python.
         */
        """
        pass

    def setHandleDatagramsInternally(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_handle_datagrams_internally(const CConnectionRepository self, bool handle_datagrams_internally)
        
        /**
         * Sets the handle_datagrams_internally flag.  When true, certain message
         * types can be handled by the C++ code in in this module.  When false, all
         * datagrams, regardless of message type, are passed up to Python for
         * processing.
         *
         * The CMU distributed-object implementation requires this to be set false.
         */
        """
        pass

    def setInQuietZone(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_in_quiet_zone(const CConnectionRepository self, bool flag)
        
        /**
         * Enables/disables quiet zone mode
         */
        """
        pass

    def setPythonRepository(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_python_repository(const CConnectionRepository self, object python_repository)
        
        /**
         * Records the pointer to the Python class that derives from
         * CConnectionRepository.  This allows the C++ implementation to directly
         * manipulation some python structures on the repository.
         */
        """
        pass

    def setSimulatedDisconnect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_simulated_disconnect(const CConnectionRepository self, bool simulated_disconnect)
        
        /**
         * Sets the simulated disconnect flag.  While this is true, no datagrams will
         * be retrieved from or sent to the server.  The idea is to simulate a
         * temporary network outage.
         */
        """
        pass

    def setTcpHeaderSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tcp_header_size(const CConnectionRepository self, int tcp_header_size)
        
        /**
         * Sets the header size of TCP packets.  At the present, legal values for this
         * are 0, 2, or 4; this specifies the number of bytes to use encode the
         * datagram length at the start of each TCP datagram.  Sender and receiver
         * must independently agree on this.
         */
        """
        pass

    def setTimeWarning(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_time_warning(const CConnectionRepository self, float time_warning)
        
        /**
         * Directly sets the time_warning field.  When non zero, this describes every
         * message going back and forth on the wire when the msg handling time is over
         * it
         */
        """
        pass

    def setVerbose(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_verbose(const CConnectionRepository self, bool verbose)
        
        /**
         * Directly sets the verbose flag.  When true, this describes every message
         * going back and forth on the wire.
         */
        """
        pass

    def setWantMessageBundling(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_want_message_bundling(const CConnectionRepository self, bool flag)
        
        /**
         * Enable/disable outbound message bundling
         */
        """
        pass

    def set_client_datagram(self, const_CConnectionRepository_self, bool_client_datagram): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_client_datagram(const CConnectionRepository self, bool client_datagram)
        
        /**
         * Sets the client_datagram flag.  If this is true, incoming datagrams are not
         * expected to be prefixed with the server routing information like message
         * sender, channel number, etc.; otherwise, these server fields are parsed and
         * removed from each incoming datagram.
         */
        """
        pass

    def set_connection_http(self, const_CConnectionRepository_self, HTTPChannel_channel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_connection_http(const CConnectionRepository self, HTTPChannel channel)
        
        /**
         * Once a connection has been established via the HTTP interface, gets the
         * connection and uses it.  The supplied HTTPChannel object must have a
         * connection available via get_connection().
         */
        """
        pass

    def set_handle_c_updates(self, const_CConnectionRepository_self, bool_handle_c_updates): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_handle_c_updates(const CConnectionRepository self, bool handle_c_updates)
        
        /**
         * Set true to specify this repository should process distributed updates
         * internally in C++ code, or false if it should return them to Python.
         */
        """
        pass

    def set_handle_datagrams_internally(self, const_CConnectionRepository_self, bool_handle_datagrams_internally): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_handle_datagrams_internally(const CConnectionRepository self, bool handle_datagrams_internally)
        
        /**
         * Sets the handle_datagrams_internally flag.  When true, certain message
         * types can be handled by the C++ code in in this module.  When false, all
         * datagrams, regardless of message type, are passed up to Python for
         * processing.
         *
         * The CMU distributed-object implementation requires this to be set false.
         */
        """
        pass

    def set_in_quiet_zone(self, const_CConnectionRepository_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_in_quiet_zone(const CConnectionRepository self, bool flag)
        
        /**
         * Enables/disables quiet zone mode
         */
        """
        pass

    def set_python_repository(self, const_CConnectionRepository_self, object_python_repository): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_python_repository(const CConnectionRepository self, object python_repository)
        
        /**
         * Records the pointer to the Python class that derives from
         * CConnectionRepository.  This allows the C++ implementation to directly
         * manipulation some python structures on the repository.
         */
        """
        pass

    def set_simulated_disconnect(self, const_CConnectionRepository_self, bool_simulated_disconnect): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_simulated_disconnect(const CConnectionRepository self, bool simulated_disconnect)
        
        /**
         * Sets the simulated disconnect flag.  While this is true, no datagrams will
         * be retrieved from or sent to the server.  The idea is to simulate a
         * temporary network outage.
         */
        """
        pass

    def set_tcp_header_size(self, const_CConnectionRepository_self, int_tcp_header_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tcp_header_size(const CConnectionRepository self, int tcp_header_size)
        
        /**
         * Sets the header size of TCP packets.  At the present, legal values for this
         * are 0, 2, or 4; this specifies the number of bytes to use encode the
         * datagram length at the start of each TCP datagram.  Sender and receiver
         * must independently agree on this.
         */
        """
        pass

    def set_time_warning(self, const_CConnectionRepository_self, float_time_warning): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_time_warning(const CConnectionRepository self, float time_warning)
        
        /**
         * Directly sets the time_warning field.  When non zero, this describes every
         * message going back and forth on the wire when the msg handling time is over
         * it
         */
        """
        pass

    def set_verbose(self, const_CConnectionRepository_self, bool_verbose): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_verbose(const CConnectionRepository self, bool verbose)
        
        /**
         * Directly sets the verbose flag.  When true, this describes every message
         * going back and forth on the wire.
         */
        """
        pass

    def set_want_message_bundling(self, const_CConnectionRepository_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_want_message_bundling(const CConnectionRepository self, bool flag)
        
        /**
         * Enable/disable outbound message bundling
         */
        """
        pass

    def shutdown(self, const_CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        shutdown(const CConnectionRepository self)
        
        /**
         * May be called at application shutdown to ensure all threads are cleaned up.
         */
        """
        pass

    def startMessageBundle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        start_message_bundle(const CConnectionRepository self)
        
        /**
         * Send a set of messages to the state server that will be processed
         * atomically.  For instance, you can do a combined setLocation/setPos and
         * prevent race conditions where clients briefly get the setLocation but not
         * the setPos, because the state server hasn't processed the setPos yet
         */
        """
        pass

    def start_message_bundle(self, const_CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        start_message_bundle(const CConnectionRepository self)
        
        /**
         * Send a set of messages to the state server that will be processed
         * atomically.  For instance, you can do a combined setLocation/setPos and
         * prevent race conditions where clients briefly get the setLocation but not
         * the setPos, because the state server hasn't processed the setPos yet
         */
        """
        pass

    def toggleVerbose(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        toggle_verbose(const CConnectionRepository self)
        
        /**
         * Toggles the current setting of the verbose flag.  When true, this describes
         * every message going back and forth on the wire.
         */
        """
        pass

    def toggle_verbose(self, const_CConnectionRepository_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        toggle_verbose(const CConnectionRepository self)
        
        /**
         * Toggles the current setting of the verbose flag.  When true, this describes
         * every message going back and forth on the wire.
         */
        """
        pass

    def tryConnectNet(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        try_connect_net(const CConnectionRepository self, const URLSpec url)
        
        /**
         * Uses Panda's "net" library to try to connect to the server and port named
         * in the indicated URL.  Returns true if successful, false otherwise.
         */
        """
        pass

    def try_connect_net(self, const_CConnectionRepository_self, const_URLSpec_url): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        try_connect_net(const CConnectionRepository self, const URLSpec url)
        
        /**
         * Uses Panda's "net" library to try to connect to the server and port named
         * in the indicated URL.  Returns true if successful, false otherwise.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This class implements the C++ side of the ConnectionRepository object.  In\n * particular, it manages the connection to the server once it has been opened\n * (but does not open it directly).  It manages reading and writing datagrams\n * on the connection and monitoring for unexpected disconnects as well as\n * handling intentional disconnects.\n *\n * Certain server messages, like field updates, are handled entirely within\n * the C++ layer, while server messages that are not understood by the C++\n * layer are returned up to the Python layer for processing.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.direct.CConnectionRepository' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68EA260>'
        'abandonMessageBundles': None, # (!) real value is "<method 'abandonMessageBundles' of 'panda3d.direct.CConnectionRepository' objects>"
        'abandon_message_bundles': None, # (!) real value is "<method 'abandon_message_bundles' of 'panda3d.direct.CConnectionRepository' objects>"
        'bundleMsg': None, # (!) real value is "<method 'bundleMsg' of 'panda3d.direct.CConnectionRepository' objects>"
        'bundle_msg': None, # (!) real value is "<method 'bundle_msg' of 'panda3d.direct.CConnectionRepository' objects>"
        'checkDatagram': None, # (!) real value is "<method 'checkDatagram' of 'panda3d.direct.CConnectionRepository' objects>"
        'check_datagram': None, # (!) real value is "<method 'check_datagram' of 'panda3d.direct.CConnectionRepository' objects>"
        'connectNative': None, # (!) real value is "<method 'connectNative' of 'panda3d.direct.CConnectionRepository' objects>"
        'connect_native': None, # (!) real value is "<method 'connect_native' of 'panda3d.direct.CConnectionRepository' objects>"
        'considerFlush': None, # (!) real value is "<method 'considerFlush' of 'panda3d.direct.CConnectionRepository' objects>"
        'consider_flush': None, # (!) real value is "<method 'consider_flush' of 'panda3d.direct.CConnectionRepository' objects>"
        'disconnect': None, # (!) real value is "<method 'disconnect' of 'panda3d.direct.CConnectionRepository' objects>"
        'flush': None, # (!) real value is "<method 'flush' of 'panda3d.direct.CConnectionRepository' objects>"
        'getBdc': None, # (!) real value is "<method 'getBdc' of 'panda3d.direct.CConnectionRepository' objects>"
        'getClientDatagram': None, # (!) real value is "<method 'getClientDatagram' of 'panda3d.direct.CConnectionRepository' objects>"
        'getCw': None, # (!) real value is "<method 'getCw' of 'panda3d.direct.CConnectionRepository' objects>"
        'getDatagram': None, # (!) real value is "<method 'getDatagram' of 'panda3d.direct.CConnectionRepository' objects>"
        'getDatagramIterator': None, # (!) real value is "<method 'getDatagramIterator' of 'panda3d.direct.CConnectionRepository' objects>"
        'getDcFile': None, # (!) real value is "<method 'getDcFile' of 'panda3d.direct.CConnectionRepository' objects>"
        'getHandleCUpdates': None, # (!) real value is "<method 'getHandleCUpdates' of 'panda3d.direct.CConnectionRepository' objects>"
        'getHandleDatagramsInternally': None, # (!) real value is "<method 'getHandleDatagramsInternally' of 'panda3d.direct.CConnectionRepository' objects>"
        'getInQuietZone': None, # (!) real value is "<method 'getInQuietZone' of 'panda3d.direct.CConnectionRepository' objects>"
        'getMsgChannel': None, # (!) real value is "<method 'getMsgChannel' of 'panda3d.direct.CConnectionRepository' objects>"
        'getMsgChannelCount': None, # (!) real value is "<method 'getMsgChannelCount' of 'panda3d.direct.CConnectionRepository' objects>"
        'getMsgSender': None, # (!) real value is "<method 'getMsgSender' of 'panda3d.direct.CConnectionRepository' objects>"
        'getMsgType': None, # (!) real value is "<method 'getMsgType' of 'panda3d.direct.CConnectionRepository' objects>"
        'getOverflowEventName': None, # (!) real value is '<staticmethod(<built-in method getOverflowEventName of type object at 0x00007FFDC68EA260>)>'
        'getQcm': None, # (!) real value is "<method 'getQcm' of 'panda3d.direct.CConnectionRepository' objects>"
        'getQcr': None, # (!) real value is "<method 'getQcr' of 'panda3d.direct.CConnectionRepository' objects>"
        'getSimulatedDisconnect': None, # (!) real value is "<method 'getSimulatedDisconnect' of 'panda3d.direct.CConnectionRepository' objects>"
        'getStream': None, # (!) real value is "<method 'getStream' of 'panda3d.direct.CConnectionRepository' objects>"
        'getTcpHeaderSize': None, # (!) real value is "<method 'getTcpHeaderSize' of 'panda3d.direct.CConnectionRepository' objects>"
        'getTimeWarning': None, # (!) real value is "<method 'getTimeWarning' of 'panda3d.direct.CConnectionRepository' objects>"
        'getVerbose': None, # (!) real value is "<method 'getVerbose' of 'panda3d.direct.CConnectionRepository' objects>"
        'getWantMessageBundling': None, # (!) real value is "<method 'getWantMessageBundling' of 'panda3d.direct.CConnectionRepository' objects>"
        'get_bdc': None, # (!) real value is "<method 'get_bdc' of 'panda3d.direct.CConnectionRepository' objects>"
        'get_client_datagram': None, # (!) real value is "<method 'get_client_datagram' of 'panda3d.direct.CConnectionRepository' objects>"
        'get_cw': None, # (!) real value is "<method 'get_cw' of 'panda3d.direct.CConnectionRepository' objects>"
        'get_datagram': None, # (!) real value is "<method 'get_datagram' of 'panda3d.direct.CConnectionRepository' objects>"
        'get_datagram_iterator': None, # (!) real value is "<method 'get_datagram_iterator' of 'panda3d.direct.CConnectionRepository' objects>"
        'get_dc_file': None, # (!) real value is "<method 'get_dc_file' of 'panda3d.direct.CConnectionRepository' objects>"
        'get_handle_c_updates': None, # (!) real value is "<method 'get_handle_c_updates' of 'panda3d.direct.CConnectionRepository' objects>"
        'get_handle_datagrams_internally': None, # (!) real value is "<method 'get_handle_datagrams_internally' of 'panda3d.direct.CConnectionRepository' objects>"
        'get_in_quiet_zone': None, # (!) real value is "<method 'get_in_quiet_zone' of 'panda3d.direct.CConnectionRepository' objects>"
        'get_msg_channel': None, # (!) real value is "<method 'get_msg_channel' of 'panda3d.direct.CConnectionRepository' objects>"
        'get_msg_channel_count': None, # (!) real value is "<method 'get_msg_channel_count' of 'panda3d.direct.CConnectionRepository' objects>"
        'get_msg_sender': None, # (!) real value is "<method 'get_msg_sender' of 'panda3d.direct.CConnectionRepository' objects>"
        'get_msg_type': None, # (!) real value is "<method 'get_msg_type' of 'panda3d.direct.CConnectionRepository' objects>"
        'get_overflow_event_name': None, # (!) real value is '<staticmethod(<built-in method get_overflow_event_name of type object at 0x00007FFDC68EA260>)>'
        'get_qcm': None, # (!) real value is "<method 'get_qcm' of 'panda3d.direct.CConnectionRepository' objects>"
        'get_qcr': None, # (!) real value is "<method 'get_qcr' of 'panda3d.direct.CConnectionRepository' objects>"
        'get_simulated_disconnect': None, # (!) real value is "<method 'get_simulated_disconnect' of 'panda3d.direct.CConnectionRepository' objects>"
        'get_stream': None, # (!) real value is "<method 'get_stream' of 'panda3d.direct.CConnectionRepository' objects>"
        'get_tcp_header_size': None, # (!) real value is "<method 'get_tcp_header_size' of 'panda3d.direct.CConnectionRepository' objects>"
        'get_time_warning': None, # (!) real value is "<method 'get_time_warning' of 'panda3d.direct.CConnectionRepository' objects>"
        'get_verbose': None, # (!) real value is "<method 'get_verbose' of 'panda3d.direct.CConnectionRepository' objects>"
        'get_want_message_bundling': None, # (!) real value is "<method 'get_want_message_bundling' of 'panda3d.direct.CConnectionRepository' objects>"
        'hasOwnerView': None, # (!) real value is "<method 'hasOwnerView' of 'panda3d.direct.CConnectionRepository' objects>"
        'has_owner_view': None, # (!) real value is "<method 'has_owner_view' of 'panda3d.direct.CConnectionRepository' objects>"
        'isBundlingMessages': None, # (!) real value is "<method 'isBundlingMessages' of 'panda3d.direct.CConnectionRepository' objects>"
        'isConnected': None, # (!) real value is "<method 'isConnected' of 'panda3d.direct.CConnectionRepository' objects>"
        'is_bundling_messages': None, # (!) real value is "<method 'is_bundling_messages' of 'panda3d.direct.CConnectionRepository' objects>"
        'is_connected': None, # (!) real value is "<method 'is_connected' of 'panda3d.direct.CConnectionRepository' objects>"
        'sendDatagram': None, # (!) real value is "<method 'sendDatagram' of 'panda3d.direct.CConnectionRepository' objects>"
        'sendMessageBundle': None, # (!) real value is "<method 'sendMessageBundle' of 'panda3d.direct.CConnectionRepository' objects>"
        'send_datagram': None, # (!) real value is "<method 'send_datagram' of 'panda3d.direct.CConnectionRepository' objects>"
        'send_message_bundle': None, # (!) real value is "<method 'send_message_bundle' of 'panda3d.direct.CConnectionRepository' objects>"
        'setClientDatagram': None, # (!) real value is "<method 'setClientDatagram' of 'panda3d.direct.CConnectionRepository' objects>"
        'setConnectionHttp': None, # (!) real value is "<method 'setConnectionHttp' of 'panda3d.direct.CConnectionRepository' objects>"
        'setHandleCUpdates': None, # (!) real value is "<method 'setHandleCUpdates' of 'panda3d.direct.CConnectionRepository' objects>"
        'setHandleDatagramsInternally': None, # (!) real value is "<method 'setHandleDatagramsInternally' of 'panda3d.direct.CConnectionRepository' objects>"
        'setInQuietZone': None, # (!) real value is "<method 'setInQuietZone' of 'panda3d.direct.CConnectionRepository' objects>"
        'setPythonRepository': None, # (!) real value is "<method 'setPythonRepository' of 'panda3d.direct.CConnectionRepository' objects>"
        'setSimulatedDisconnect': None, # (!) real value is "<method 'setSimulatedDisconnect' of 'panda3d.direct.CConnectionRepository' objects>"
        'setTcpHeaderSize': None, # (!) real value is "<method 'setTcpHeaderSize' of 'panda3d.direct.CConnectionRepository' objects>"
        'setTimeWarning': None, # (!) real value is "<method 'setTimeWarning' of 'panda3d.direct.CConnectionRepository' objects>"
        'setVerbose': None, # (!) real value is "<method 'setVerbose' of 'panda3d.direct.CConnectionRepository' objects>"
        'setWantMessageBundling': None, # (!) real value is "<method 'setWantMessageBundling' of 'panda3d.direct.CConnectionRepository' objects>"
        'set_client_datagram': None, # (!) real value is "<method 'set_client_datagram' of 'panda3d.direct.CConnectionRepository' objects>"
        'set_connection_http': None, # (!) real value is "<method 'set_connection_http' of 'panda3d.direct.CConnectionRepository' objects>"
        'set_handle_c_updates': None, # (!) real value is "<method 'set_handle_c_updates' of 'panda3d.direct.CConnectionRepository' objects>"
        'set_handle_datagrams_internally': None, # (!) real value is "<method 'set_handle_datagrams_internally' of 'panda3d.direct.CConnectionRepository' objects>"
        'set_in_quiet_zone': None, # (!) real value is "<method 'set_in_quiet_zone' of 'panda3d.direct.CConnectionRepository' objects>"
        'set_python_repository': None, # (!) real value is "<method 'set_python_repository' of 'panda3d.direct.CConnectionRepository' objects>"
        'set_simulated_disconnect': None, # (!) real value is "<method 'set_simulated_disconnect' of 'panda3d.direct.CConnectionRepository' objects>"
        'set_tcp_header_size': None, # (!) real value is "<method 'set_tcp_header_size' of 'panda3d.direct.CConnectionRepository' objects>"
        'set_time_warning': None, # (!) real value is "<method 'set_time_warning' of 'panda3d.direct.CConnectionRepository' objects>"
        'set_verbose': None, # (!) real value is "<method 'set_verbose' of 'panda3d.direct.CConnectionRepository' objects>"
        'set_want_message_bundling': None, # (!) real value is "<method 'set_want_message_bundling' of 'panda3d.direct.CConnectionRepository' objects>"
        'shutdown': None, # (!) real value is "<method 'shutdown' of 'panda3d.direct.CConnectionRepository' objects>"
        'startMessageBundle': None, # (!) real value is "<method 'startMessageBundle' of 'panda3d.direct.CConnectionRepository' objects>"
        'start_message_bundle': None, # (!) real value is "<method 'start_message_bundle' of 'panda3d.direct.CConnectionRepository' objects>"
        'toggleVerbose': None, # (!) real value is "<method 'toggleVerbose' of 'panda3d.direct.CConnectionRepository' objects>"
        'toggle_verbose': None, # (!) real value is "<method 'toggle_verbose' of 'panda3d.direct.CConnectionRepository' objects>"
        'tryConnectNet': None, # (!) real value is "<method 'tryConnectNet' of 'panda3d.direct.CConnectionRepository' objects>"
        'try_connect_net': None, # (!) real value is "<method 'try_connect_net' of 'panda3d.direct.CConnectionRepository' objects>"
    }


