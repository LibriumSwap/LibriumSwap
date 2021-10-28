    var other_username = "{{ other_username }}";
	const chatSocket = new ReconnectingWebSocket(
        'ws://'
        + window.location.host
        + '/ws'
        + window.location.pathname
    );
    chatSocket.onopen = function(e){
    	console.log("Connection is opened");
    }

    chatSocket.onmessage = function(e){
    	const data = JSON.parse(e.data);
        var msgListTag = document.createElement('li');
        var pTag = document.createElement('p');
        var imgTag = document.createElement('img');
        pTag.textContent = data.message;
        imgTag.src = 'http://emilcarlsson.se/assets/harveyspecter.png';
        msgListTag.className = 'sent';
        msgListTag.appendChild(imgTag);
        msgListTag.appendChild(pTag);
        
        
        document.querySelector('.chat-log').appendChild(msgListTag);
    }

    chatSocket.onclose = function(e){
    	console.log("Connection is closed");
    }

    chatSocket.onerror = function(e){
    	console.error('Chat socket closed unexpectedly');
    }

    document.querySelector('.chat-message-input').focus();
    document.querySelector('.chat-message-input').onkeyup = function(e) {
        if (e.keyCode === 13) {  // enter, return
            document.querySelector('.chat-message-submit').click();
        }
    };

    document.querySelector('.chat-message-submit').onclick = function(e) {
        const messageInputDom = document.querySelector('.chat-message-input');
        const message = messageInputDom.value;
        chatSocket.send(JSON.stringify({
            'message': message,
        }));
        messageInputDom.value = '';
    };