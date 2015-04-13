module.exports = (robot) ->

  robot.hear /add (.*)/i, (res) ->
    rule_str = res.match[1]
    data = "rule_string=#{rule_str}"
    robot.http("http://localhost:8080/add")
      .post(data) (err, response, body) ->
        if err
          res.send "Something went wrong #{err}"
          return
        console.log(body)
        result = JSON.parse(body)
        if result.error
          res.send "error: #{result.error_msg}"
        else
          res.send result.msg

  robot.hear /remove (.*)/i, (res) ->
    rule_str = res.match[1]
    data = "rule_string=#{rule_str}"
    robot.http("http://localhost:8080/remove")
      .post(data) (err, response, body) ->
        if err
          res.send "Something went wrong #{err}"
          return
        result = JSON.parse(body)
        if result.error
          res.send "error: #{result.error_msg}"
        else
          res.send result.msg

  robot.hear /evaluate (.*)/i, (res) ->
    action_str = res.match[1]
    data = "action_string=#{action_str}"
    robot.http("http://localhost:8080/evaluate")
      .post(data) (err, response, body) ->
        if err
          res.send "Something went wrong #{err}"
          return
        result = JSON.parse(body)
        if result.error
          res.send "error: #{result.error_msg}"
        else
          res.send result.msg

  robot.hear /list/i, (res) ->
    robot.http("http://localhost:8080/list")
      .get() (err, response, body) ->
        if err
          res.send "Something went wrong #{err}"
          return
        result = JSON.parse(body)
        if result.error
          res.send "error: #{result.error_msg}"
        else if result.msg
          res.send result.msg
        else
          res.send "No rules yet!"
