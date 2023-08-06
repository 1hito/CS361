import socket
import pickle
import pandas as pd


def get_data(filters):
    # Path to the Excel file
    df = pd.read_excel('workouts.xlsx')

    # Apply the filters received from the client
    for column, value in filters.items():
        df = df[df[column] == value]

    # Convert the filtered data back to a list of dictionaries
    filtered_data = df.to_dict(orient='records')

    return filtered_data


def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connection established with {addr}")

        # Receive filters from the client
        data = conn.recv(4096)
        filters = pickle.loads(data)

        # Get the filtered data
        filtered_data = get_data(filters)

        # Send the filtered data back to the client
        serialized_data = pickle.dumps(filtered_data)
        conn.send(serialized_data)

        conn.close()
        print(f"Connection with {addr} closed")


if __name__ == "__main__":
    start_server("localhost", 12345)
