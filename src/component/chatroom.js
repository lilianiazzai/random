import React, { useState } from 'react'
import {over} from 'stompjs'
import SockJS from 'sockjs-client'

var stompClient = null;

const ChatRoom = () => {
    const [publicChats, setpublicChats] = useState([]);
    const [privateChats, setPrivateChats] = useState(new Map());
    const [tab, setTab] = useState("CHATROOM");
    const[userData, setUserData] = useState({
        username:"",
        receivername:"",
        connected:false,
        message:""
    })

    const handleValue = (event)=>{
        const {value, name} = event.target;
        setUserData({...userData, [name]:value});
    }

    const registerUser = ()=>{
        let Sock = new SockJS ('https://localhost:8080/ws')
        // termina com ws pq no backend, arquivo WebSocketConfig definimos ao stomp o
        // endpoint como sendo ws

//        stompClient = over(Sock);
//        stompClient.connect({}, onConnected, onError);
//    }
        Sock.onopen = function() {
            console.log("aberto")
        }
    }

    const onConnected = ()=>{
        setUserData({...userData, "connected":true})
        stompClient.subscribe('/chatroom/public', onPublicMessageReceived);
        stompClient.subscribe('/user/'+userData.username+'/private', onPrivateMessageReceived);
        userJoin();
    }

    // Avisa o servidor quando um usuario entra
    const userJoin = ()=>{
        
        let chatMessage = {
            senderName: userData.username,
            status: 'JOIN'
        };
        stompClient.send('/app/message', {}, JSON.stringify(chatMessage));
    
    }

    const onError = (err)=>{
        console.log(err);
    }

    const onPublicMessageReceived = (payload)=>{
        let payloadData = JSON.parse(payload.body);

        switch(payloadData.status) {
            case "JOIN":
                if (!privateChats.get(payloadData.senderName)) {
                    privateChats.set(payloadData.senderName, []);
                    setPrivateChats(new Map (privateChats));
                }
                break;

            case "MESSAGE":
                publicChats.push(payloadData);
                setpublicChats([...publicChats]);
                break;
        }
    }

    const onPrivateMessageReceived = (payload)=>{
        console.log(payload)
        let payloadData = JSON.parse(payload.body);
        if (privateChats.get(payloadData.senderName)) {
            privateChats.get(payloadData.senderName).push(payloadData);
            setPrivateChats(new Map(privateChats));
        } else {
            let list = [];
            list.push(payloadData);

            privateChats.get(payloadData.senderName, list);
            setPrivateChats(new Map(privateChats));
        }
    }

    const sendPublicMessage = ()=>{
        if (stompClient) {
            let chatMessage = {
                senderName: userData.username,
                message: userData.message,
                status: 'MESSAGE'
            };
            stompClient.send('/app/message', {}, JSON.stringify(chatMessage));
            setUserData({...userData, "message": ""});
        }
    }

    const sendPrivateMessage = ()=>{
        if (stompClient) {
            let chatMessage = {
                senderName: userData.username,
                receiverName: tab,
                message: userData.message,
                status: 'MESSAGE'
            };

            // Caso mande uma msg p si msm, o servidor responde direto
            if (userData.username !== tab) {
                privateChats.get(tab).push(chatMessage);
                setPrivateChats(new Map(privateChats));
            }
            stompClient.send('/app/private-message', {}, JSON.stringify(chatMessage));
            setUserData({...userData, "message": ""});
        }
    }


    return (
        <div className='container'>
            {userData.connected?
            <div className='chat-box'>
                <div className='member-list'>
                    <ul>
                        <li onClick={() => { setTab("CHATROOM") }} className={`member ${tab === "CHATROOM" && "active"}`}>Chatroom</li>
                        {[...privateChats.keys()].map((name, index) => (
                        <li onClick={() => { setTab(name) }} className={`member ${tab === name && "active"}`} key={index}>
                            {name}
                        </li>
                        ))}
                    </ul>
                    </div>

                {tab === "CHATROOM" && <div className = 'chat-content'>
                    <ul className='chat-messages'>
                    {publicChats.map((chat, index)=>(
                        <li className = 'message' key = {index}>
                            {chat.senderName !== userData.username && <div className='avatar'>{chat.senderName}</div>}
                                <div className='message-data'>{chat.message}</div>
                            {chat.senderName === userData.username && <div className='avatar self'>{chat.senderName}</div>}
                        </li>
                    ))}
                    </ul>

                    <div className='send-message'>
                        <input type='text' className='input-message'
                            name='message' placeholder='digite uma mensagem publica' value={userData.message}
                            onChange={handleValue} />
                        <button type='button' className='send-button' onClick={sendPublicMessage}>send</button>

                    </div>

                </div>}
                {tab !== "CHATROOM" && <div className = 'chat-content'>
                <ul className='chat-messages'>
                    {[...privateChats.get(tab)].map((chat, index)=>(
                        <li className = 'message' key = {index}>
                            {chat.senderName !== userData.username && <div className='avatar'>{chat.senderName}</div>}
                            <div className='message-data'>{chat.message}</div>
                            {chat.senderName === userData.username && <div className='avatar self'>{chat.senderName}</div>}
                        </li>
                    ))}
                    </ul>

                    <div className='send-message'>
                        <input type='text' className='input-message'
                            name = 'message' placeholder={`digite uma mensagem para ${tab}`} value={userData.message}
                            onChange={handleValue} />
                        <button type='button' className='send-button' onClick={sendPrivateMessage}>send</button>

                    </div>

                </div>}

            </div>
            :
            <div className='register'>
                <input
                id='user-name'
                name = 'username'
                placeholder='nome de usuario'
                value={userData.username}
                onChange={handleValue}
                />

                <button type='button' onClick={registerUser}>
                    connect
                </button>

            </div>

        }</div>  // antes tava sem essa chave
    )

}

export default ChatRoom