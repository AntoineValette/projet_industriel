import socket
import time

def wait_for_service(host, port, timeout=60):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            with socket.create_connection((host, port), timeout=5):
                print(f"Kafka est prêt sur {host}:{port}")
                return True
        except (OSError, ConnectionRefusedError):
            print(f"Attente de Kafka sur {host}:{port}...")
            time.sleep(5)
    raise Exception(f"Kafka n'est pas accessible après {timeout} secondes")

if __name__ == "__main__":
    wait_for_service("kafka", 9092)