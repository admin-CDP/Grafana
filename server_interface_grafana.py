import requests
import json
from json_generator import json_generator
from http.server import BaseHTTPRequestHandler, HTTPServer

"""Le code est immonde et j'en suis conscient"""

token = "glsa_kjmdxYEXOiMPfbp2t1PWVv1zwNqLYF5r_01404515"
firm = "\"Coup de Pousse\""


headers = {"Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer "+token}



class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        #We get the content of request
        try : 
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            json_data = json.loads(post_data.decode('utf-8'))
            print(json_data)
            firm = json_data["company"]
            

        except Exception as e:
            print('The request do not match our requierements',e)
        #Then we get all the dashboards from grafana

        try :
            r = requests.get('http://54.37.8.214:3000/api/search?folderIds=0&query=&starred=false',headers = headers)
            response = r.json()

            for dash in response :
                print(dash['title'])
                print(firm)
                if firm in dash['title']:
                    uid = dash['uid']
            print(uid)
        
            r = requests.get('http://54.37.8.214:3000/api/dashboards/uid/'+uid, headers = headers)
            print(f"Status Code: {r.status_code}, Response: {r.json()}")

            json_dash = r.json()

            json_dash['dashboard']['id'] = None
            json_dash['dashboard']['uid'] = None
            json_dash['dashboard']['title'] = 'test_'+firm
            for object in json_dash['dashboard']["panels"][0]["transformations"]:
                if object["id"]=='filterByValue' and object["options"]["filters"][0]["fieldName"] == "Company":
                    print("oui")
                    object["options"]["filters"][0]["config"]["options"]["value"] = firm


            r = requests.post('http://54.37.8.214:3000/api/dashboards/db', headers = headers, json = json_dash)
            #print(f"Status Code: {r.status_code}, Response: {r.json()}")
        except Exception as e:
            print('Problem during request to grafana database : ',e)


        
        try : 
            processed_data = {'received_data': json_dash}
            self.send_response(200)
            self.send_header('Content-type', 'application/json', 'Access-Control-Allow-Origin', 'http://89.82.239.21')
            self.end_headers()
            self.wfile.write(json.dumps(processed_data).encode('utf-8'))
            print('OUI')

        except Exception as e:
            print('Error while retriving information to the client',e)


if __name__ == '__main__':
    
    server_address = ('', 8081)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Starting server on port 8080...')
    httpd.serve_forever()


