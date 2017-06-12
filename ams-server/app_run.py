from flask import *
from datetime import datetime
from dbModel import *
import urllib
import base64
import imageprocessing
import generatingqrcode

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/API/get_dates', methods=['GET'])
def get_dates():
    cid = request.args.get('cid')
    if  cid:
        if type(cid) is str:
            return jsonify({'dates':["12-5-2017","4-1-2017","5-8-2017","7-4-2017"]})
        else: 
            return error_type_mismatch()
            
    else:
         return error_empty()
         
        
@app.route('/API/get_record', methods=['GET'])
def get_record():
    date = request.args.get('date')
    cid = request.args.get('cid')
    pid = request.args.get('pid')
    if  cid and  pid and date:
        pid = int(pid)
        if type(cid) is str and type(pid) is int and type(date) is str:
            return render_template("%s/%s.json" % (cid, date))
        else:
            return error_type_mismatch()
            
    else:
        return error_empty()
        
    
@app.route('/API/post_record', methods=['POST'])
def post_record():
    date = request.get_json()
    return date
    #time = request.args.get('time')
    #cid = request.args.get('cid')
    #pid = request.args.get('pid')
    #lat = request.args.get('lat')
    #lng = request.args.get('lng')
    #attendance = request.args.get('attendance')
   # if  cid and  pid and  date and  time and lat and lng:
        #date = urllib.parse.unquote_plus(date)
        #time = urllib.parse.unquote_plus(time)
        #cid = urllib.parse.unquote_plus(cid)
        #pid = int(pid)
        #lat = float(lat)
        #lng = float(lng)
        #attendance = bytes(attendance,'utf-8')
        #if type(cid) is str and  type(time) is str and type(pid) is int and type(date) is str and type(lat) is float and type(lng) is float:
            #return jsonify({'status':'success', 'message':'request is received successfully'}), 200
           # return base64.decodestring(attendance)
        #else:
            #return error_type_mismatch()
            
   # else:
      #  return error_empty()
        
    
@app.route('/API/post_edit_record', methods=['PUT', 'DELETE'])
def post_edit_record():
    date = request.args.get('date')
    time = request.args.get('time')
    cid = request.args.get('cid')
    pid = request.args.get('pid')
    sid = request.args.get('sid')
    
    if  cid and  pid and  date and  time and sid:
        date = urllib.parse.unquote_plus(date)
        time = urllib.parse.unquote_plus(time)
        cid = urllib.parse.unquote_plus(cid)
        pid = int(pid)
        sid = int(sid)
        if type(cid) is str and  type(time) is str and type(pid) is int and type(date) is str and type(sid) is int:
            if request.method == 'PUT':
                return jsonify({'status':'success', 'message':'request is received successfully'}), 200
            else:
                return jsonify({'status':'success', 'message':'request is received successfully'}), 200
        else:
            return error_type_mismatch()
               
    else:
        return error_empty()
        
    
@app.route('/API/auth', methods=['GET'])
def authentication():
    password = request.args.get('password')
    username = request.args.get('username')
    if password and username:
        if type(password) is str and type(username) is str:
            return render_template('Pro.json')
        else:
            return error_type_mismatch()
            
    else:
        return error_empty()
        
    
def error_empty():
    return jsonify({'status':'failed', 'message':'Requested parameters are empty'})

def error_type_mismatch():
     return jsonify({'status':'failed', 'message':'Requested parameters\' type mismatch'})
    
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'status':'failed', 'message':'bad request'}), 400

@app.errorhandler(401)
def unauthorized(error):              
    return jsonify({'status':'failed', 'message':'authentication is required and has failed or has not yet been provided'}), 401

@app.errorhandler(403)
def forbidden(error):              
    return jsonify({'status':'failed', 'message':'The request was valid, but the server is refusing action'}), 403

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'status':'failed', 'message':'This URL does not exist'}), 404

@app.errorhandler(405)
def mathod_not_allowed(error):              
    return jsonify({'status':'failed', 'message':'The method is not allowed for the requested URL'}), 405

@app.errorhandler(406)
def not_acceptable(error):              
    return jsonify({'status':'failed', 'message':'The requested resource is capable of generating only content not acceptable'}), 406

@app.errorhandler(408)
def request_timeout(error):              
    return jsonify({'status':'failed', 'message':'The server timed out waiting for the request'}), 408

@app.errorhandler(409)
def conflict(error):              
    return jsonify({'status':'failed', 'message':'Indicates that the request could not be processed because of conflict in the request'}), 409

@app.errorhandler(410)
def gone(error):              
    return jsonify({'status':'failed', 'message':'Indicates that the resource requested is no longer available and will not be available again'}), 410

@app.errorhandler(414)
def urltolong(error):              
    return jsonify({'status':'failed', 'message':'The URI provided was too long for the server to process'}), 414



if __name__ == '__main__':
    app.run(debug=True )
