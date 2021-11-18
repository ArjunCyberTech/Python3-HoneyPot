from socket import *

def main():
	print(
    '''
   █████████                  ███                                                             
  ███░░░░░███                ░░░                                                              
 ░███    ░███  ████████      █████ █████ ████ ████████                                        
 ░███████████ ░░███░░███    ░░███ ░░███ ░███ ░░███░░███                                       
 ░███░░░░░███  ░███ ░░░      ░███  ░███ ░███  ░███ ░███                                       
 ░███    ░███  ░███          ░███  ░███ ░███  ░███ ░███                                       
 █████   █████ █████         ░███  ░░████████ ████ █████                                      
░░░░░   ░░░░░ ░░░░░          ░███   ░░░░░░░░ ░░░░ ░░░░░                                       
                         ███ ░███                                                             
                        ░░██████                                                              
                         ░░░░░░                                                               
   █████████             █████                        ███████████                   █████     
  ███░░░░░███           ░░███                        ░█░░░███░░░█                  ░░███      
 ███     ░░░  █████ ████ ░███████   ██████  ████████ ░   ░███  ░   ██████   ██████  ░███████  
░███         ░░███ ░███  ░███░░███ ███░░███░░███░░███    ░███     ███░░███ ███░░███ ░███░░███ 
░███          ░███ ░███  ░███ ░███░███████  ░███ ░░░     ░███    ░███████ ░███ ░░░  ░███ ░███ 
░░███     ███ ░███ ░███  ░███ ░███░███░░░   ░███         ░███    ░███░░░  ░███  ███ ░███ ░███ 
 ░░█████████  ░░███████  ████████ ░░██████  █████        █████   ░░██████ ░░██████  ████ █████
  ░░░░░░░░░    ░░░░░███ ░░░░░░░░   ░░░░░░  ░░░░░        ░░░░░     ░░░░░░   ░░░░░░  ░░░░ ░░░░░ 
               ███ ░███                                                                       
              ░░██████                                                                        
               ░░░░░░                                                                         
                                                            
    '''
)
	ip_add = input("Enter the IP Address: ")
	port = int(input("Enter the port number: "))
	message = input("Enter the message: ")
	m = "<h1>" + message + "</h1>"
	print("[+] Honeypot Start ......")
	try:
		get_socket_con = socket(AF_INET, SOCK_STREAM)
		get_socket_con.bind((ip_add,port))
		get_socket_con.listen(10)
		while 1:
			client_con,client_addr = get_socket_con.accept()
			print("Vister found ! - [{}]".format(client_addr[0]))
			client_con.send(m.encode())
			data = client_con.recv(2048)
			print(data.decode('utf-8'))
	except error as identifier:
		print("[+] Unspecified error [{}]".format(identifier))
	except KeyboardInterrupt as ky:
		print("[-] Process stopped !")
	finally:
		get_socket_con.close()


if __name__ == "__main__":
	main()
