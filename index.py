import cv2
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open("index.html", "r") as file:
                self.wfile.write(file.read().encode('utf-8'))
        elif self.path == '/video_feed':
            self.send_response(200)
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=frame')
            self.end_headers()
            self.stream_video()
        else:
            self.send_response(404)
            self.end_headers()

    def stream_video(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Convert the frame to grayscale
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)  # Convert back to 3-channel image

            # Encode the frame as JPEG
            ret, jpeg = cv2.imencode('.jpg', gray_frame)
            if not ret:
                continue

            # Write the JPEG image as a multipart response
            self.wfile.write(b'--frame\r\n')
            self.wfile.write(b'Content-Type: image/jpeg\r\n\r\n')
            self.wfile.write(bytearray(jpeg))
            self.wfile.write(b'\r\n\r\n')

            time.sleep(0.05)  # Control frame rate

        cap.release()

def run(server_class=HTTPServer, handler_class=handler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
