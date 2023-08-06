import socket
import pickle


def send_filters(filters, host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Serialize and send the filters to the microservice
    serialized_data = pickle.dumps(filters)
    client_socket.send(serialized_data)

    # Receive and deserialize the filtered data from the microservice
    data = client_socket.recv(4096)
    filtered_data = pickle.loads(data)

    client_socket.close()
    return filtered_data


if __name__ == "__main__":
    filters = {
        "Name": "Running"
    }

    host, port = "localhost", 12345

    filtered_data = send_filters(filters, host, port)
    print(filtered_data)
