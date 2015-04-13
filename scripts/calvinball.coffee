module.exports = (robot) ->

  robot.hear /add (.*)/i, (res) ->
		data = JSON.stringify({
			rule_string: res.match[1]
		})
		robot.http("http://localhost:8080/add")
			.post(data) (err, res, body) ->
				if err
					res.send "Something went wrong #{err}"
					return
				result = JSON.parse(body)
				if result.err
					res.send "error: #{result.err_msg}"
					return
				res.send result.msg

  robot.hear /remove (.*)/i, (res) ->
		data = JSON.stringify({
			rule_string: res.match[1]
		})
		robot.http("http://localhost:8080/remove")
			.post(data) (err, res, body) ->
				if err
					res.send "Something went wrong #{err}"
					return
				result = JSON.parse(body)
				if result.err
					res.send "error: #{result.err_msg}"
					return
				res.send result.msg

  robot.hear /list/i (res) ->
		robot.http("http://localhost:8080/list")
			.get(data) (err, res, body) ->
				if err
					res.send "Something went wrong #{err}"
					return
				result = JSON.parse(body)
				if result.err
					res.send "error: #{result.err_msg}"
					return
				res.send result.msg
