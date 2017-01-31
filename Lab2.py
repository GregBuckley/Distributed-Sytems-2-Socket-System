import socket
import threading
import argparse
max_threads = 10
thread_pool = []
STUDENT_ID = "133252220"
ip_address = "10.62.0.148"
SOCKET_LIST = []
ALL_ACTIVE_SOCKETS=[]


def respond(client_sock, portnum):
        alive =True
        #Keep checking for data until socket is closed
        while(alive == True):
                data = client_sock.recv(16)
                if("HELO" in data):
                        print 'received "%s"' % data
                        print 'sending data back to the client'
                        sendtoclient = "HELO BASE_TEST\nIP:%s\nPort:%d\nStudentID:%s" % (ip_address, portnum, STUDENT_ID)
                        client_sock.sendall(sendtoclient.encode())

                elif("KILL_SERVICE" in data):
                        alive=False
                        client_sock.close()

def main():
        parse = argparse.ArgumentParser(description='')
        parse.add_argument("-start", help="port number needed")
        argument = parse.parse_args()
        portnum = 0
        if(argument.start):
                portnum = int(argument.start)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ("10.62.0.148", portnum)
        print 'starting up on %s port %s' % server_address
        sock.bind(server_address)

        while True:
        # Waiting for a connection
                print 'waiting for a connection'
                sock.listen(5)
                client_sock, client_address = sock.accept()
                SOCKET_LIST.append(client_sock)
                ALL_ACTIVE_SOCKETS.append(client_sock)
                print 'added new socket'

                #locate and remove dead threads
                for x in thread_pool:
                        if not x.isAlive:
                                thread_pool.remove(x)
                                print 'removed thread'

                print 'connection from', client_address
                #call thread to perform response
                if(len(thread_pool) < max_threads):
                        thread = threading.Thread(target = respond, args=(SOCKET_LIST.pop(), portnum))
                        thread_pool.append(thread)
                        thread.start()
main()
