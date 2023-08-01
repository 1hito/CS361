# CS361
Communication contract of my microservice:
1. How to programmatically REQUEST data from the microservice you implemented. Include an example call.
   You can set the desired filters in the format of: filters = {"Column1" : "Value1", "Column2" : "Value2", ...}
   Then, you can send the serialized filters via socket module.
   First, create the socket object on the client side (e.g. client_socket) with the same host(e.g. "localhost") and port(e.g. 12345) of the microservice.
   Then use client.socket.send(pickle.dumps(filters)) to send the filters to the microservice and request the filtered data.
   
2. Clear instructions for how to programmatically RECEIVE data from the microservice you implemented.
   Once the request is made, the microservice will return the filtered data via socket.
   You can recieve the data by using filtered_data = pickle.loads(client_socket.recv(4096))
   The received data contains the filtered data in the format of a list of dict. (e.g. [{'Column1': 'Value1', 'Column2': 'Value2', 'Column3': 'Value3'...}, {}...,])
   
3. UML sequence diagram![CS361UML](https://github.com/1hito/CS361/assets/96344873/1c12ce0c-8a68-4d82-9262-c0b5f898642f)
