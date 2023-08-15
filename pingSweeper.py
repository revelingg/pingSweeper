import os
import sys


def ping_sweep(ipaddr, startOct, endOct):
  cmd = f"ping -c 1 {ipaddr}"
  startOct = (int)(startOct)
  endOct = (int)(endOct)
  results = []

  for octet in range(startOct, endOct + 1):
    #checks the octet in the range and for each one add it to the back of the Ip and try it 
    ipaddy = f"{cmd}.{octet}"

    #resp is the response from the connection if its 0 add it to the list 
    resp = os.system(ipaddy)
    if resp == 0:
      #creates the Ip back again and adds it 
      ip = f"{ipaddr}.{octet}"
      results.append(ip)
    else :
      print("Ping didnt work")
      
  return results  
    


def main():
  #takes in the command line arguments using the sys module 
  ipaddr = sys.argv[1]
  startOct = sys.argv[2]
  endOct = sys.argv[3]

  # add error checking next time so the user doesnt  put more thsn needeed
  
  result = ping_sweep(ipaddr, startOct, endOct)
  for result in result:
    print(result)


main()
