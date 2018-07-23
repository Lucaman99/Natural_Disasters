var express = require('express')
var app = express()
var http = require('http').createServer(app)
var io = require('socket.io')(http)

app.use(express.static('im'))

app.get('/', function (req, res){
  res.sendfile('chatroom.html')
})

io.on('connection', function (socket) {
  socket.on('event1', function (data) {
    io.sockets.emit('event2', data)
  })
})

http.listen(3001, function () {
  console.log("Listening...")
})
