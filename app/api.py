from app import app
from flask import Flask, abort
from app import db_connect
import json

@app.route('/')
def index():
	msg = "This is an API endpoint for the database kaalumine"
	return msg

@app.route('/weights/', methods = ['GET'])
def weights():
	try:
		cur = db_connect.connect()
		query = """SELECT * FROM weights LIMIT 100;"""
		cur.execute(query)
		row_headers=[x[0] for x in cur.description] # automagically get row headers 
		data = cur.fetchall()
	except Exception as e:
		print ("Here comes an error")
		abort(404)

	result = []
	for row in data:
		#determines what rows to print
		result.append(dict(zip(row_headers, (int(row['id']), row['sample_id'], row['sensor_id'], row['date'].strftime("%Y-%m-%d"), row['time'].strftime("%H:%M"), row['weight']))))
	return json.dumps(result)

@app.route('/weights/sensor/<int:sens_id>', methods = ['GET'])
def sensor_id(sens_id):
	try:
		cur = db_connect.connect()
		query = """SELECT * FROM weights WHERE sensor_id=""" + str(sens_id) + """;"""
		cur.execute(query)
		row_headers=[x[0] for x in cur.description] # automagically get row headers 
		data = cur.fetchall()
	except Exception as e:
		print ("Here comes an error")
		abort(404)

	result = []
	for row in data:
		#determines what rows to print
		result.append(dict(zip(row_headers, (int(row['id']), row['sample_id'], row['sensor_id'], row['date'].strftime("%Y-%m-%d"), row['time'].strftime("%H:%M"), row['weight']))))
	return json.dumps(result)

@app.route('/weights/sample/<int:sample_id>', methods = ['GET'])
def sample_id(sample_id):
	try:
		cur = db_connect.connect()
		query = """SELECT * FROM weights WHERE sample_id=""" + str(sample_id) + """;"""
		cur.execute(query)
		row_headers=[x[0] for x in cur.description] # automagically get row headers 
		data = cur.fetchall()
	except Exception as e:
		print ("Here comes an error")
		abort(404)

	result = []
	for row in data:
		#determines what rows to print
		result.append(dict(zip(row_headers, ( int(row['id']), row['sample_id'],row['sensor_id'], row['date'].strftime("%Y-%m-%d"), row['time'].strftime("%H:%M"), row['weight']))))
	return json.dumps(result)

@app.route('/weights/desc/sensor/<int:sens_id>', methods = ['GET'])
def sensor(sens_id):
	try:
		cur = db_connect.connect()
		query = """SELECT * FROM sensor WHERE sensor_id=""" + str(sens_id) + """;"""
		cur.execute(query)
		row_headers=[x[0] for x in cur.description] # automagically get row headers 
		data = cur.fetchall()
	except Exception as e:
		print ("Here comes an error")
		abort(404)

	result = []
	for row in data:
		#determines what rows to print
		result.append(dict(zip(row_headers, (int(row['sensor_id']), row['description'], ))))
	return json.dumps(result)

@app.route('/weights/desc/sample/<int:sample_id>', methods = ['GET'])
def sample(sample_id):
	try:
		cur = db_connect.connect()
		query = """SELECT * FROM sample_w WHERE sample_id=""" + str(sample_id) + """;"""
		cur.execute(query)
		row_headers=[x[0] for x in cur.description] # automagically get row headers 
		data = cur.fetchall()
	except Exception as e:
		print ("Here comes an error")
		abort(404)

	result = []
	for row in data:
		#determines what rows to print
		result.append(dict(zip(row_headers, (int(row['sample_id']), row['description'], ))))
	return json.dumps(result)

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')