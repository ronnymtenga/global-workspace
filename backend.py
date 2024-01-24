from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
from main import Cart
import json

#server location or id
HOST = "localhost"
PORT = 8000


class myHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>CAN'T WAIT TO WORK AT WOLT!!!</h1></body></html>", "utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])

        raw_post_data = self.rfile.read(content_length)

        try:
            data = json.loads(raw_post_data.decode('utf-8'))
        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'Invalid JSON data')

        cart_value = data.get('cart_value', 0)
        delivery_distance = data.get('delivery_distance', 0)
        number_of_items = data.get('number_of_items', 0)
        Time = datetime.strptime(data.get('time', 'No time provided'), "%Y-%m-%dT%H:%M:%SZ")

        day_of_week = datetime.weekday(Time)
        hours = Time.hour
        
        flag = False
        if day_of_week == 4 and hours > 15 and hours <  19: flag = True

        Cart1 = Cart(cart_value, delivery_distance, number_of_items, flag)

        #date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        response_data = {'status': 'success', 'delivery_fee': Cart1.calculate()}
        response_JSON = json.dumps(response_data).encode('utf-8')

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header('Content-Length', len(response_JSON))
        self.end_headers()

        self.wfile.write(response_JSON)

server = HTTPServer((HOST, PORT), myHTTP)
print("Server now running...")
server.serve_forever()


