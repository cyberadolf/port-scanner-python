from socket import *
ip = input("enter ip address:")
port_start=int(input("STARTING PORT NUMBER:"))
port_stop=int(input("STOPING PORT NUMBER:"))
main_array=[]
for port in range(port_start,port_stop+1):
    addr=(ip,port)
    s=socket(AF_INET,SOCK_STREAM)
    result=s.connect_ex(addr)
    setdefaulttimeout(0.01)
    s.close() 
    if(result==0):
        print("the port number {} is open".format(port))
        main_array.append(port)
    else:
            print("the port number {} is not open".format(port))
print("_"*40)
print("the scanning is done..")
print("the ports which are open:")
print(main_array)
