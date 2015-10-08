#import socket module 
#Fill in
#Create serverSocket 
#Fill in
#Prepare a seversocket with port #
#Fill in
while True: 
    print 'Ready to serve...' 
    #generate connection socket and establish the connection
    #Fill in 
    try:
        #receive HTTP request 
        #Fill in 
        #tokenize HTTP message header
        #Fill in
        #find filename in the message string array *use split function
        #Fill in
        #open the requested file
        #Fill in
        #read the file into a string
        #Fill in
        #close the file
        #Fill in
        #Send one HTTP header line into socket *check the header for 200 OK, and add an empty line at the end
        #Fill in 
        #Send the data content of the requested file to the client (may need a loop)
        #Fill in 
        #close connection socket
        #Fill in 
    except IOError: 
        #Send response message for file not found including a 404 header and a 404 html
        #Fill in 
    except Exception:
        #print an error message to the console for any other exception 
        #Fill in 
    finally:
        #Close client socket 
        #Fill in 
#close serversocket 	
#Fill in
