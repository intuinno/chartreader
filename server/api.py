from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('url', type=str)


def build_table(url): 
    table = '<table><caption>' + url + '</caption>   <tr>     <th scope="col">Name</th>    <th scope="col">Age</th>    <th scope="col">Birthday</th>    </tr>    <tr>     <th scope="row">Jackie</th>     <td>5</td>     <td>April 5</td>     </tr>     <tr>     <th scope="row">Beth</th>     <td>8</td>     <td>January 14</td>     </tr> 12</table>'
    return { 'table': table }



class HelloWorld(Resource):
    def get(self):
        return table 

class ChartReader(Resource):
    def post(self):
        args = parser.parse_args()
        chart_url = str(args['url'])
        return build_table(chart_url) 



api.add_resource(HelloWorld,'/')
api.add_resource(ChartReader, '/chart')

if __name__ == '__main__':
    app.run(debug=True)


